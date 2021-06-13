from src.resizer import Resizer

def main() -> None:
    resizer = Resizer(3)
    resizer.resize_images()

if __name__ == "__main__":
    main()