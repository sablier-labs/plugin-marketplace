#!/usr/bin/env python3
"""
Extract constructor arguments from Foundry broadcast initCode.

Factory-created contracts (CREATE2) embed constructor args after the bytecode.
This script extracts them by finding the Solidity metadata hash ending.

Usage:
    python extract_constructor_args.py <initcode_file_or_hex> [solc_version]
    python extract_constructor_args.py /tmp/initcode.txt 0.8.29
    python extract_constructor_args.py 0x608060405234801... 0.8.28

Metadata pattern: 64736f6c6343 + major + minor + patch + 0033
    Example for 0.8.29: 64736f6c6343 + 00 + 08 + 1d + 0033
"""

import sys
import os


def version_to_pattern(version: str) -> str:
    """Convert solc version string to metadata pattern."""
    parts = version.split(".")
    if len(parts) != 3:
        raise ValueError(f"Invalid version format: {version}")

    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
    return f"64736f6c634300{minor:02x}{patch:02x}0033"


def extract_constructor_args(data: str, pattern: str) -> str | None:
    """Extract constructor args from initCode hex string."""
    data = data.strip().lower()
    if data.startswith("0x"):
        data = data[2:]

    idx = data.find(pattern.lower())
    if idx == -1:
        return None

    args_start = idx + len(pattern)
    if args_start >= len(data):
        return None

    return f"0x{data[args_start:]}"


def main():
    if len(sys.argv) < 3:
        print("Usage: extract_constructor_args.py <initcode_file_or_hex> <solc_version>")
        print("\nExamples:")
        print("  extract_constructor_args.py /tmp/initcode.txt 0.8.29")
        print("  extract_constructor_args.py 0x608060405234801... 0.8.28")
        print("\nGet solc version from foundry.toml: grep solc foundry.toml")
        sys.exit(1)

    input_arg = sys.argv[1]
    version = sys.argv[2]

    # Load data
    if os.path.isfile(input_arg):
        with open(input_arg, "r") as f:
            data = f.read()
    else:
        data = input_arg

    # Generate pattern and extract
    pattern = version_to_pattern(version)
    args = extract_constructor_args(data, pattern)

    if args:
        print(args)
    else:
        print(f"Pattern {pattern} not found in initCode", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
