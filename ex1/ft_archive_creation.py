#!/usr/bin/env python3
import sys


def create_archive(file_path: str, entries: list[str]) -> bool:
    """
    Write numbered entries into the archive file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as vault:
            print(f"Initializing new storage unit: {file_path}")
            print("Storage unit created successfully...")
            print()
            print("Inscribing preservation data...")

            i = 1
            for entry in entries:
                vault.write(f"[ENTRY {i:03d}] {entry}\n")
                print(f"[ENTRY {i:03d}] {entry}")
                i += 1

        return True
    except OSError as e:
        print(f"ERROR: Unable to create storage unit - {e}")
        return False


def main() -> None:
    """Main routine."""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    if len(sys.argv) > 1:
        archive_name = sys.argv[1]
    else:
        print("WARNING: No archive name provided, using 'new_discovery.txt'")
        archive_name = "new_discovery.txt"

    archive_entries = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee"
    ]

    if create_archive(archive_name, archive_entries):
        print()
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{archive_name}' ready for long-term preservation.")


if __name__ == "__main__":
    main()
