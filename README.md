
# Cell Phone Detection using your own custom dataset Step-by-Step (Windows/linux) 
## Requirements
- Pytorch>=1.4.0
- opencv-python
- matplotlib
- tqdm
- pillow

## Installation
- `Install Anaconda: https://docs.anaconda.com/anaconda/install/`
- `Create an new enviroment with cmd: conda create --name torch`
- `Update conda:  conda update -yn base -c defaults conda`
- `Install libraries: conda install -yc pytorch pytorch torchvision`
- `conda install -yc anaconda numpy opencv matplotlib tqdm pillow ipython future`


## Dataset

Download only image data of a cell-phone class from COCO Dataset, using `phone_download.py`
Then, read images and save as data file `data/data.txt`, using `savetxt.py`


## Labelling
Label data in darknet format: makesense.ai is a free open-source tool for labelling photo. The tool is really smooth and easy to use.
Github: https://github.com/SkalskiP/make-sense 
After label is done, you can download a `*.zip` data, contain `*.txt` files. Extract `*.zip` and save in folder `labels`

## Model
YOLOv3
ref: https://github.com/ultralytics/yolov3.git
 
This work use pretrained model `yolov3-tiny.pt`
Download pretrained wights from:  https://drive.google.com/drive/folders/1LezFG5g3BCW6iYaV89B2i64cqEUZD7e0

## Configuration
- Create a new `*.name` file listing the name of classes in dataset
- Create `*.data` file to define the locations of the files: train, test, and names of labels; Move file to folder 'data'
- Update `*.cfg` file: we only have one class, so change from 'filters=255' to 'filters=18', follow function filters=[4 + 1 + n] * 3, where n is your class count; Also modify classes=80 to classes=1

## Training
Run `python train.py --data data.data --cfg yolov3-tiny.cfg --batch 6`

## Test
Run python `detect.py --weights weights/last.pt --source 0`
- weights: using latest trained model 
-  source 'folder' if test data from specific folder,
    source '0' if real-time detection

