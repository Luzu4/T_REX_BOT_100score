import pyscreenshot as ImageGrab
import pyautogui
# make T-rex photo
# T_rex_position = (x=666, y=380)
# im=ImageGrab.grab(bbox=(666,384,700,420)) # X1,Y1,X2,Y2
# im.show()
# im.save('T-REX.png')

t_rex_x = pyautogui.locateOnScreen('T-REX.png')[0]
t_rex_y = pyautogui.locateOnScreen('T-REX.png')[1]
while True:
    im = ImageGrab.grab(bbox=(t_rex_x+97, t_rex_y+29, t_rex_x+104, t_rex_y+30))
    for x in range(5):
        if im.getpixel((x, 0)) != (247, 247, 247):
            print('?')
            pyautogui.press('space')
            break
