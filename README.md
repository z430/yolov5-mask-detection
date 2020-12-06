## Face Mask Detection with YOLOv5
Detect faces and check if they are using mask or not

## Requirements
```bash
$ pip install -r requirements.txt

```

## Dataset
* [AIZOO Dataset](https://drive.google.com/file/d/1QspxOJMDf_rAWVV7AU_Nc0rjo1_EPEDW/view)

## Inference

detect.py runs inference on a variety of sources, downloading models automatically from the [latest model release](https://github.com/z430/yolov5-mask-detection/releases) and saving results to `runs/detect`.
```bash
$ python detect.py --source 0  # webcam
                            file.jpg  # image 
                            file.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
                            rtsp://170.93.143.139/rtplive/470011e600ef003a004ee33696235daa  # rtsp stream
                            rtmp://192.168.1.105/live/test  # rtmp stream
                            http://112.50.243.8/PLTV/88888888/224/3221225900/1.m3u8  # http stream
```

## Results

## Citation
* convert_voc_to_yolo.py [1](https://gist.github.com/Amir22010/a99f18ca19112bc7db0872a36a03a1ec)
* yolov5 [2](https://github.com/ultralytics/yolov5)
