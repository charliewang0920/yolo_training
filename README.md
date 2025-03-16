# yolo_training
## 1. 準備訓練資料
https://universe.roboflow.com/fmdv/fsoco-kxq3s

<img width="1280" alt="image" src="https://github.com/user-attachments/assets/03edcf78-54ed-424e-a2ff-5942c535d997" />

<img width="1280" alt="image" src="https://github.com/user-attachments/assets/796ad446-bbe1-44d4-960f-a45acb0a1075" />
選擇yolov11

## 2. 創建train.py
將載下來的資料夾解壓縮，在資料夾裡創一個train.py檔案。檔案內容如下:
![image](https://github.com/user-attachments/assets/6acf5cb8-2aae-494b-b57c-a03c5ac628d9)
![image](https://github.com/user-attachments/assets/8f956af4-166e-45f3-a296-bc97b4a2fbf9)


## 3. 開始訓練
在該資料夾中打開cmd，打上python train.py，即可開始訓練

## 4. 訓練完後，找到best.pt的檔案，把它傳送到ubuntu
訓練完後，會出現一個名字為runs的資料夾。在 ./runs/detect/trainXX/weights 裡會有一個best.pt和一個last.pt。把best.pt想辦法傳送到ubuntu裡。

## 5. 在ubuntu安裝ultralytics ros
https://github.com/Alpaca-zip/ultralytics_ros
照著上面的步驟安裝

## 6. 在ultralytics_ros的資料夾裡找到models資料夾，把訓練好的.pt檔放進去
ultralytics_ros 的package裡面的長相
![image](https://github.com/user-attachments/assets/6bc102d4-d485-4c57-b9dc-596488d85bc8)

## 7. 開始執行
先用rosbag執行.bag檔，再使用指令：roslaunch ultralytics_ros tracker.launch debug:=true 執行ultralytics_ros。框好角錐的畫面會publish到/yolo_image裡面。
![image](https://github.com/user-attachments/assets/263532b7-5c36-4f72-bfb9-b70f4634d71f)
