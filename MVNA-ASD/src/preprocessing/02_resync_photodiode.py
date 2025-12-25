"""Resync trigger events using photodiode timing."""
from pathlib import Path

def resync_photodiode(raw_path: Path, output_path: Path) -> None:
    """Align TRIG events to PHOTO channel timestamps."""
    raise NotImplementedError("Implement photodiode resync.")

def main() -> None:
    print("TODO: implement photodiode resync.")

if __name__ == "__main__":
    main()
