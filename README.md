# Cristiano Ronaldo Detector

This project aims to detect Cristiano Ronaldo in images using a custom-trained YOLOv8 model. It includes tools for automated data collection, model training, and inference.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Data Collection](#data-collection)
- [Model Training](#model-training)
- [Inference](#inference)
- [Google Colab](#google-colab)
- [License](#license)

## Features
- Automated image data collection using keywords.
- Custom YOLOv8 model training for Cristiano Ronaldo detection.
- Inference on new images to identify Cristiano Ronaldo.

## Project Structure

```
cristiano-ronaldo-detector/
├── AutoCrawler/                     # Scripts for automated data collection
│   ├── collect_links.py             # Collects image links
│   ├── keywords.txt                 # Keywords for image search
│   ├── main.py                      # Main script for crawling and downloading images
│   └── rename.py                    # Renames downloaded images
├── data.yaml                        # Dataset configuration for YOLOv8
├── download/                        # Downloaded raw images
│   ├── not_ronaldo/                 # Images not containing Cristiano Ronaldo
│   └── ronaldo/                     # Images containing Cristiano Ronaldo
├── model/                           # Model training scripts
│   └── train_yolov8.py              # Script to train YOLOv8 model
├── requirements.txt                 # Python dependencies for the main project
├── run/                             # Generated output from model inference (e.g., detected images)
├── train_test_data/                 # Processed data for training, validation, and testing
│   ├── fill_txt.py                  # Script to fill annotation text files
│   ├── test_data/                   # Images for testing the model
│   ├── train/                       # Images and labels for training
│   └── val_data/                    # Images and labels for validation
└── LICENSE                          # MIT License file
```

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/cristiano-ronaldo-detector.git
    cd cristiano-ronaldo-detector
    ```

2.  **Install dependencies:**
    Ensure you have Python 3.8+ installed. It's recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```
    For the `AutoCrawler`, navigate to its directory and install its specific dependencies:
    ```bash
    cd AutoCrawler
    pip install -r requirements.txt
    cd ..
    ```

## Data Collection

This project utilizes a modified version of the AutoCrawler developed by YoongiKim. For the original repository, please refer to [YoongiKim/AutoCrawler](https://github.com/YoongiKim/AutoCrawler).

The `AutoCrawler/` directory contains scripts to automate the collection of image data.

1.  **Define Keywords:**
    Edit `AutoCrawler/keywords.txt` to specify the search terms for images you want to download. Each line should contain a keyword. For example:
    ```
    Cristiano Ronaldo
    Football player
    ```

2.  **Run the Crawler:**
    Use `AutoCrawler/main.py` to collect and download images.
    ```bash
    python AutoCrawler/main.py
    ```
    This will save images into `download/ronaldo/` and `download/not_ronaldo/` based on your keywords.

3.  **Rename Images (Optional but Recommended):**
    After downloading, you can use `AutoCrawler/rename.py` to standardize the filenames.
    ```bash
    python AutoCrawler/rename.py
    ```

## Model Training

The `model/train_yolov8.py` script is used to train the YOLOv8 model.

1.  **Prepare your dataset:**
    Ensure your dataset is organized according to the structure defined in `data.yaml`. The `train_test_data/` directory should contain your images and corresponding YOLO annotation files. You might need to use `train_test_data/fill_txt.py` to generate the `.txt` annotation files if you have bounding box data in another format.

2.  **Configure `data.yaml`:**
    The `data.yaml` file specifies the paths to your training, validation, and test datasets, as well as the class names.
    ```yaml
    train: train_test_data/train/images
    val: train_test_data/val_data/images
    test: train_test_data/test_data

    nc: 1
    names: ['ronaldo']
    ```
    **Note:** The `model/train_yolov8.py` script currently uses a hardcoded path `../My First Project.v1i.yolov8/data.yaml`. You might need to adjust `data_yaml_path` in `model/train_yolov8.py` to `../data.yaml` if your `data.yaml` is in the project root.

3.  **Train the model:**
    Run the training script from the `model/` directory:
    ```bash
    python model/train_yolov8.py
    ```
    You can adjust parameters like `epochs` and `imgsz` within `train_yolov8.py` as needed. The trained model will be saved as `my_finetuned_yolov8.pt`.

## Inference

After training, you can use the trained model to perform inference on new images. The `model/train_yolov8.py` script includes an inference step that saves results with bounding boxes.

The `run/` directory is automatically generated when the model in `model/` is run for inference (e.g., using `model.predict`). This directory will contain images with detected bounding boxes.

## Google Colab

This project was developed and can be run on Google Colab for easier access to GPU resources. You can find the Colab notebook here:

[https://colab.research.google.com/drive/1vNgR8z_CMPnw12d05ud_B7_-hgfnx7qz#scrollTo=jExrTij1aJIN](https://colab.research.google.com/drive/1vNgR8z_CMPnw12d05ud_B7_-hgfnx7qz#scrollTo=jExrTij1aJIN)

## Limitations and Future Improvements

The current model's performance is limited due to the small scale of the training dataset, which was primarily for demonstration purposes. To improve the accuracy of Cristiano Ronaldo detection, it is highly recommended to augment the training set with more diverse images. We welcome and are happy to merge pull requests that contribute additional training data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 