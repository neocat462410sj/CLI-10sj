#!/usr/bin/env python3
"""
Directory statistics CLI tool.
"""

import argparse
import sys
from pathlib import Path

def dir_stats(path: Path):
    total_size = 0
    file_count = 0
    max_file = None
    max_size = 0
    for p in path.rglob('*'):
        if p.is_file():
            file_count += 1
            size = p.stat().st_size
            total_size += size
            if size > max_size:
                max_size = size
                max_file = p
    return file_count, total_size, max_file, max_size

def main():
    parser = argparse.ArgumentParser(description="Show directory statistics")
    parser.add_argument('directory', nargs='?', default='.', help='Target directory')
    args = parser.parse_args()
    dir_path = Path(args.directory).resolve()
    if not dir_path.is_dir():
        print(f"Error: {dir_path} is not a directory", file=sys.stderr)
        sys.exit(1)
    count, size, max_file, max_size = dir_stats(dir_path)
    print(f"Directory: {dir_path}")
    print(f"Files: {count}")
    print(f"Total size: {size} bytes")
    if max_file:
        print(f"Largest file: {max_file} ({max_size} bytes)")

if __name__ == "__main__":
    main()