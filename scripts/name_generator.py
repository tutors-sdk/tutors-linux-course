import argparse
import random
from itertools import product

FIRST_NAMES = [
    "Oliver",
    "Amelia",
    "William",
    "Sophia",
    "James",
    "Charlotte",
    "Henry",
    "Emily",
    "Alexander",
    "Grace",
    "Edward",
    "Eleanor",
    "Samuel",
    "Alice",
    "Arthur",
    "Victoria",
    "Thomas",
    "Lucy",
    "Charles",
    "Isla",
    "George",
    "Lily",
    "Daniel",
    "Hannah",
    "Matthew",
    "Mia",
    "Benjamin",
    "Olivia",
    "David",
    "Ava",
    "Louis",
    "Emma",
    "Joseph",
    "Zoe",
    "Andrew",
    "Clara",
    "Frederick",
    "Sarah",
    "Robert",
    "Eva",
    "Patrick",
    "Julia",
    "Michael",
    "Laura",
    "Paul",
    "Anna",
    "John",
    "Ellie",
    "Richard",
    "Bella",
]

SURNAMES = [
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Miller",
    "Davis",
    "Wilson",
    "Anderson",
    "Taylor",
    "Thomas",
    "Moore",
    "Martin",
    "Jackson",
    "Thompson",
    "White",
    "Harris",
    "Clark",
    "Lewis",
    "Robinson",
    "Walker",
    "Young",
    "Allen",
    "King",
    "Wright",
    "Scott",
    "Green",
    "Baker",
    "Adams",
    "Nelson",
    "Hill",
    "Evans",
    "Campbell",
    "Mitchell",
    "Roberts",
    "Carter",
    "Phillips",
    "Turner",
    "Parker",
    "Collins",
    "Edwards",
    "Stewart",
    "Morris",
    "Murphy",
    "Cook",
    "Rogers",
    "Morgan",
    "Reed",
    "Cooper",
    "Ward",
]


def run():
    parser = argparse.ArgumentParser(
        prog="name generator",
        description="Generate a list of names were some are prefixed with Prof.",
    )

    parser.add_argument(
        "-p",
        "--professors",
        default=10,
        type=int,
        help="number of names to have Prof. prefix",
    )
    parser.add_argument(
        "-n", "--names", default=1_000, type=int, help="number of names unique names."
    )
    parser.add_argument("--seed", help="Set the seed for the random generation.")

    args = parser.parse_args()

    names = product(FIRST_NAMES, SURNAMES)
    names = [" ".join(name) for name in names]

    if args.seed is not None:
        random.seed(args.seed)

    names = random.sample(names, k=args.names)
    profs = random.sample(names, k=args.professors)

    for prof in profs:
        i = names.index(prof)
        names[i] = f"Prof. {prof}"

    for name in names:
        print(name)


if __name__ == "__main__":
    run()
