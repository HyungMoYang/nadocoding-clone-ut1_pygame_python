import time
import tkinter.ttk as ttk  # Combo Box를 사용하기 위해서
from tkinter import *  # Tkinter 모듈 가져오고


root = Tk()  # Tkinter 정의
root.title("Nado GUI")  # 프로그램 title 설정
root.geometry("640x480")  # 가로 * 세로  크기 조정

# progress bar 1
# # progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(5)  # 5ms 마다 움직임
# progressbar.pack()


# def btncmd():
#     progressbar.stop() # 작동 중지


# btn = Button(root, text="중지", command=btncmd)
# btn.pack()


# progress bar 2
p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)  # 0.01초 대기

        p_var2.set(i)  # progress bar의 값 설정
        progressbar2.update()  # ui 업데이트
        print(p_var2.get())  # 값 가져오기


btn = Button(root, text="시작", command=btncmd2)
btn.pack()


root.mainloop()
