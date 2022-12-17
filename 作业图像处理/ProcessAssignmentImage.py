import cv2
import numpy as np

#显示图像
def imgshow(img,title='image',showtime=0):
    cv2.imshow(title,img)#显示图像
    cv2.waitKey(showtime)
    cv2.destroyAllWindows()


#加载图像
def load_picture(path):
    img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    #img=cv2.add(img,120)
    #imgshow(img)
    return img


#处理图像
def deal_img(img,mid=128):
    ret,dst=cv2.threshold(img,mid,255,cv2.THRESH_BINARY)
    #print(ret)
    #print(dst)
    return dst


#获取阈值
def get_thresh(img):
    #print(img)
    img_mat=np.array(img)
    return round(img_mat.mean())


#开运算（先腐蚀再膨胀）
def open_(img):
    kernel = np.ones((11,11),np.uint8)
    opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
    return opening



if __name__ =="__main__":
    week=input('输入周数:')
    for i in range(3):
        # imgname = f'test ({i+10}).jpg'
        imgname = f'w{week}-{i+1}.jpg'
        print(f'正在处理 {imgname}')
        img = load_picture(f'E:\homework_img_deal\original/{imgname}')
        mid = get_thresh(img)
        print('阈值：',mid) 

        img_done = deal_img(img=img,mid=mid-20)
        # img1=img_done
        

        cv2.imwrite(f'E:\homework_img_deal\output\{imgname}',img_done)#保存图像
        print(f'已保存 {imgname}')
        # imgshow(cv2.resize(img_done,(0,0),fx=0.25,fy=0.25))


        # img_done = deal_img(img=img,mid=mid-30)
        # img2=img_done

        # img_done = deal_img(img=img,mid=mid-21)
        # img3=img_done

        # res = np.hstack((img1,img2))
        # imgshow(cv2.resize(res,(0,0),fx=0.25,fy=0.25))
