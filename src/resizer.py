import os
import cv2
import numpy as np

class Resizer:
    SRC_DIR = "../../src_images/"
    DST_DIR = "../../dst_images/"

    def __init__(self, resize_ratio : int = 3) -> None:
        self.src_path = os.path.join(os.getcwd(), self.SRC_DIR)
        self.dst_path = os.path.join(os.getcwd(), self.DST_DIR)

        self.ratio = resize_ratio

        self.img_file_list = os.listdir(self.src_path)       

    def resize_images(self) -> None:
        """
        Resizes all images in src_dir by the given ratio
        and places the new images in dst_dir.
        input:
        -
        output:
        -
        """
        print("[INFO] Initializing...\n")

        count = 1
        for f in self.img_file_list:
            img_path = self.src_path + f
            img = cv2.imread(img_path)

            orig_dim = img.shape[:2]
            new_dim = tuple(map(lambda x: x // self.ratio, orig_dim))

            img_resize = cv2.resize(img, new_dim)
            self._write_image(img_resize, f)

            print(f"[INFO] Progress: { 100 * count / self.dataset_size :.0f}%")
            count+=1

        print("\n[INFO] Process Finished")

    @property
    def dataset_size(self) -> int:
        return len(self.img_file_list)
    
    @classmethod
    def _write_image(cls, img : np.array, filename : str) -> None:
        new_image_path = cls.DST_DIR + filename
        cv2.imwrite(new_image_path, img)

