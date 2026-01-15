import sys


def print_argv(argv: list[str]) -> None:
    argv_len = len(argv)
    if argv_len < 2:
        print("No arguments provided!")
        print(f"Program name: {argv[0]}")
    else:
        print(f"Program name: {argv[0]}")
        print(f"Arguments received: {argv_len - 1}")
        ind = 1
        while ind < argv_len:
            print(f"Argument {ind}: {argv[ind]}")
            ind += 1
    print(f"Total arguments: {argv_len}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    print_argv(sys.argv)
