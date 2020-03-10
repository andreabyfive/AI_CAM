import sys 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import uic 

import urllib.request

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import win32api

aiMainUI = uic.loadUiType("AI_MainView.ui")[0]  # Load the UI


class MyWindow(QMainWindow, aiMainUI):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.url = "http://192.168.4.1"
        self.modelName = "runCoding.h5"
        self.model = tensorflow.keras.models.load_model(self.modelName)  # Load the model
        self.do_run = False
        self.resultVal = 0

    def execBtn_clicked(self):
        print ("exe clicked")

        self.do_run = True
        self.play()

    def stopBtn_clicked(self):
        print("stop clicked")

        self.do_run = False

    def play(self):
    
        playUrl = self.url + "/capture"
        print("\n*****\nstart (do_run Enable :{})\nURL : {} \nModel Name : {}\n***** \n".format(self.do_run, playUrl, self.modelName))
        
        while (self.do_run==True):
            
            try:
                imageOpen = urllib.request.urlopen(playUrl)

            except OSError as e:
                print("\n*****\nPlay Timeout {0}\n".format(e))
                win32api.MessageBox(0, 'Connect to camera please', 'Error Message')
                break
            except:
                print("\n*****Play Unexpected error:", sys.exc_info()[0])

            imageLoad = imageOpen.read()
            imageDecode = cv2.imdecode(np.fromstring(imageLoad, dtype=np.uint8), -1)
            imageOpen.close()

            #test
            #img = cv2.imread("5.jpg")
            
            cv2.imshow('imgae', imageDecode)
            if cv2.waitKey(5) & 0xFF == 0x20:
                break
        
            pilImage = Image.fromarray(imageDecode)

            # Disable scientific notation for clarity
            np.set_printoptions(suppress=True)

            # Create the array of the right shape to feed into the keras model
            # The 'length' or number of images you can put into the array is
            # determined by the first position in the shape tuple, in this case 1.
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

            #resize the image to a 224x224 with the same strategy as in TM2:
            #resizing the image to be at least 224x224 and then cropping from the center
            size = (224, 224)
            image = ImageOps.fit(pilImage, size, Image.ANTIALIAS)
            
            #turn the image into a numpy array
            image_array = np.asarray(image)

            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

            # Load the image into the array
            data[0] = normalized_image_array

            try:
                # run the inference
                prediction = self.model.predict(data)
                
                # 1~9까지 전달 default : 0
                if prediction[0][0] > 0.5:
                    self.resultVal = "1"
                    print("[1] First target {}".format(prediction[0][0]))
                elif prediction[0][1] > 0.5:
                    self.resultVal = "2"
                    print("[2] second target {}".format(prediction[0][1]))
                elif prediction[0][2] > 0.5:
                    self.resultVal = "3"
                    print("[3] second target {}".format(prediction[0][2]))
                elif prediction[0][3] > 0.5:
                    self.resultVal = "4"
                    print("[4] second target {}".format(prediction[0][3]))
                elif prediction[0][4] > 0.5:
                    self.resultVal = "5"
                    print("[5] second target {}".format(prediction[0][4]))
                elif prediction[0][5] > 0.5:
                    self.resultVal = "6"
                    print("[6] second target {}".format(prediction[0][5]))
                elif prediction[0][6] > 0.5:
                    self.resultVal = "7"
                    print("[7] second target {}".format(prediction[0][6]))
                elif prediction[0][7] > 0.5:
                    self.resultVal = "8"
                    print("[8] second target {}".format(prediction[0][7]))
                elif prediction[0][8] > 0.5:
                    self.resultVal = "9"
                    print("[9] second target {}".format(prediction[0][8]))
                else:
                    self.resultVal = "0"
                    print("no match!")
            except ValueError as ve:
                print("*********\nprediction error:{0}".format(ve))
            except:
                print("*********\nUnexpected error(prediction):", sys.exc_info()[0])
                break

            self.result()
  
        self.do_run = False
        cv2.destroyAllWindows()
        print("\n*****\nstop (do_run Enable :{})\nURL : {} \nModel Name : {}\n***** \n".format(self.do_run, self.url, self.modelName))
            
    def result(self):
        #oby 
        resultUrl = self.url + "/control?var=result&val=" + self.resultVal # check need (error)
        print("\n*****\nsend result({})\n".format(resultUrl))

        try:
            resultOpen = urllib.request.urlopen(resultUrl)
        except OSError as e:
            
            print("\n*****\nResult Timeout {0}\n".format(e))
            win32api.MessageBox(0, 'Re-start please', 'Error Message')
        except:
            print("\n*****Result Unexpected error:", sys.exc_info()[0])

        resultOpen.close() 

    def closeEvent(self,event):
        self.do_run = False
        print("Session STOP\n")

if __name__ == '__main__': 
    app = QApplication(sys.argv) 
  
    window = MyWindow()
    window.show() 
    sys.exit(app.exec_())