#!/usr/bin/env python3
import sys


def main() -> None:
    """
    Main routine: collect archivist ID and status,
    then output via proper streams.
    """

    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n", file=sys.stdout)

    try:
        print(
              "\nInput Stream active. Enter archivist ID: ",
              end="",
              flush=True
        )
        archivist_id = input()
        print(
               "\nInput Stream active. Enter status report: ",
               end="",
               flush=True
        )
        status_report = input()
    except (EOFError, KeyboardInterrupt):

        print("\n[ALERT] Input interrupted.", file=sys.stderr)
        return

    print(f"[STANDARD] Archive status from {archivist_id}: {status_report}",
          file=sys.stdout)
    sys.stdout.flush()

    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)

    print("[STANDARD] Data transmission complete\n", file=sys.stdout)
    print("Three-channel communication test successful.", file=sys.stdout)


if __name__ == "__main__":
    main()
