import cv2
import src.actions.WindowHandlers as Windows_handler
import src.actions.PixelSearch as Pixel_handler
import src.actions.MouseMovement as Mouse_handler
import numpy as np
import tempfile
import sys
import os

path = r"C:\Users\Neon\PycharmProjects\pytomatic\samples\Pokemon_go\training_data\pokestops"

config = {}

def nothing(x):
    pass

def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:

        print x, '--',y

        size = 20

        maxX,maxY, _ = param.shape
        tf = tempfile.NamedTemporaryFile(dir=path)


        if x < 0 + size: x = 0 + size
        if y < 0 + size: y = 0 + size

        if maxX < x - size: x = maxX - size
        if maxY < y - size: y = maxY + size

        img = param[y-size:y+size,x-size:x+size]


        cv2.imwrite(tf.name + '.png',img)

    return


def main():
    img = None
    main_win = Windows_handler.WinHandler(title='Nox',class_name='Qt5QWindowIcon')
    main_box = main_win.get_bbox()
    px_handler = Pixel_handler.PixelSearch(win_handler=main_win)
    mouse = Mouse_handler.MouseMovement(window_handler=main_win)
    main_win.init_window()
    cv2.namedWindow('image')
    cv2.namedWindow('config')

    # create trackbars for color change
    cv2.createTrackbar('R', 'config', 0, 255, nothing)
    cv2.createTrackbar('G', 'config', 0, 255, nothing)
    cv2.createTrackbar('B', 'config', 0, 255, nothing)
    cv2.createTrackbar('Offset', 'config', 0, 255, nothing)


    while True:

        img = px_handler.grab_window(bbox=main_box)
        img = px_handler.img_to_numpy(img,compound=False)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

        cv2.imshow('image',img)
        cv2.setMouseCallback('image', mouse_event, param=img)


        k = cv2.waitKey(1)
        if k == ord('q'):  # wait for ESC key to exit
            cv2.destroyAllWindows()
            quit(0)


if __name__ == '__main__':
    main()