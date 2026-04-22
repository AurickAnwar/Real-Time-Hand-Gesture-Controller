import mediapipe as mp
import cv2
import pyautogui
import math
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 10000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000)
mp_hands = mp.solutions.hands.Hands()
mp_draw = mp.solutions.drawing_utils

MY_CONNECTOR_STYLE = mp_draw.DrawingSpec(color=(255,255,0), thickness=2)
MY_LANDMARK_STYLE = mp_draw.DrawingSpec(color=(255,255,255), thickness=2) 

last_pause = 0
last_mute = 0
last_click = 0
pause_cooldown = 1.0

screen_x, screen_y = pyautogui.size()


while True:
    check, img = cap.read()
    if not check:
        break
    
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    results = mp_hands.process(rgb)

    num_hands = 0

    fps = cap.get(cv2.CAP_PROP_FPS)
    cv2.putText(img, 'FPS: ' + str(fps), (10,120), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0), thickness = 3)

    if results.multi_hand_landmarks:
        num_hands = len(results.multi_hand_landmarks)

        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                img,
                hand_landmarks,
                mp.solutions.hands.HAND_CONNECTIONS,
                landmark_drawing_spec=MY_LANDMARK_STYLE,
                connection_drawing_spec=MY_CONNECTOR_STYLE
            )

            x1 = hand_landmarks.landmark[4].x
            y1 = hand_landmarks.landmark[4].y
            x2 = hand_landmarks.landmark[8].x
            y2 = hand_landmarks.landmark[8].y
 
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

            index_up = hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y
            middle_up = hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y
            ring_up = hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y
            pinky_up = hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y
            thumb_up = hand_landmarks.landmark[4].y < hand_landmarks.landmark[2].y

            full_hand = index_up and middle_up and ring_up and pinky_up and thumb_up
            #fist = not index_up and not middle_up and not ring_up and not pinky_up and not thumb_up

            current_time = time.time()
            x = int(hand_landmarks.landmark[8].x * screen_x)
            y = int(hand_landmarks.landmark[8].y * screen_y)

            # play/pause gesture
            if full_hand and current_time - last_pause > pause_cooldown:
                pyautogui.press("space")
                last_pause = current_time
            
            elif middle_up and not index_up and not ring_up and current_time - last_mute > pause_cooldown:
                pyautogui.press('volumemute')
                last_mute = current_time

            elif index_up and middle_up and not ring_up and not pinky_up and current_time - last_click > pause_cooldown:
                pyautogui.click()
                last_click = current_time
            
            elif ring_up and not index_up and not middle_up and not pinky_up:
                pyautogui.press("right") 
            
            elif pinky_up and not index_up and not middle_up and not ring_up:
                 pyautogui.press("left")
            
            elif index_up:
                pyautogui.moveTo(x,y)
            

            else:
                if distance > 0.2:
                    pyautogui.press("volumeup")
                elif distance < 0.10:
                    pyautogui.press("volumedown")

    cv2.putText(img, f"Hands: {num_hands}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (75, 150, 225), 3)
    cv2.putText(img, "Press i for instructions", (10,180), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), thickness=3)

    cv2.imshow("img", img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == ord('s'):
        cv2.imwrite("HandGestureControl.jpg", img)
    if key == ord('i'):
        img1 = cv2.imread("HandInstructions.png")
        cv2.imshow("Instructions", img1)
       
   

cap.release()
cv2.destroyAllWindows()