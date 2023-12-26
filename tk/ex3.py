from tkinter import *
import cv2 as cv


def get_variable_name(var):
    for name, value in globals().items():
        if value is var:
            return name


def cv_show(img):
    title = get_variable_name(img)
    cv.namedWindow(title, cv.WINDOW_NORMAL)
    cv.imshow(title, img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return


def show_image(path:str):
    img=cv.imread(path,cv.IMREAD_ANYDEPTH)
    # cv_show(img)
    return img


# def create_new_window():
#     new_window = tk.Toplevel()

#     # Add widgets to the new window here

root = Tk()
# 创建侧边栏
sidebar = Frame(root, bg='#234567', width=100, height=500)
sidebar.pack(side=RIGHT, fill=Y)

# 创建主窗口
main_window = Frame(root, bg='white', width=500, height=500)
main_window.pack(side=LEFT, fill=BOTH, expand=True)

button = Button(main_window, text="show", command=show_image("./res/pxArt.png"))
button.pack()

root.mainloop()
