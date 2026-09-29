"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Santos, Miguel]
Date: [9/29/26]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]


============================================
KEY VOCABULARY
============================================
- os module:
- shutil module:
- file path:
- directory:
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
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
