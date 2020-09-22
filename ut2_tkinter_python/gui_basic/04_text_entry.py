from tkinter import *  # Tkinter 모듈 가져오고

root = Tk()  # Tkinter 정의
root.title("Nado GUI")  # 프로그램 title 설정
root.geometry("640x480")  # 가로 * 세로  크기 조정

# text widget (text area)
txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")  # text widget에 미리 text 추가

# entry
e = Entry(root, width=30)  # entry 정의
e.pack()
e.insert(0, "한 줄만 입력하세요")


# text, entry 가져오기, 삭제하기
def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))  # 1: 첫번째 라인, 0: 0번째 column 위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
