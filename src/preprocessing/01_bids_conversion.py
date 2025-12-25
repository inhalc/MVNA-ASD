"""Convert raw Neuroscan data into BIDS structure."""
from pathlib import Path

def convert_to_bids(input_dir: Path, output_dir: Path) -> None:
    """Convert raw .cnt or .avg files into BIDS layout."""
    raise NotImplementedError("Implement BIDS conversion.")

def main() -> None:
    print("TODO: implement BIDS conversion pipeline.")

if __name__ == "__main__":
    main()
