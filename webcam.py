import cv2
import hashlib
import time
import base64

def base64_sha256(frame):
    data = frame.tobytes()
    n = hashlib.sha256(data).digest()
    n = base64.b64encode(n)
    return n

def int_sha256(frame):
    data = frame.tobytes()
    n = hashlib.sha256(data).hexdigest()
    n = int(n, 16)
    return n


cap = cv2.VideoCapture(0)
print("random number generator with webcam. For using it, press the number for the command you want to do in the webcam window::")
print("0:exit")
print("1:int output after using SHA256")
print("2:generate n ammount of time a number between 1 and 5, and report the stats")
print("3:generate a number in a custom range")
print("4:base64 hash output")

while True:
    ret, frame = cap.read()
    cv2.imshow("camera", frame)

    tasto = cv2.waitKey(1) & 0xFF

    if tasto == ord('0'):
        break

    if tasto == ord('1'):
        n = int_sha256(frame)
        print(n)

    if tasto == ord("2"):
        n1 = 0
        n2 = 0
        n3 = 0
        n4 = 0
        n5 = 0
        n = int(input("number of generation:"))
        inizio = time.time()

        for i in range(n):
            print(f"elaborating... {i+1}/{n}", end="\r")
            ret, frame = cap.read()
            risultato = int_sha256(frame)
            cv2.imshow("camera", frame)
            cv2.waitKey(1)

            if (risultato % 5) + 1 == 1:
                n1 += 1
            if (risultato % 5) + 1 == 2:
                n2 += 1
            if (risultato % 5) + 1 == 3:
                n3 += 1
            if (risultato % 5) + 1 == 4:
                n4 += 1
            if (risultato % 5) + 1 == 5:
                n5 += 1

        fine =time.time()
        print("\n")
        print(f"\n1: {(n1*100)/n}% ({n1})\n")
        print(f"2: {(n2*100)/n}% ({n2})\n")
        print(f"3: {(n3*100)/n}% ({n3})\n")
        print(f"4: {(n4*100)/n}% ({n4})\n")
        print(f"5: {(n5*100)/n}% ({n5})\n")
        print(f"time: {fine-inizio:.2f} seconds\n")
    
    if tasto == ord("3"):
        minimo = int(input("minimun number?"))
        massimo = int(input("max number?"))

        if minimo >= massimo or massimo == 0:
            print("number not valid")
        else:
            print((int_sha256(frame) % ((massimo - minimo + 1)) + minimo))
    
    if tasto == ord('4'):
        n = base64_sha256(frame)
        print(n) 

            
#conversione in base64 (stringa)
cap.release()
cv2.destroyAllWindows()
