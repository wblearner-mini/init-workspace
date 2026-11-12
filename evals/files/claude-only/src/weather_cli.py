import sys


def main() -> None:
    city = sys.argv[1] if len(sys.argv) > 1 else "Paris"
    print(f"Forecast for {city}: not implemented yet")


if __name__ == "__main__":
    main()
