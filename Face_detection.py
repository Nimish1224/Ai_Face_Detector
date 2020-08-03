import cv2
from random import randrange


# You can load this data online also
# Train_face_data = cv2.CascadeClassifier('https://github.com/opencv/opencv/blob/master/data/haarcascades/harrcascade_frontalface_default.xml')

# Load some pretrained data on face frontals from opencv (harr cascade algorithm)
Train_face_data =cv2.CascadeClassifier('C:/Users/nimis/Desktop/Face Detector/haarcascade_frontalface_default.xml')
# After declearing variable you'll have to load that file
Train_face_data.load('haarcascade_frontalface_default.xml')



# To capture video from webcamp
webcamp = cv2.VideoCapture(0)

# for video
# webcamp = cv2.VideoCapture('https://media.giphy.com/media/GPn300EibJ2F2/giphy.gif')


while True:
	#Read current Frame
	succesful_frame_read,frame = webcamp.read()

	#Must convert to grayscale
	grayscale_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


	#Detect Faces
	face_coordinates = Train_face_data.detectMultiScale(grayscale_img)

	#Draw rectangle around faces
	for (x,y,w,h) in face_coordinates: 
		cv2.rectangle(frame,(x,y),(w+x,y+h),(randrange(128,256),randrange(128,256),randrange(128,256)),3)

	cv2.imshow('FAce DEtrctor',frame)
	key = cv2.waitKey(1)

	#Stop if Q key is pressed
	if key==81 or key==113:
		break

#Release videoCapture object
webcamp.release()


############# (For Image use Below code) #############

# import cv2
# from random import randrange

# Load some pretrained data on face frontals from opencv (harr cascade algorithm)
# Train_face_data =cv2.CascadeClassifier('C:/Users/nimis/Desktop/Face Detector/haarcascade_frontalface_default.xml')
# After declearing variable you'll have to load that file
# Train_face_data.load('haarcascade_frontalface_default.xml')


# Choose an image to detect faces in 
# img = cv2.imread('im.jpg')

# Must convert to grayscale
# grayscale_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Detect Faces
# face_coordinates = Train_face_data.detectMultiScale(grayscale_img)

# Draw rectangle around faces
# for (x,y,w,h) in face_coordinates: 
# 	cv2.rectangle(img,(x,y),(w+x,y+h),(randrange(128,256),randrange(128,256),randrange(128,256)),3)


# print(face_coordinates)
# cv2.imshow('FAce DEtrctor',img)
# cv2.waitKey()
# print("Code Completed")