from pathlib import Path
import os
import argparse


def read_file():
    output = []
    names = Path("names.txt")
    if not names.is_file():
        print("Could not find names.txt")
        exit(1)
    with open("names.txt", "r") as f:
        for line in f.readlines():
            if line.startswith("Prof."):
                output.append(line.strip("\n"))
    return output


def read_index_file(index):
    output = []
    with open(index, "r") as f:
        for line in f:
            if "href=" in line:
                split = line.split("href=")
                split = split[1].split(">")
                filename = split[0]
                filename = filename.strip('"')
                filename = filename.strip("'")
                filename = filename.strip("./")

                split = split[1].split("<")
                name = split[0]
                filename = Path("html", filename)
                output.append({"name": name, "filename": filename})
    return output


def challenge_files_validate(profs):
    results = []
    for prof in profs:
        file_exists = False
        content_exists = False
        if prof["filename"].is_file():
            file_exists = True
            with open(prof["filename"], "r") as f:
                data = f.read()
                if prof["name"] in data:
                    content_exists = True
        results.append((prof, file_exists, content_exists))
    return results


def challenge_passed(results, challenge="Challenge 1"):
    passed = True
    for result in results:
        if not result[1] and not result[2]:
            passed = False

    if passed:
        print(f"{challenge} passed")
    else:
        print(f"{challenge} failed")
        for result in results:
            if not result[1]:
                print(f"Missing file for: {result[0]}")
            if not result[2]:
                print(f"Missing content for: {result[0]}")
    return passed


def run():

    parser = argparse.ArgumentParser(
        prog="Challenge Validator",
        description="Validate the results for the challenge",
    )
    parser.add_argument(
        "--part-two",
        action="store_true",
        help="Run the validator on the second part of the challenge.",
    )
    args = parser.parse_args()

    profs_read = read_file()
    profs = []
    for prof in profs_read:
        split = prof.split()
        filename = Path("html", f'{"".join(split[1:])}.html')
        profs.append({"name": prof, "filename": filename})

    # TODO: There should be a check that ensures the correct number of files were created.
    # This should take into account that the challenge 2 index file may or may not be there.

    _, _, files = next(os.walk("html"))
    file_count = len(files)
    target = len(profs)
    if args.part_two:
        target = len(profs) + 1

    if file_count != target:
        print(
            f"Challenge kinda failed, number of files created ({file_count}) does not match what was expected ({target})"
        )

    if file_count == target + 1 and not args.part_two:
        print(
            'Number of files match if your checking the second challenge, run command with "--part-two"'
        )

    results = challenge_files_validate(profs)

    passed = challenge_passed(results)

    if not args.part_two:
        exit()

    if not passed and args.part_two:
        print("Challenge 1 failed so Challenge 2 also is failed")

    index = Path("html", "index.html")
    if not index.is_file():
        print("index.hmtl does not exist")
        print("Challenge 2 failed")
        exit(1)

    site_links = read_index_file(index)

    if len(site_links) != len(profs):
        print("site links not the same length as expected links")
        exit(1)

    results = challenge_files_validate(site_links)
    passed = challenge_passed(results, "Challenge 2")
    if not passed:
        exit(1)


if __name__ == "__main__":
    run()
