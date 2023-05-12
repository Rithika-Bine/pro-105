import os 
import cv2

path = "Images-1"

images = []

for files in os.listdir(path):
    name , ext = os.path.splitext(files)
    
    if ext in ['.gif' , '.png' , '.jpg','.jpeg','.jfif']:
        file_name = path + "/"+ files
        print(file_name)

        images.append(file_name)
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height,widht,channel = frame.shape
size = (widht,height)
print(size)

friends = cv2.VideoWriter("project.avi" , cv2.VideoWriter_fourcc(*'DIVX'),0.2,size)

for img in range(0,count,1) :
    frame = cv2.imread(images[img])
    friends.write(frame)

friends.release()
print("Done!!!")