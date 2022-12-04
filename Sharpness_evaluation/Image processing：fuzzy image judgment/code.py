import cv2
import os

def getPhotopath(paths):
    imgfile = []
    file_list=os.listdir(paths)
    for i in file_list:
        newph=os.path.join(paths,i)
        imgfile.append(newph)
    return imgfile

def getImgVar(image):
    imggray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageVar = cv2.Laplacian(imggray, cv2.CV_64F).var()
    return imageVar

def getTest(imgfile):
    c = []
    for i in imgfile:
        # print(i)
        img=cv2.imread(i)
        image=getImgVar(img)
        # print(image)
        c.append(float(f"{image:.3f}"))
    if 'test' in imgfile[0]:   #对测试集数据进行反转
        c.sort(reverse=True)
    else:
        c.sort()
    return c

def getThr():
    a=getTest(imgfile1)
    b=getTest(imgfile2)
    thr=(a[0],b[0])
    # print(thr)
    return thr

path1="./test"     #测试的数据集文件夹位置
path2="./Standards"  #标准图的数据文件夹位置
#获取文件下的名称
imgfile1=getPhotopath(path1)
imgfile2=getPhotopath(path2)

#获得阈值
minThr,maxThr=getThr()
print(minThr,maxThr)

def vagueJudge(image):
    img = cv2.imread(image)
    imgVar = getImgVar(img)
    if imgVar>maxThr:
        cv2.putText(img, f"Not Vague{imgVar:.2f}", (12, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
    else:
        cv2.putText(img, f"Vague{imgVar:.2f}", (12, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
    cv2.imshow("img",img)
    k=cv2.waitKey(0) & 0xFF
image="./Standards/001.jpg"   #需要进行测试的图片
vagueJudge(image)