import matplotlib.pyplot as plt
import os
from datetime import datetime
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

class ImagePlotter:
    def load_image(self, image_path):
        img = Image.open(f"png/{image_path}")
        img = np.array(img)
        return img

    def save_images_grid(self, image_paths):

        grid_size = 16
        images_per_row = 4
        images_per_col = 4

        total_images = len(image_paths)
        grids_needed = (total_images + grid_size - 1) // grid_size

        for grid_index in range(grids_needed):

            fig, axes = plt.subplots(
                images_per_row, images_per_col, figsize=(15, 15), dpi=400
            )

            axes = axes.flatten()

            start_idx = grid_index * grid_size
            end_idx = min((grid_index + 1) * grid_size, total_images)
            images_to_plot = image_paths[start_idx:end_idx]

            for i, img_path in enumerate(images_to_plot):
                img = self.load_image(img_path)
                ax = axes[i]
                ax.set_title(img_path)
                ax.imshow(img)
                ax.axis("off")

            for j in range(len(images_to_plot), grid_size):
                axes[j].axis("off")

            timestamp = datetime.now().strftime("%H.%M-%d.%m.%y")
            filename = f"output/{timestamp}_{grid_index + 1}.png"

            plt.tight_layout()
            plt.savefig(filename)
            plt.close()

        print(f"Saved {grids_needed} grid(s) of images.")


if __name__ == "__main__":
    image_paths_set = ["png/388982.png"]
