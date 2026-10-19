"""PyArgentis - Example App #2"""


app_name= "PyArgentis Example #2"
build_tag = "example-2026"


def compute_token(seed: int) -> str:
    value = (seed * 17 + 42) % 1000
    return f"{build_tag}-{value:03d}"


def main() -> None:
    print(app_name)
    print(f"Build: {build_tag}")
    token = compute_token(7)
    print(f"Token: {token}")


if __name__ == "__main__":
    main()
