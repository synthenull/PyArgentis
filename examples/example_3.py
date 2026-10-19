"""PyArgentis - Example App #3"""

APP_NAME = "PyArgentis Example #3"
VERSION = "0.3.0"

PLANS = {
    "starter": 9,
    "pro": 29,
    "team": 79,
}


def format_price(plan: str) -> str:
    amount = PLANS.get(plan)
    if amount is None:
        return "unknown plan"
    return f"${amount}/mo"


def main() -> None:
    print(APP_NAME)
    print(f"Version: {VERSION}")
    for plan in ("starter", "pro", "team"):
        print(f"{plan:>8}: {format_price(plan)}")


if __name__ == "__main__":
    main()
