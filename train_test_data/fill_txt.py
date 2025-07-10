
import os

def create_missing_label_files(base_dir):
    for split in ["train", "val_data"]:
        images_dir = os.path.join(base_dir, split, "images")
        labels_dir = os.path.join(base_dir, split, "labels")

        if not os.path.exists(images_dir):
            print(f"Images directory not found: {images_dir}")
            continue

        if not os.path.exists(labels_dir):
            os.makedirs(labels_dir) # Create labels directory if it doesn't exist
            print(f"Created labels directory: {labels_dir}")

        for image_filename in os.listdir(images_dir):
            if image_filename.lower().endswith((".jpg", ".jpeg", ".png")):
                image_name_without_ext = os.path.splitext(image_filename)[0]
                label_filename = f"{image_name_without_ext}.txt"
                label_filepath = os.path.join(labels_dir, label_filename)

                if not os.path.exists(label_filepath):
                    with open(label_filepath, "w") as f:
                        pass  # Create an empty file
                    print(f"Created missing label file: {label_filepath}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    create_missing_label_files(script_dir)
    print("Missing label file check complete.")

