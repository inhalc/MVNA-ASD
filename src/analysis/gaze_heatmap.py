"""Gaze heatmap rendering."""
from pathlib import Path

def render_heatmap(gaze_tsv: Path, image_path: Path, out_path: Path) -> None:
    """Overlay gaze samples on stimulus image and export heatmap."""
    raise NotImplementedError("Implement gaze heatmap.")

def main() -> None:
    print("TODO: implement gaze heatmap.")

if __name__ == "__main__":
    main()
