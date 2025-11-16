import argparse
import shutil
import os
from pathlib import Path


def parse_argv():
    parser = argparse.ArgumentParser(description="Sorting file by extension")
    parser.add_argument(
        "-s", "--src", type=Path, required=True, help="Source directory"
    )
    parser.add_argument(
        "-d",
        "--dest",
        type=Path,
        default=Path("dest"),
        help="Destination directory",
    )
    return parser.parse_args()


def copy(src: Path, dest: Path):
    try:
        for item in src.iterdir():
            if item.is_dir():
                copy(item, dest)
            else:
                file_extension = item.suffix.lower()[1:]
                folder = dest / file_extension
                folder.mkdir(parents=True, exist_ok=True)
                dest_file = folder / item.name
                print(f"Copying {item} to {dest_file}")
                shutil.copy2(item, dest_file)
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred when copy file {item.name}: {e}")


def processing():
    args = parse_argv()
    print("Run sort utility...")
    print(f"Source: {args.src}")
    print(f"Destination: {args.dest}")
    if not args.src.exists():
        print(f"Error: Source directory '{args.src}' does not exist")
        os._exit(1)
    if not args.src.is_dir():
        print(f"Error: Source directory '{args.src}' is not a directory")
        os._exit(1)
    try:
        args.dest.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Failed to create output directory: {e}")
        return
    copy(args.src, args.dest)
    print(f"Files successfully copied to {args.dest}")


if __name__ == "__main__":
    processing()
