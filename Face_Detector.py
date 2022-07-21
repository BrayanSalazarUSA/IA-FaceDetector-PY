import cv2

#Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Choose an image to detect faces in
""" img = cv2.imread('colombia_3.jpeg') """


#To capture a video from webcam.
webcam = cv2.VideoCapture(0)

#Itera siempre sobre la ventana
while True:
    #lee el actual frame (Lo pirmero que retorna es un boolena si se leyo o no, el segundo es el frame o marco)
    succesful_frame_read, frame = webcam.read()
    

    #Se debe convertir la imagen a escala de grises
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #detecta los rostros
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    #Dibujar un rectangulo alrededor del rostro

    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0),2)

    #SOlo es la ventana con la imagen que le pasemos
    cv2.imshow('Inteligente Detector De Rostros', frame)
    #Es la funcion que ejecuta la ventana
    key = cv2.waitKey(1)

    #Stop if Q key is pressed:
    if key==81 or key==113:
        break





""" cv2.rectangle(img,(3, 140), (3+56, 140+56), (0,0,255),2) """
""" print(face_coordinates) """


 


