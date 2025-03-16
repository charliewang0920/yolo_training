from ultralytics import YOLO
import torch
import multiprocessing  # Import the multiprocessing module

if __name__ == '__main__':
    # Check CUDA availability (optional, but good practice)
    print(torch.cuda.is_available())

    # MUST be called inside the if __name__ == '__main__' block
    multiprocessing.freeze_support()

    # Load the model *inside* the main block
    model = YOLO("yolo11n.pt")

    # Start training *inside* the main block
    model.train(data="data.yaml", epochs=100, imgsz=640)
