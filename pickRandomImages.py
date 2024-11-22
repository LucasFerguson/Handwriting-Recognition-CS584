from genericpath import isdir
import os
import random
import shutil
from pathlib import Path

source_dir = "Datasets/MergedMNIST/"
destination_dir = "Presentation_Data/set2"
n = 40

source_path = Path(source_dir)
dest_path = Path(destination_dir)

dest_path.mkdir(parents=True, exist_ok=True)

for subfolder in source_path.glob('dataset/*/'):

	if subfolder.is_dir():

		# Get all files
		images = list(subfolder.glob('*.png'))

		# Select n files
		selected_images = random.sample(images, min(n, len(images)))

		# Create corresponding subfolder in the destination directory
		relative_path = subfolder.relative_to(source_path)
		dest_subfolder = dest_path / relative_path
		dest_subfolder.mkdir(parents=True, exist_ok=True)
		
		# Copy selected images to the destination folder
		for img in selected_images:
			shutil.copy(img, dest_subfolder)
			# print(f"Copied {img} to {dest_subfolder}")