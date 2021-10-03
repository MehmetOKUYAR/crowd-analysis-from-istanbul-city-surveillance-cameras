from PyQt5.QtWidgets import QMainWindow,QMessageBox
from PyQt5.QtGui import QImage,QPixmap
from istanbul_city_surveillance_cameras_Gui_python import Ui_MainWindow
from src.camera_list import  selected_camera
from src.yolov4_pred import YOLOv4
import os
import time
import cv2

class istanbul_city_surveillance_cameras(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        self.ui.pushButton.clicked.connect(self.start_predict)
        self.ui.comboBox_2.currentIndexChanged[int].connect(self.select_camera)
        self.ui.pushButton_2.clicked.connect(self.page_menu)
        
        
        self.ui.stackedWidget.setCurrentIndex(0)

    def page_menu(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.stop = False
    #==================== Tespit etmek istediğiniz kamera bölgesi seçiliyor ==========================
    def select_camera(self,index):
        
        if index != 0:
            self.camera_index = index
            self.camera_name = self.ui.comboBox_2.itemText(index)
            self.url_cam = selected_camera(self.camera_index)
            print('url adresi',self.url_cam) 


    #=========== işlenmiş görüntüyü göster ================================
    def show_images_area(self,img):
        geo = self.ui.label_mobese.geometry()
        w,h = geo.getRect()[2:]
        image = cv2.resize(img,(w,h))
        frame = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        image = QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.ui.label_mobese.setPixmap(QPixmap.fromImage(image))

    #=================== Seçilen mobese üzerinden predict yapmaya başlar ============================
    def start_predict(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.stop = True
        #======= Yolov4 ağırlıkları  yüklenmektedir ========================
        weightsPath = "yolo_weight/yolov4-obj.weights"
        configPath = "yolo_weight/yolov4-obj.cfg"
                
        net = cv2.dnn.readNet(weightsPath, configPath)
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)

        cnt=0
        frames_to_count=20
        st=0

        vid = cv2.VideoCapture(self.url_cam) 

        if vid.isOpened() == False:
            QMessageBox.about(self,'Error','Can not connect camera. Turn back menu page')

        #============ kamera açıldıysa görüntüyü aktar ===========
        while(vid.isOpened()):
            ret,frame = vid.read()
            predicted_img,car_count,people_count = YOLOv4(net,frame)

            if car_count>20 :
                car_crowd = 'Crowded'
            else:
                car_crowd = 'Normal'

            if people_count>20 :
                people_crowd = 'Crowded'
            else:
                people_crowd = 'Normal' 

            text = f'Predictions on {self.camera_name} camera              People count: {people_count} -- {people_crowd}  ,  Car count: {car_count} -- {car_crowd}  '
            self.ui.label.setText(text)

            if cnt == frames_to_count:
                try:
                    print(frames_to_count/(time.time()-st),'FPS')
                    fps = round(frames_to_count/(time.time()-st)) 
                    st = time.time()
                    cnt=0
                except:
                    pass
            cnt+=1

            self.show_images_area(predicted_img)

            '''cv2.namedWindow('predict_video',cv2.WINDOW_NORMAL)
            cv2.resizeWindow('predict_video',1400,750)
            cv2.imshow("predict_video",frame)'''

            if cv2.waitKey(1) & self.stop == False:
                self.ui.label_mobese.clear()
                break

        vid.release()  
        cv2.destroyAllWindows()



