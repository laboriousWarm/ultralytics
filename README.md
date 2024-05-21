1. 数据集准备
   若准备使用自己的数据集，首先需要处理为yolov8所需格式，与yolov5处理相同，并按照如下规则放置.
   划分三个数据集文件在同一目录下  
   ![image](https://github.com/laboriousWarm/ultralytics/assets/32408245/2ca1a6bb-b55a-4e02-8ebb-57d9a73c9d0c)
   以train为例，内容如下  
   ![image](https://github.com/laboriousWarm/ultralytics/assets/32408245/3055675a-965b-4a2b-b98f-16e009132ccc)
   images中内容就是你的处理好的图片  
   ![image](https://github.com/laboriousWarm/ultralytics/assets/32408245/3d3a2204-4a23-4565-a881-2796f7236bc7)
   labels中为图片对应的标签，包含检测框大小类别等信息，以txt文件形式存放  
   ![image](https://github.com/laboriousWarm/ultralytics/assets/32408245/64f41b9e-a424-448e-982f-f50ba778ea62)
   ![image](https://github.com/laboriousWarm/ultralytics/assets/32408245/71bb0ae6-f96f-4145-9371-319b3ff324c7)
2.修改配置文件  
  修改yaml文件以让yolo适用自己的数据集，其中数据处理配置文件如下  
![image](https://github.com/laboriousWarm/ultralytics/assets/32408245/bb6c9a72-a8b8-4e00-bed1-502f1dc69bbf)
  若直接git clone本项目到ben本地需要修改绝对路径为自己的数据集的路径  
  接下来配置模型文件，修改其中的nc为自己的数据集中的类别，可以自行修改其他模块  
![image](https://github.com/laboriousWarm/ultralytics/assets/32408245/1d614354-a982-4753-8398-7155a28fa714)
  
  注意若选择nxms中任意一种规格的配置文件，需要预先从yolo8官网下载相应的权重文件，并在自己的模型yaml文件名后添加对应的字母表示规格（n,x等）  
3.训练  
  ![image](https://github.com/laboriousWarm/ultralytics/assets/32408245/f25a7d8f-98e2-4bb6-a652-d878606fbfa3)  
  直接执行python train.py就可以进行训练，注意修改相应的yaml和pt文件的路径为自己的绝对路径，并可以设置训练参数，我只更改了epoch和batch大小其他为默认参数  
  训练好后的最佳权重保存在以下位置  
  ![image](https://github.com/laboriousWarm/ultralytics/assets/32408245/b537558e-a4c8-4163-ad03-f7a2d6d04b64)  
4.检测自己的图片  
![image](https://github.com/laboriousWarm/ultralytics/assets/32408245/2cc4a59a-3ce4-4f4e-8dd9-27131d5d5b52)  
  
  在完成训练后可以执行python mypre.py来进行检测指定图片，配置如下  注意修改文件路径为绝对路径  
 
  





   


