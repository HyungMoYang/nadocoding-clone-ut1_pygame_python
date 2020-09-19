from tkinter import *  # Tkinter 모듈 가져오고

root = Tk()  # Tkinter 정의

root.title("Nado GUI")  # 프로그램 title 설정
root.geometry("640x480")  # 가로 * 세로  크기 조정
# root.geometry("640x480+300+100")  # 가로 * 세로 + x좌표 + y좌표 : 창이 뜨는 위치 조정

root.resizable(False, False)  # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

root.mainloop()
