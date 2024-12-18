import cv2
import numpy as np
import vlc
import time

class Toles:
    def __init__(self):
        self.eye_detect  = cv2.CascadeClassifier("haarcascade_eye.xml")
        self.face_detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        
    def eye_face(self):
        self.cap = cv2.VideoCapture(0)
        while True:
            self.ret ,self.frame = self.cap.read()
            if self.ret:
                self.frame = cv2.flip(self.frame , 1)
                self.gray  = cv2.cvtColor(self.frame , cv2.COLOR_BGR2GRAY)
                self.result1 = self.face_detect.detectMultiScale(self.gray)
                self.result2 = self.eye_detect.detectMultiScale(self.result1)
                
                for (x , y , w , h) in self.result1:
                    cv2.rectangle(self.frame , (x,y) , (x+w , y+h) , (0,0,255) , 2)
                cv2.imshow("webcam" , self.frame) 
                q = cv2.waitKey(1)
                if q == ord('q'):
                    break
        self.cap.release()
        cv2.destroyAllWindows()


    def tolebar(self , movie_music_book):
        self.movie_music_book = movie_music_book

        if self.movie_music_book == 'movie':
            movie = cv2.VideoCapture("movie.mp4")
            while True:
               self.ret ,self.frame = movie.read()
               if self.ret:
                    self.frame = cv2.flip(self.frame , 1)
                    self.gray  = cv2.cvtColor(self.frame , cv2.COLOR_BGR2GRAY)

                    cv2.imshow("webcam" , self.frame) 
                    q = cv2.waitKey(1)
                    if q == ord('q'):
                        break
                    else:
                        break
            self.cap.release()
            cv2.destroyAllWindows()

        elif self.movie_music_book == 'music':
              music = vlc.MediaPlayer()
              music.play()
              time.sleep(10)

        elif self.movie_music_book == "book":
            print('1984')





inst = Toles()
# print(inst.eye_face())
print(inst.tolebar('book'))