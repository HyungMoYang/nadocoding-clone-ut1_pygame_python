from tkinter import *  # Tkinter 모듈 가져오고

root = Tk()  # Tkinter 정의
root.title("Nado GUI")  # 프로그램 title 설정
root.geometry("640x480")  # 가로 * 세로  크기 조정

# listbox
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    # 삭제
    # listbox.delete(END)  # 맨 뒤의 항목을 삭제
    # listbox.delete(0)  # 맨 앞의 항목을 삭제

    # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인 (시작 index, 끝 index)
    # print("1번째부터 3번째까지의 항목: ", listbox.get(0, 2))

    # 선택된 항목 확인 (위치(index)로 반환) - tuple로 반환
    print("선택된 항목: ", listbox.curselection(), type(listbox.curselection()))


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
