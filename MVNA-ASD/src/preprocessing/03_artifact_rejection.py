"""Artifact rejection with ICA and ASR."""
from pathlib import Path

def reject_artifacts(raw_path: Path, output_path: Path) -> None:
    """Run ICA and ASR for ocular and motion artifacts."""
    # ICA rejection criteria: remove components with high EOG correlation,
    # clear frontal topography, or blink/saccade time courses.
    raise NotImplementedError("Implement artifact rejection.")

def main() -> None:
    print("TODO: implement ICA and ASR pipeline.")

if __name__ == "__main__":
    main()
