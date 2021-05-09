# import pyscreenshot as ImageGrab
# import pyautogui
# import PIL
# # make T-rex photo
# # T_rex_position = (x=666, y=380)
# # im=ImageGrab.grab(bbox=(666,384,700,420)) # X1,Y1,X2,Y2
# # im.show()
# # im.save('T-REX.png')
#
# # make cactus photo
# # T_rex_position = (x=666, y=380)
# # im=ImageGrab.grab(bbox=(1012,420,1023,425)) # X1,Y1,X2,Y2
# # im.show()
# # im.save('Cactus13.png')
#
# import time
# import threading
#
#
#
# global t_rex_x
#
#
# from pynput.keyboard import Key, Listener
#
# def on_press(key):
#     def speed():
#         global t_rex_x
#         t_rex_x = t_rex_x + 40
#     global t_rex_x
#     print(time.time())
#     print(pyautogui.position()  )
#     pyautogui.leftClick()
#     print(pyautogui.locateOnScreen('T-REX.png'))
#     print(1619624004.810275 - 1619623993.8882897)
#     t_rex_x = pyautogui.locateOnScreen('T-REX.png')[0]
#     t_rex_y = pyautogui.locateOnScreen('T-REX.png')[1]
#
#     threading.Timer(10, speed).start()
#     while True:
#         #im = ImageGrab.grab(bbox=(740,384,780,415))
#         im = ImageGrab.grab(bbox=(t_rex_x+74, t_rex_y, t_rex_x+114, t_rex_y+31))
#         #score = ImageGrab.grab(bbox=(1218,301,1225, 311))
#         #score.show()
#         print(t_rex_x)
#         for x in range(15):
#             if im.getpixel((x, 28)) != (247, 247, 247):
#                 pyautogui.press('space')
#                 print(time.time())
#                 break
#
#         # if pyautogui.locateOnScreen('Cactus13.png'):
#         #     print(f"Cactus13 - {pyautogui.locateOnScreen('Cactus13.png')}")
#         #     print(f"T-REX: {pyautogui.locateOnScreen('T-REX.png')}")
#         #     pyautogui.press('space')
#
# with Listener(
#         on_press=on_press) as listener:
#     listener.join()


# import pyautogui
# import pyscreenshot as ImageGrab
#
# t_rex_x = pyautogui.locateOnScreen('T-REX.png')[0]
# t_rex_y = pyautogui.locateOnScreen('T-REX.png')[1]
#
# while True:
#     im = ImageGrab.grab(bbox=(t_rex_x+74, t_rex_y, t_rex_x+114, t_rex_y+31))
#     for x in range(15):
#         if im.getpixel((x, 28)) != (247, 247, 247):
#             im.show()
#             pyautogui.press('space')
#             break
#
#
import pyautogui
import pyscreenshot as ImageGrab

t_rex_x = pyautogui.locateOnScreen('T-REX.png')[0]
t_rex_y = pyautogui.locateOnScreen('T-REX.png')[1]
# Point(x=1224, y=310)
# Point(x=1217, y=299)
# score_1 = ImageGrab.grab(bbox=(1217,299,1224,312))
# score_1.save('score_1.png')
print(pyautogui.locateOnScreen('score_1.png', region=(1216,298,1225,313)))
speed = 0
while True:
    im = ImageGrab.grab(bbox=(t_rex_x+97+speed, t_rex_y+29, t_rex_x+104+speed, t_rex_y+30))
    for x in range(5):
        if im.getpixel((x, 0)) != (247, 247, 247):
            print('?')
            pyautogui.press('space')
            break
        try:
            if pyautogui.locateOnScreen('score_1.png', region=(1216, 298, 1225, 313))[0] == 1217:
                speed = 100
                print(pyautogui.locateOnScreen('score_1.png', region=(1216, 298, 1225, 313)))
        except TypeError:
            pass

#siemanko