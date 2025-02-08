from .img_plotter import ImagePlotter

import os
import numpy as np
import torch
from torchvision import models, transforms
from concurrent.futures import ProcessPoolExecutor
from sklearn.neighbors import NearestNeighbors
import multiprocessing
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
multiprocessing.set_start_method("spawn", force=True)

class ImageSimilarityChecker:
    def __init__(self, image_directory="png", batch_size=32):

        Image.MAX_IMAGE_PIXELS = None

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(self.device)

        self.model = models.resnet50(weights="ResNet50_Weights.DEFAULT")
        self.model.to(self.device)
        self.model.eval()

        self.transform = transforms.Compose(
            [
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                ),
            ]
        )

        self.image_directory = image_directory
        self.batch_size = batch_size
        self.similarities = None
        self.indices = None
        self.image_paths = []
        self.img_plotter = ImagePlotter()

        if not "output" in os.listdir():
            os.mkdir("output")

    def _extract_features_batch(self, image_paths_batch):
        """
        Extract features from a batch of images by passing them through the pre-trained ResNet model.
        """
        images = []
        for image_path in image_paths_batch:
            image = Image.open(image_path).convert("RGB")
            max_size = (10000, 10000)
            image.thumbnail(max_size)
            image = self.transform(image)
            images.append(image)

        images = torch.stack(images).to(self.device)

        with torch.no_grad():
            features = self.model(images).cpu().numpy()
        return features

    def _compute_similarity(self):
        """
        Compute the cosine similarity between all images using NearestNeighbors from sklearn.
        """
        self.image_paths = [
            os.path.join(self.image_directory, fname)
            for fname in os.listdir(self.image_directory)
            if fname.endswith(".png")
        ]

        all_features = []
        with ProcessPoolExecutor() as executor:

            batches = [
                self.image_paths[i : i + self.batch_size]
                for i in range(0, len(self.image_paths), self.batch_size)
            ]

            for batch in batches:
                features_batch = executor.submit(self._extract_features_batch, batch)
                all_features.append(features_batch.result())

        if not all_features : return

        all_features = np.concatenate(all_features, axis=0)

        nn = NearestNeighbors(n_neighbors=5, metric="cosine", n_jobs=-1)
        nn.fit(all_features)

        distances, indices = nn.kneighbors(all_features)

        similarities = 1 - distances
        self.similarities = similarities
        self.indices = indices
        return similarities, indices, self.image_paths

    def get_similar_images(self):
        """
        Identify and return a set of image paths that are highly similar (similarity > 0.90).
        """
        if self.similarities is None or self.indices is None:
            self._compute_similarity()

        img_dict = {}
        img = set()

        for i, (sim, idx) in enumerate(zip(self.similarities, self.indices)):
            for j, index in enumerate(idx[1:]):
                rounded_similarity = round(sim[j + 1], 2)
                if rounded_similarity < 0.95:
                    break

                primary_img = os.path.basename(self.image_paths[i])
                secondary_image = os.path.basename(self.image_paths[index])

                if primary_img not in img_dict:
                    img.add(primary_img)
                    img_dict[primary_img] = True

                if secondary_image not in img_dict:
                    img.add(secondary_image)
                    img_dict[secondary_image] = True

        self.img_plotter.save_images_grid(list(img))

        """
        Identify and return a set of image paths that are highly similar (similarity > 0.90).
        """
        if self.similarities is None or self.indices is None:
            self._compute_similarity()

        img_dict = {}

        img = set()
        for i, (sim, idx) in enumerate(zip(self.similarities, self.indices)):

            for j, index in enumerate(idx[1:]):
                rounded_similarity = round(sim[j + 1], 2)
                if rounded_similarity < 0.95:
                    break

                primary_img = os.path.basename(self.image_paths[i])
                secondary_image = os.path.basename(self.image_paths[index])


                if primary_img not in img_dict : 
                    img.add(primary_img)
                    img_dict[primary_img] = True

                if secondary_image not in img_dict : 
                    img.add(secondary_image)
                    img_dict[secondary_image] = True

        self.img_plotter.save_images_grid(list(img))


if __name__ == "__main__":
    similarity_checker = ImageSimilarityChecker(batch_size=20)
    similar_images = similarity_checker.get_similar_images()
