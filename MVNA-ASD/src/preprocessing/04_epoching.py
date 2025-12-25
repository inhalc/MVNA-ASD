"""Epoch continuous data into trials."""
from pathlib import Path

def epoch_trials(raw_path: Path, output_path: Path) -> None:
    """Create epochs from -200 ms to 800 ms and save to disk."""
    raise NotImplementedError("Implement epoching.")

def main() -> None:
    print("TODO: implement epoching.")

if __name__ == "__main__":
    main()
