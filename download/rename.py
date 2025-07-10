
import os

def rename_images(directory, prefix):
    for index, filename in enumerate(os.listdir(directory)):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
            new_name = f"{prefix}_{index:04d}.jpg"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f"Renamed {filename} to {new_name}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    ronaldo_dir = os.path.join(script_dir, "ronaldo")
    not_ronaldo_dir = os.path.join(script_dir, "not_ronaldo")

    print("Renaming images in ronaldo/...")
    rename_images(ronaldo_dir, "ronaldo")

    print("Renaming images in not_ronaldo/...")
    rename_images(not_ronaldo_dir, "not_ronaldo")

    print("Renaming complete!")

