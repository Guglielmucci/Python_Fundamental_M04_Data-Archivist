#!/usr/bin/env python3


def recover_fragment(file_path: str) -> str | None:
    """
    Apre e legge il file, restituisce il contenuto o None se non trovato.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as vault:
            print("Accessing Storage Vault:", file_path)
            print("Connection established...")
            return vault.read()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return None


def display_recovery_result(fragment: str | None) -> None:
    """
    Visualizza il risultato del recupero.
    """
    if fragment is not None:
        print()
        print("RECOVERED DATA:")
        print(fragment)
        print("Data recovery complete. Storage unit disconnected.")


def main() -> None:
    """Punto di ingresso principale."""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    fragment = recover_fragment("ancient_fragment.txt")
    display_recovery_result(fragment)


if __name__ == "__main__":
    main()
