import os
import shutil
from pathlib import Path

# Path to your dataset root
DATA_DIR = Path("data/brand")

# Includes all possible folder naming conventions from your setup
SPLITS = ["train", "val", "test"]

# Your exact 15 classes ordered exactly as specified in your data.yaml
CLASSES = ['mechanical', 'fashion', 'sports', 'food', 'bank', 'phone', 'electronics', 'travel', 'furniture', 'health', 'beauty', 'home' , 'pet','toy']

for split in SPLITS:
    split_dir = DATA_DIR / split
    images_dir = split_dir / "images"
    labels_dir = split_dir / "labels"
    
    # Check if this specific split directory exists with the required folders
    if not images_dir.exists() or not labels_dir.exists():
        continue
        
    print(f"Processing '{split}' split...")
    moved_count = 0
    
    # Process each label text file
    for label_file in labels_dir.glob("*.txt"):
        image_name = label_file.stem
        
        # Look for the matching image file across common extensions
        img_path = None
        for ext in [".png", ".jpg", ".jpeg", ".PNG", ".JPG", ".JPEG"]:
            possible_path = images_dir / f"{image_name}{ext}"
            if possible_path.exists():
                img_path = possible_path
                break
                
        if not img_path:
            continue
            
        # Parse the class ID out of the YOLO annotation file
        try:
            with open(label_file, "r") as f:
                line = f.readline().strip()
                if not line:
                    continue
                # YOLO format: 'class_id x_center y_center width height'
                class_id = int(line.split()[0])
        except Exception:
            continue
            
        # If the class ID is valid, map it to the class folder and move the image
        if class_id < len(CLASSES):
            class_name = CLASSES[class_id]
            target_folder = split_dir / class_name
            target_folder.mkdir(exist_ok=True)
            
            try:
                shutil.move(str(img_path), str(target_folder / img_path.name))
                moved_count += 1
            except Exception as e:
                print(f"Error moving {img_path.name}: {e}")

    print(f"Moved {moved_count} images into class folders for '{split}'.")

    # Clean up empty original YOLO folders to keep your workspace tidy
    try:
        if any(split_dir.glob(f"*/")): # Ensure we successfully created folders before deleting originals
            shutil.rmtree(str(images_dir))
            shutil.rmtree(str(labels_dir))
            print(f"Cleaned up legacy YOLO folders for '{split}'.")
    except Exception as e:
        print(f"Could not remove old folders for '{split}': {e}")

print("\nDataset conversion complete!")
