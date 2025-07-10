import os
import shutil

def split_data(source_dir, train_target_dir, test_target_dir, train_count):
    os.makedirs(train_target_dir, exist_ok=True)
    os.makedirs(test_target_dir, exist_ok=True)

    files = sorted([f for f in os.listdir(source_dir) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))])

    # Copy for training set
    for i in range(min(train_count, len(files))):
        shutil.copy(os.path.join(source_dir, files[i]), os.path.join(train_target_dir, files[i]))
    print(f"Copied {min(train_count, len(files))} images to {train_target_dir}")

    # Copy for testing set
    for i in range(train_count, len(files)):
        shutil.copy(os.path.join(source_dir, files[i]), os.path.join(test_target_dir, files[i]))
    print(f"Copied {max(0, len(files) - train_count)} images to {test_target_dir}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    download_dir = os.path.join(script_dir, "..", "download")
    train_data_dir = os.path.join(script_dir, "train_data")
    test_data_dir = os.path.join(script_dir, "test_data")

    # Split Ronaldo images
    ronaldo_source_dir = os.path.join(download_dir, "ronaldo")
    ronaldo_train_target_dir = os.path.join(train_data_dir, "ronaldo")
    ronaldo_test_target_dir = os.path.join(test_data_dir, "ronaldo")
    print("\nSplitting Ronaldo images...")
    split_data(ronaldo_source_dir, ronaldo_train_target_dir, ronaldo_test_target_dir, 150)

    # Split Not_Ronaldo images
    not_ronaldo_source_dir = os.path.join(download_dir, "not_ronaldo")
    not_ronaldo_train_target_dir = os.path.join(train_data_dir, "not_ronaldo")
    not_ronaldo_test_target_dir = os.path.join(test_data_dir, "not_ronaldo")
    print("\nSplitting Not_Ronaldo images...")
    split_data(not_ronaldo_source_dir, not_ronaldo_train_target_dir, not_ronaldo_test_target_dir, 75)

    print("\nData splitting complete!")
