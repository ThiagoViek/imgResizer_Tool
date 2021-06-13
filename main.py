import argparse
from src.resizer import Resizer

def main() -> None:
    # Inputs
    parser = argparse.ArgumentParser(description="-- Image Resizer --")
    parser.add_argument("--resize_ratio",
                        help = "Ratio by which the image is resize",
                        type = int,
                        default = 3)
    args = parser.parse_args()
    ratio = args.resize_ratio

    # Resizing Images
    resizer = Resizer(ratio)
    resizer.resize_images()

if __name__ == "__main__":
    main()