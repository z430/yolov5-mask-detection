import shutil
import subprocess
import shutil
import glob
import os
import xml.etree.ElementTree as ET
import tqdm
import cv2
from sklearn import model_selection

dirs = ['train', 'val']
classes = ['with_mask', 'without_mask', 'mask_weared_incorrect']

def getImagesInDir(dir_path):
    image_list = []
    for filename in glob.glob(dir_path + '/*.png'):
        image_list.append(filename)

    return image_list

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(dir_path, output_path, image_path):
    basename = os.path.basename(image_path)
    basename_no_ext = os.path.splitext(basename)[0]

    in_file = open(os.path.join(dir_path, f"{basename_no_ext}.xml"))
    out_file = open(os.path.join(output_path, f"{basename_no_ext}.txt"), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()

    # get the image w and h with cv2
    img = cv2.imread(image_path)
    width = img.shape[1]
    height = img.shape[0]

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        box = (
            float(xmlbox.find('xmin').text),
            float(xmlbox.find('xmax').text),
            float(xmlbox.find('ymin').text),
            float(xmlbox.find('ymax').text)
        )
        bounding_box = convert((width, height), box)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bounding_box]) + '\n')


def main():
    cwd = 'datasets/archive/'
    for dir_path in dirs:
        full_dir_path = os.path.join(cwd, dir_path)
        output_path = os.path.join(cwd, f"yolo/labels/{dir_path}")
        image_folder = os.path.join(cwd, f"yolo/images/{dir_path}")
        print(f"output path: {output_path}")

        print(f"image_folder")
        print(f"full dir path: {full_dir_path}")
        print(f"{image_folder}")

        if not os.path.exists(output_path):
            os.makedirs(output_path)
            os.makedirs(image_folder)

        image_paths = getImagesInDir(full_dir_path)
        list_file = open(full_dir_path + '.txt', 'w')

        for image_path in tqdm.tqdm(image_paths):
            list_file.write(image_path + '\n')
            # print(image_path, image_folder)
            shutil.copy(image_path, image_folder)
            convert_annotation(full_dir_path, output_path, image_path)
        list_file.close()

        print("Finished processing: " + dir_path)

def split_image_set():
    images_dir = "datasets/archive/images"

    images_list = glob.glob(f"{images_dir}/*.png")

    # split train and val
    train, val = model_selection.train_test_split(images_list, test_size=0.3)
    print(len(train), len(val))

    os.makedirs("datasets/archive/train")
    os.makedirs("datasets/archive/val")

    for image in train:
        shutil.move(image, "datasets/archive/train")
        shutil.move(image.replace("png", "xml"), "datasets/archive/train")

    for image in val:
        shutil.move(image, "datasets/archive/val")
        shutil.move(image.replace("png", "xml"), "datasets/archive/val")


if __name__ == "__main__":
    main()
    # split_image_set()
