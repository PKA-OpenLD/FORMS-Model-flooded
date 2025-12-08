import cv2
import numpy as np

image_path = "D:\\Du_an\\pmmnm-project\\datasets\\images\\train\\0000000035.jpg"
label_path = "D:\\Du_an\\pmmnm-project\\datasets\\labels\\train\\0000000035.txt"

img = cv2.imread(image_path)
h, w = img.shape[:2]


with open(label_path, "r") as f:
    line = f.readline().strip().split()

cls = int(line[0])
coords = list(map(float, line[1:]))


points = []
for i in range(0, len(coords), 2):
    x = int(coords[i] * w)
    y = int(coords[i+1] * h)
    points.append([x, y])

points = np.array(points, dtype=np.int32)

# vẽ polygon
overlay = img.copy()
cv2.polylines(overlay, [points], isClosed=True, color=(0,255,0), thickness=2)

# tô màu vùng polygon (alpha blend)
mask = np.zeros_like(img)
cv2.fillPoly(mask, [points], (0,255,0))
result = cv2.addWeighted(img, 0.7, mask, 0.3, 0)

cv2.imwrite("visualized.png", result)
print("Saved to visualized.png")
