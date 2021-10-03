import cv2 
import random
from src.class_name import predict_name

def YOLOv4(model,image):
    car_count = 0
    people_count = 0
    model = cv2.dnn_DetectionModel(model)
    model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

    confThreshold= 0.4
    nmsThreshold = 0.3

   
    classes, confidences, boxes = model.detect(image, confThreshold, nmsThreshold)
    
    if len(boxes) > 0:
        for cl, score, (left, top, width, height) in zip(classes, confidences, boxes):
            if cl[0]==0:car_count +=1
            if (cl[0]-1)==0:people_count +=1
            start_point = (int(left), int(top))
            end_point = (int(left + width), int(top + height))
            
            b= random.randint(0,255)
            g= random.randint(0,255)
            r= random.randint(0,255)
            COLORS = [[b, g, r]]
            color = COLORS[0]


            img = cv2.rectangle(image, start_point, end_point, color, 1)  # draw class box
            name = predict_name(cl[0])
            text = f'{name}: {score[0]:0.2f}'

            cv2.putText(img, text, (int(left), int(top-7)), cv2.FONT_HERSHEY_SIMPLEX, 0.3, COLORS[0], 1)  # print class type with
    else:
        img = image
    return img,car_count,people_count
