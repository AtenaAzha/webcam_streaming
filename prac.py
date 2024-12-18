import cv2
import numpy as np
import time


class webcam:
    def __init__(self):
        pass
    def forpic(self):
        self.cap = cv2.VideoCapture(0)
        self.t0 = time.time()


        while True:
            self.ret,self.frame = self.cap.read()
            if self.ret:

                self.frame1 = cv2.flip(self.frame , 1)
                self.t1 = str(round(time.time() - self.t0))
                self.str_ti =str(self.t1)
                cv2.putText(self.frame1 ,self.t1 , (50,50) , cv2.FONT_HERSHEY_SIMPLEX , 2 ,(0,0,255),1)
                cv2.putText(self.frame1 , 'ATENA' , (100,100) , cv2.FONT_HERSHEY_SIMPLEX , 2 ,(0,255,255),1)
                self.gray = cv2.cvtColor(self.frame , cv2.COLOR_BGR2GRAY)
                print(self.gray.shape)
                self.frame2 = cv2.flip(self.frame,1)
                self.frame2[: , : , 2] = 255
                self.frame3= cv2.flip(self.frame , 0)
                self.frame4 = np.concatenate([self.gray , self.gray , self.gray] , 2)
                self.frame[:,:,0] = 255 
                self.gray = cv2.cvtColor(self.frame , cv2.COLOR_BGR2GRAY)
                self.image1 = np.concatenate([self.frame1,self.frame2],1)
                self.image2 = np.concatenate([self.frame3 , self.frame4],1)
                self.image3 = np.concatenate([self.image1 , self.image2],0)
                cv2.imshow('webcam',self.image3)
                self.q = cv2.waitKey(1)
                if self.q == ord('q'):
                    break
        self.cap.release()
        cv2.destroyAllWindows()
inst = webcam()
print(inst.forpic())

