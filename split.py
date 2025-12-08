import os
import random
import shutil


IMAGE_DIR = "D:\\Du_an\\pmmnm-project\\datasets\\images"
LABEL_DIR = "D:\\Du_an\\pmmnm-project\\datasets\\labels"

#%split
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1


for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(IMAGE_DIR, split), exist_ok=True)
    os.makedirs(os.path.join(LABEL_DIR, split), exist_ok=True)

images = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

# Shuffle
random.shuffle(images)

# Tính số lượng
total = len(images)
train_end = int(total * train_ratio)
val_end   = train_end + int(total * val_ratio)

train_files = images[:train_end]
val_files   = images[train_end:val_end]
test_files  = images[val_end:]

def move_files(file_list, split):
    for img_name in file_list:
        label_name = os.path.splitext(img_name)[0] + ".txt"

        # copy ảnh
        shutil.copy(
            os.path.join(IMAGE_DIR, img_name),
            os.path.join(IMAGE_DIR, split, img_name)
        )

        # copy label 
        if os.path.exists(os.path.join(LABEL_DIR, label_name)):
            shutil.copy(
                os.path.join(LABEL_DIR, label_name),
                os.path.join(LABEL_DIR, split, label_name)
            )

move_files(train_files, "train")
move_files(val_files, "val")
move_files(test_files, "test")

print("✔ DONE! Chia dữ liệu train/val/test hoàn tất.")
print(f"Train: {len(train_files)}, Val: {len(val_files)}, Test: {len(test_files)}")
