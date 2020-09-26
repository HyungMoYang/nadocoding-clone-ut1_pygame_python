import tkinter.ttk as ttk  # Combo Box를 사용하기 위해서
from tkinter import *  # Tkinter 모듈 가져오고


root = Tk()  # Tkinter 정의
root.title("Nado GUI")  # 프로그램 title 설정
root.geometry("640x480")  # 가로 * 세로  크기 조정

# Combo Box
values = [str(i) + "일" for i in range(1, 32)]  # 1~31까지 숫자
combobox = ttk.Combobox(root, height=5, value=values)
combobox.pack()
combobox.set("카드 결제일")  # 최초 목록 제목 설정

# readonly Combo Box - Combo Box의 내용을 변경할 수 없음.
readonly_combobox = ttk.Combobox(
    root, height=10, value=values, state="readonly")
readonly_combobox.current(0)  # 0번째 index 값 초기 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())


btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()
