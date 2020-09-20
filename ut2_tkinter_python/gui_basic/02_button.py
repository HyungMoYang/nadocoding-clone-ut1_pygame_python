from tkinter import *  # Tkinter 모듈 가져오고

root = Tk()  # Tkinter 정의 - main window

root.title("Nado GUI")  # 프로그램 title 설정
root.geometry("640x480")  # 가로 * 세로  크기 조정

# 1. 버튼의 생성
btn1 = Button(root, text="버튼1")  # 버튼 생성
btn1.pack()  # 버튼 포함시키기

# 2, 3. padx, pady = 버튼의 공간 확보
btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

# 4. width, height 버튼의 고정 크기 정의
btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

# 5. fg(foreground): 글자색 | bg(background):배경색
btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

# 6. 이미지를 사용한 버튼 추가
photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()


# 7. 동작하는 버튼
def btncmd():
    print("버튼이 클릭되었어요")


btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()
