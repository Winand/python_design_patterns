from collections import defaultdict
from collections.abc import Callable
from types import MethodType
from typing import TYPE_CHECKING, Any
from weakref import WeakMethod
from weakref import ref as _ref

if TYPE_CHECKING:
    from weakref import ReferenceType

EventCallback = Callable[[Any], None]

_subscribers: dict[str, list[ReferenceType[EventCallback]]] = defaultdict(list)


def ref[C](func: C) -> ReferenceType[C]:
    "Create a weak reference for a function or method."
    if isinstance(func, MethodType):
        return WeakMethod(func)
    if getattr(func, "__name__", None) == "<lambda>":
        msg = "Lambda functions are not supported in this context"
        raise ValueError(msg)
    return _ref(func)


def subscribe(event_type: str, callback: EventCallback) -> None:
    "Subscribe to an event type."
    _subscribers[event_type].append(ref(callback))


def post_event(event_type: str, data: Any) -> None:  # noqa: ANN401
    "Post a new event."
    for callback_ref in _subscribers[event_type]:
        if callback := callback_ref():
            callback(data)
