from PIL import Image
import os

# 🔧 Change this to your folder path
folder_path = "rajgad_gut"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".png"):
        file_path = os.path.join(folder_path, filename)

        try:
            # Open image
            img = Image.open(file_path)

            # Rotate 90° counterclockwise
            rotated = img.rotate(90, expand=True)

            # Save (overwrite OR change name if needed)
            rotated.save(file_path)

            print(f"Rotated: {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("Done ✅")