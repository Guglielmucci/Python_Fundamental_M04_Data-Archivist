#!/usr/bin/env python3


def handle_crisis(file_path: str) -> None:
    """Attempt to read a file and handle various crisis scenarios."""
    try:
        with open(file_path, 'r', encoding='utf-8') as archive:
            content = archive.read()
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_path}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_path}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"CRISIS ALERT: Attempting access to '{file_path}'...")
        print(f"RESPONSE: Unexpected system anomaly: {type(e).__name__}")
        print("STATUS: Crisis handled, system stable")
    else:
        print(f"ROUTINE ACCESS: Attempting access to '{file_path}'...")
        print(f"SUCCESS: Archive recovered - {content.strip()}")
        print("STATUS: Normal operations resumed")
    print()


def main() -> None:
    """Main routine: test various crisis scenarios."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    test_files = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]

    for fname in test_files:
        handle_crisis(fname)

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
