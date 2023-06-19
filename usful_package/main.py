import sys


def main() -> None:
    try:
        name = sys.argv[1]

    except IndexError:
        print("No name")
        return None

    print(f"Hello World, {name}")


if __name__ == "__main__":
    main()
