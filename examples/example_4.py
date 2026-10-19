"""PyArgentis - Example App #4"""

APP_NAME = "PyArgentis Example #4"
SALT = 0x5A17


def checksum(text: str) -> int:
    total = SALT
    for char in text:
        total = (total + ord(char) * 31) % 9973
    return total


def verify_access(code: str) -> bool:
    expected = checksum("demo-access")
    return checksum(code) == expected


def main() -> None:
    print(APP_NAME)
    code = "demo-access"
    status = "granted" if verify_access(code) else "denied"
    print(f"Access: {status}")
    print(f"Check: {checksum(code)}")


if __name__ == "__main__":
    main()
