from tkinter import *  # Tkinter 모듈 가져오고

root = Tk()  # Tkinter 정의 - main window

root.title("Nado GUI")  # 프로그램 title 설정
root.geometry("640x480")  # 가로 * 세로  크기 조정

# 1. label 기초
label1 = Label(root, text="안녕하세요")
label1.pack()

# 2. image label 추가
photo = PhotoImage(file="gui_basic/img.png")  # 이미지 불러오고
label2 = Label(root, image=photo)  # 추가할 label 만들고
label2.pack()  # label 추가


# 3. label 변화 시키기
def change():
    label1.config(text="또 만나요")  # label 변경

    global photo2  # 전역으로 photo2를 선언
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)  # 사진 label변경


btn = Button(root, text="클릭", command=change)
btn.pack()


root.mainloop()
