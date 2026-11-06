
import os
import shutil

source = "Source"
destination = "JPG Files"

os.makedirs(destination, exist_ok=True)

count = 0

for file in os.listdir(source):
    if file.lower().endswith(".jpg"):
        shutil.move(
            os.path.join(source, file),
            os.path.join(destination, file)
        )
        count += 1

print("File Organization Completed!")
print("Total JPG files moved:", count)
