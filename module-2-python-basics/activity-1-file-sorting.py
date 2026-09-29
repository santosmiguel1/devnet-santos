"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Santos, Miguel]
Date: [9/29/26]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
sorts files into folders based on their file extensions
folder so Python can find and organize the files
correctly


============================================
KEY VOCABULARY
============================================
- os module: A Python module used to interact with files
  and folders on the computer.
- shutil module: A Python module used to move, copy, and
  manage files.
- file path: The ending of a filename that
  identifies its file type, such as .jpg, .pdf, or .mp3.
- directory: The folder containing the files
  that the program will organize.

(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

source_folder = "module-2-python-basics/file-sorting-test"

images_folder = os.path.join(source_folder, "Images")
documents_folder = os.path.join(source_folder, "Documents")
music_folder = os.path.join(source_folder, "Music")

os.makedirs(images_folder, exist_ok=True)
os.makedirs(documents_folder, exist_ok=True)
os.makedirs(music_folder, exist_ok=True)

for file_name in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file_name)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file_name)[1].lower()

        if extension in [".jpg", ".jpeg", ".png", ".gif"]:
            shutil.move(file_path, images_folder)

        elif extension in [".pdf", ".txt", ".docx"]:
            shutil.move(file_path, documents_folder)

        elif extension in [".mp3", ".wav"]:
            shutil.move(file_path, music_folder)

print("Files have been sorted!")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I made was using the wrong path for the
file-sorting-test folder. I initially used
"file-sorting-test" as the source folder, but my test
folder was actually inside the module-2-python-basics
folder.

I fixed it by changing the path to
"module-2-python-basics/file-sorting-test". This taught
me that the file path needs to match the actual location
of the folder so Python can find and organize the files
correctly.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
