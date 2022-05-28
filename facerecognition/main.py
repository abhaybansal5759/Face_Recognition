import tkinter as tk
import numpy as np
import face_recognition
from datetime import *
import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
import cv2
import os

window=tk.Tk()
window.title("Face recognition system")
#window.config(background="lime")
l1=tk.Label(window,text="Name",font=("Algerian",20))
l1.grid(column=0, row=0)
t1=tk.Entry(window,width=50,bd=5)
t1.grid(column=1, row=0)

l2 = tk.Label(window, text="Age", font=("Algerian", 20))
l2.grid(column=0, row=1)
t2 = tk.Entry(window, width=50, bd=5)
t2.grid(column=1, row=1)

l3 = tk.Label(window, text="Address", font=("Algerian", 20))
l3.grid(column=0, row=2)
t3 = tk.Entry(window, width=50, bd=5)
t3.grid(column=1, row=2)

l4 = tk.Label(window, text="External", font=("Algerian", 20))
l4.grid(column=0, row=3)
t4 = tk.Entry(window, width=50, bd=5)
t4.grid(column=1, row=3)


def entry():
    def Final_csv(file_name):
        f = pd.read_csv(file_name)
        f = f.drop_duplicates(subset=['Name'])
        f.to_csv(file_name, index=False)

    def findEncodings(images):
        encodeList = []

        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def markTIMEentry(name, Win_name):
        print("marking entry")
        Win_name += '.csv'
        with open(Win_name, 'r+') as f:
            myDataList = f.readlines()

            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
                if name not in nameList:
                    now = datetime.now()
                    dtString = now.strftime('%H:%M:%S')
                    f.writelines(f'\n{name},{dtString}')

    def cameraENTRY(img, Win_name):
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()

                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markTIMEentry(name, "ENTRY")

        cv2.imshow(Win_name, img)

    path = 'Training_images'

    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)

    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    nameList = []

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()

        cameraENTRY(img, 'ENTRY')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print("calling final csv")
    Final_csv("ENTRY.csv")

    cap.release()
    cv2.destroyAllWindows()


b1 = tk.Button(window, text="Entry", font=("Algerian", 20), bg='orange', fg='red', command=entry)
b1.grid(column=0, row=4)

def exit():
  def Final_csv(file_name):
    f = pd.read_csv(file_name)
    f = f.drop_duplicates(subset=['Name'])
    f.to_csv(file_name, index=False)


  def findEncodings(images):
    encodeList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


  def markTIMEexit(name, Win_name):
    print("marking exit")
    Win_name += '.csv'
    with open(Win_name, 'r+') as f:
        myDataList = f.readlines()

        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')

    print("done")


  def cameraEXIT(img, Win_name):
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markTIMEexit(name, "EXIT")

    cv2.imshow(Win_name, img)


  path = 'Training_images'

  images = []
  classNames = []
  myList = os.listdir(path)
  print(myList)

  for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
  print(classNames)

  nameList = []

  encodeListKnown = findEncodings(images)
  print('Encoding Complete')

  cap = cv2.VideoCapture(0)

  while True:
    success, img = cap.read()

    cameraEXIT(img, 'EXIT')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

  print("calling final csv")
  Final_csv("EXIT.csv")

  cap.release()
  cv2.destroyAllWindows()


b2 = tk.Button(window, text="Exit", font=("Algerian", 20), bg='green', fg='white', command=exit)
b2.grid(column=1, row=4)


def attendance():
    def clear_CSV(file_name):
        file = open(file_name, "r+")
        file.truncate(16)
        file.close()

    def TOminutes(Entry, Exit):
        IN = Entry.split(':')
        OUT = Exit.split(':')
        t1 = (int)(IN[0]) * 60 + (int)(IN[1])
        t2 = (int)(OUT[0]) * 60 + (int)(OUT[1])
        return t2 - t1

    df1 = pd.read_csv("ENTRY.csv")
    df2 = pd.read_csv("EXIT.csv")
    LIST = pd.read_csv("LIST.csv")

    result = df1.merge(df2, indicator=True, how='outer').loc[lambda v: v['_merge'] == 'both']
    result.drop(['_merge'], axis=1, inplace=True)

    result['DURATION'] = 0

    for i in range(result.shape[0]):
        result['DURATION'][i] = TOminutes(result['Time_ENTRY'][i], result['Time_EXIT_'][i])

    # dropping student records who have a duration less than a specified threshold
    result = result.drop(result[result.DURATION < 1].index)

    for i in range(LIST.shape[0]):
        if result.shape[0] != 0:
            for j in range(result.shape[0]):
                if result['Name'][j] == LIST['Name'][i]:
                    LIST['ATTENDANCE'][i] = "PRESENT"
                else:
                    LIST['ATTENDANCE'][i] = "ABSENT"
        else:
            LIST['ATTENDANCE'][i] = "ABSENT"

    '''
    print(df1)
    print()
    print(df2) 
    print()
    print(result)            
    print() 
    '''

    t = date.today()

    t = t.strftime("%m-%d-%Y")
    t = t + '.csv'

    print(LIST)

    LIST.to_csv(t)

    clear_CSV("ENTRY.csv")
    clear_CSV("EXIT.csv")



b3 = tk.Button(window, text="Mark Attendance", font=("Algerian", 20), bg='pink', fg='black', command=attendance)
b3.grid(column=2, row=4)


def update1():
    path = 'Training_images'
    def setname():
        global e
        ret, frame = cap.read()
        name = e.get()
        name = name + ".png"
        cv2.imwrite(os.path.join(path, name), frame)

    root = Toplevel(window)
    root.geometry('644x560')
    root.configure(bg='black')

    # Create a frame
    app = Frame(root, bg="white")
    app.grid()

    # Create a label in the frame
    lmain = Label(app)
    lmain.grid()

    # Capture from camera
    cap = cv2.VideoCapture(0)

    # function for video streaming
    def video_stream():
        _, frame = cap.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(1, video_stream)

    e = Entry(root, width=20, font=('Times 15'))
    e.place(x=200, y=490, width=250, height=25)
    e.focus_set()

    b = Button(root, text='UPDATE', command=setname, width=20, font=('Helvetica 15'), bg="white", fg="black")
    b.place(x=270, y=520, width=150, height=50)
    video_stream()
    root.mainloop()
    cap.release()
    cv2.destroyAllWindows()

b4 =tk.Button(window, text="Generate database", font=("Algerian", 20), bg='green', fg='white', command=update1)
b4.grid(column=3, row=4)
window.geometry("1000x300")
window.mainloop()













     # Warm greetings to every individual watching me here.
#     I am Abhay Bansal
     # an undergraduate student pursuing B.tech with a specialisation in the
     # information technology branch from the Jaipur engineering college
      # and research centre.
     #
     # I have been fortunate enough to be a part of the Microsoft mentee
#     program this program had helped me develop
     # and define my software development skills moreover this past month
#    has taught me a lot in terms of  practical
     # applications threw the knowledge
#     of many of new technology
#     how it is work and how the software development huge company
     #  like Microsoft work so for this demonstration this is the final video
#      demonstration for my project.


















