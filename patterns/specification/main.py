from dataclasses import dataclass
from pathlib import Path

from .spec import SpecRule, load_spec_rule_from_file, spec_rule, spec_rule_with_args


@dataclass
class User:
    "User account."

    id: int
    is_admin: bool
    is_active: bool
    account_age: int
    is_banned: bool
    country: str
    credit_score: int
    has_manual_override: bool


@spec_rule
def is_admin(u: User) -> bool:
    "Check if user is admin."
    return u.is_admin


@spec_rule
def is_active(u: User) -> bool:
    "Check if user is active."
    return u.is_active


@spec_rule
def is_banned(u: User) -> bool:
    "Check if user is banned."
    return u.is_banned


@spec_rule
def has_override(u: User) -> bool:
    "Check if user has manual override."
    return u.has_manual_override


@spec_rule_with_args
def account_older_than(u: User, age: int) -> bool:
    "Check if user account is older than given age."
    return u.account_age > age


@spec_rule_with_args
def from_country(u: User, *countries: str) -> bool:
    "Check if user account belongs to any of the given countries."
    return u.country in countries


@spec_rule_with_args
def credit_score_above(u: User, threshold: int) -> bool:
    "Check if user credit score is above given threshold."
    return u.credit_score > threshold


api_check = is_admin | (
    is_active
    & account_older_than(30)
    & ~is_banned
    & from_country("NL", "BE")
    & (credit_score_above(650) | has_override)
)


def reporting(users: list[User]) -> list[User]:
    "List users that meet reporting criteria."
    return [u for u in users if api_check(u)]


def cli_export(users: list[User]) -> list[User]:
    "List users that meet CLI export criteria."
    return [u for u in users if api_check(u)]


def main() -> None:
    "Application entrypoint."
    print("Hello from specification!")
    users = [
        User(
            id=1,
            is_admin=False,
            is_active=True,
            account_age=100,
            is_banned=False,
            country="US",
            credit_score=800,
            has_manual_override=False,
        ),
        User(
            id=2,
            is_admin=False,
            is_active=True,
            account_age=100,
            is_banned=False,
            country="BE",
            credit_score=800,
            has_manual_override=False,
        ),
    ]
    print("\n=== Access via Config rule ===")
    for u in reporting(users):
        print(u)

    try:
        rule: SpecRule[User] = load_spec_rule_from_file(
            Path(__file__).parent / "rule_config.json",
        )
        print("\n=== Access via Config rule ===")
        for u in users:
            print(u, "=>", rule(u))
    except FileNotFoundError:
        print("Specification rule file not found.")


if __name__ == "__main__":
    main()
