import json
from collections.abc import Callable
from functools import reduce, wraps
from operator import __and__, __or__
from typing import TYPE_CHECKING, Any, Concatenate

if TYPE_CHECKING:
    from pathlib import Path

type PredicateFunc[T] = Callable[[T], bool]
type PredicateFuncWithArgs[T, **P] = Callable[Concatenate[T, P], bool]
type SpecRuleFactory[T, **P] = Callable[P, SpecRule[T]]

RULE_REGISTRY: dict[str, SpecRule[Any] | SpecRuleFactory[Any, ...]] = {}
OP = {"and": __and__, "or": __or__}


class SpecRule[T]:
    "A composable predicate that supports logical operations &, |, and ~."

    def __init__(self, func: PredicateFunc[T]) -> None:
        "Initialize the predicate with a function."
        self.func = func

    def __call__(self, obj: T) -> bool:
        "Evaluate the predicate function."
        return self.func(obj)

    def __and__(self, other: SpecRule[T]) -> SpecRule[T]:
        "Combine two predicates using logical AND."
        return SpecRule(lambda u: self(u) and other(u))

    def __or__(self, other: SpecRule[T]) -> SpecRule[T]:
        "Combine two predicates using logical OR."
        return SpecRule(lambda u: self(u) or other(u))

    def __invert__(self) -> SpecRule[T]:
        "Invert the predicate."
        return SpecRule(lambda u: not self(u))


def spec_rule[T](func: PredicateFunc[T]) -> SpecRule[T]:
    "Specification rule without additional arguments."
    predicate = SpecRule(func)
    RULE_REGISTRY[func.__name__] = predicate
    return predicate


def spec_rule_with_args[T, **P](
    func: PredicateFuncWithArgs[T, P],
) -> SpecRuleFactory[T, P]:
    "Specification rule with additional arguments."

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> SpecRule[T]:  # noqa: ANN401
        return SpecRule(lambda obj: func(obj, *args, **kwargs))

    RULE_REGISTRY[func.__name__] = wrapper
    return wrapper


def load_spec_rule_from_file(path: Path) -> SpecRule[Any]:
    """
    Load a specification rule from a JSON file.

    Format:
    {
        "logic": "and",
        "conditions": [
            { "name": "is_active", "args": [] },
            { "name": "older_than", "args": [30] }
        ]
    }
    """
    with path.open() as f:
        config = json.load(f)
    preds: list[SpecRule[Any]] = []
    for cond in config["conditions"]:
        name = cond["name"]
        args = cond.get("args", [])

        if name not in RULE_REGISTRY:
            msg = f"Unknown rule: {name}"
            raise ValueError(msg)
        predicate = RULE_REGISTRY[name]
        if not isinstance(predicate, SpecRule):
            predicate = predicate(*args)
        preds.append(predicate)
    operation = OP[config["operation"]]
    return reduce(operation, preds)
