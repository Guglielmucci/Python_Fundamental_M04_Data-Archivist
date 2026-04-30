#!/usr/bin/env python3


def read_classified_data(file_path: str) -> str | None:
    """
    Read classified data from a file using a context manager.
    Returns the content as a string, or None if an error occurred.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as vault:
            print("Initiating secure vault access...")
            print("Vault connection established with failsafe protocols")
            content = vault.read()
        print("SECURE EXTRACTION:")
        return content
    except FileNotFoundError:
        print("\nERROR: Classified vault not found.")
        return None
    except Exception as e:
        print(f"\nERROR: Unexpected vault failure: {e}")
        return None


def write_secure_archive(file_path: str, data: str) -> bool:
    """
    Write new information to a secure archive using a context manager.
    Returns True if successful, False otherwise.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as vault:
            vault.write(data)
        print("\nSECURE PRESERVATION:")
        print("[CLASSIFIED] New security protocols archived")
        return True
    except Exception as e:
        print(f"\nERROR: Failed to write to secure archive: {e}")
        return False


def main() -> None:
    """Main routine: demonstrate secure vault operations."""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    classified = read_classified_data("classified_data.txt")
    if classified:
        for line in classified.strip().split('\n'):
            print(line)
        print()

    new_data = "[CLASSIFIED] New security protocols archived\n"
    write_secure_archive("secure_archive.txt", new_data)

    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
