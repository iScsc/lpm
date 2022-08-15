import argparse


def main(args: argparse.Namespace) -> None:
    for key, value in args.__dict__.items():
        print(f"args.{key}: {value}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    default = "default-long"
    parser.add_argument(
        "--long",
        "-l",
        type=str,
        default=default,
        help=f"Some string (defaults to '{default}')",
    )

    default = [1, 2, 3]
    parser.add_argument(
        "--list",
        "-L",
        nargs=3,
        type=int,
        default=default,
        help=f"Some list of integers (defaults to {default})",
    )

    parser.add_argument(
        "--required",
        "-r",
        type=str,
        required=True,
        help="Some required string",
    )

    choices = ["choice_1", "choice_2", "choice_3"]
    default = choices[-1]
    parser.add_argument(
        "--choice",
        "-c",
        type=str,
        choices=choices,
        default=default,
        help=f"Some string with restricted choices (defaults to '{default}')",
    )

    parser.add_argument(
        "positional",
        nargs="+",
        help="Some positional arguments",
    )

    args = parser.parse_args()
    main(args)