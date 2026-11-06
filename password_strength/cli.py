"""Command-line interface for the password strength checker."""

import argparse
import getpass
import sys

from .checker import check_password


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Check a password's strength using simple local heuristics."
    )
    parser.add_argument(
        "password",
        nargs="?",
        help="password to check (omit this argument to enter it securely)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    password = args.password if args.password is not None else getpass.getpass("Password: ")
    result = check_password(password)

    print(f"Score: {result.score}/{result.maximum_score} ({result.label})")
    if result.tips:
        print("Tips:")
        for tip in result.tips:
            print(f"- {tip}")
    else:
        print("Tips: Keep using unique passwords and a password manager.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
