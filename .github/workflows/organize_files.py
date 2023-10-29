import os
import shutil

labels = os.getenv("INPUT_PULL_REQUEST_LABELS").split(",")
file_extensions = [".rst"]  # Define the file extensions to organize

for label in labels:
    # Create a folder based on the label name
    if not os.path.exists(label):
        os.makedirs(label)

    # Organize files with specific extensions
    for ext in file_extensions:
        for file in os.listdir():
            if file.endswith(ext):
                shutil.move(file, os.path.join(label, file))
