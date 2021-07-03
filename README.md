
# Mask Detection

Another mask detection with YOLOv5


## Results

![](https://camo.githubusercontent.com/8bf4aeb859c38c19d80829aa83c41b26c3c145d3546eb508edfb70c4eaafe7e2/68747470733a2f2f692e6962622e636f2f366d314a6276302f696d67312e6a7067)
![](https://camo.githubusercontent.com/162ab9ea2b02182591707f6c53d792436eb4844c55c0ed9ac4de95045c88113b/68747470733a2f2f692e6962622e636f2f66396d784b734a2f696d67322e6a7067)
![](https://camo.githubusercontent.com/ce56ddc44e73396a267e911ccc7c4887b9530b9b7605428a4fb4392d532b4e92/68747470733a2f2f692e6962622e636f2f434b336252636b2f696d67332e6a7067)

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/z430/yolov5-mask-detection.git
```

Go to the project directory

```bash
  cd yolov5-mask-detection
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Download checkpoint from [here](https://github.com/z430/yolov5-mask-detection/releases) and save it to `runs/detect`

Start the server

```bash
python detect.py --source 0  # webcam
                        file.jpg  # image 
                        file.mp4  # video
                        path/  # directory
                        path/*.jpg  # glob
                        rtsp://170.93.143.139/rtplive/470011e600ef003a004ee33696235daa  # rtsp stream
                        rtmp://192.168.1.105/live/test  # rtmp stream
                        http://112.50.243.8/PLTV/88888888/224/3221225900/1.m3u8  # http stream

```

  
## Related


- [AIZOO Mask Detection](https://github.com/AIZOOTech/FaceMaskDetection)
- [AIZOO Dataset (Fixed)](https://drive.google.com/file/d/1QspxOJMDf_rAWVV7AU_Nc0rjo1_EPEDW/view)
- [Convert VOC to COCO](https://gist.github.com/Amir22010/a99f18ca19112bc7db0872a36a03a1ec)
- [YOLOv5](https://github.com/ultralytics/yolov5)

  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  