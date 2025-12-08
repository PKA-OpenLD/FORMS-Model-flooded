from ultralytics import YOLO

def main():
    model = YOLO("yolo11l-seg.pt")

    model.train(
        data="datasets/data.yaml",
        epochs=50,
        imgsz=640,
        batch=-1,
        device=0,
        workers=0
    ) # <--- Đảm bảo có dấu đóng ngoặc đơn

if __name__ == "__main__": # <--- CẦN CÓ PHẦN NÀY
    main() # <--- CẦN CÓ PHẦN NÀY