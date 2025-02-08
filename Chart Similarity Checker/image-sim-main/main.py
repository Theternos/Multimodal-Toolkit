import pandas as pd
from file.check_image_simmilarities import ImageSimilarityChecker


if __name__ == "__main__":
    similarity_checker = ImageSimilarityChecker(batch_size=20)
    similar_images = similarity_checker.get_similar_images()
