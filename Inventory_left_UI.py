# MCU_Vending_Machine
# Client
import socket
import pandas as pd
from Inventory_right_UI import *
from Inventory_System import *
import tkinter.font

'''
#서버에 연걸
server_ip = 'localhost' #서버 ip
server_port = 9090      #포트번호

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #소켓 객체 생성
socket.connect((server_ip, server_port))    #연결
'''


# 물품수량 확인
# 바운더리 클래스
class Inventory_left_UI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.action = Inventory_System()  # 컨트롤클래스 객체 생성

        self.title('재고관리 UI')
        self.geometry('800x500')
        self.resizable(False, False)

        # 제품 목록이 출력될 왼쪽 프레임
        left_frame = tk.Frame(self, width=200)
        left_frame.pack(side='left')

        # 레이블('재고관리')
        font = tkinter.font.Font(family='궁서', size=20, underline=True, slant='italic')
        self.label = tk.Label(left_frame, text='\u2662 재고관리 \u2665', font=font)
        self.label.pack(pady=10)

        # 새로고침 버튼
        font = tkinter.font.Font(family='궁서', size=20, underline=True, slant='italic')
        self.repaint_btn = tk.Button(left_frame, text='새로고침', font=font
                                     , command=lambda: self.action.repaint(self.itemTable))
        self.repaint_btn.pack(pady=30)

        # 테이블과 스크롤바를 부착할 프레임
        item_frame = tk.Frame(left_frame)

        # 테이블 생성
        self.itemTable = ttk.Treeview(item_frame, selectmode='browse')
        self.itemTable['columns'] = ('one', 'two', 'three')
        self.itemTable['show'] = 'headings'
        self.itemTable.pack(side='left')

        # 스크롤바 생성
        self.scrollbar = ttk.Scrollbar(item_frame, command=self.itemTable.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.itemTable.configure(yscrollcommand=self.scrollbar.set)

        # 테이블 속성 설정
        self.itemTable.column("one", width=100, )
        self.itemTable.heading("one", text="제품명", anchor="center")

        self.itemTable.column("two", width=100, )
        self.itemTable.heading("two", text="잔여 수량", anchor="center")

        self.itemTable.column("three", width=100, )
        self.itemTable.heading("three", text="제품 가격(원)", anchor="center")

        item_frame.pack(padx=50)  # 검색 결과 테이블 프레임 부착

        # 선택버튼
        self.ChoiceButton = tk.Button(left_frame, text='선택', width=30
                                      , command=lambda: self.frame.modify(self.itemTable.focus(), self.itemTable))
        self.ChoiceButton.pack(pady=40)

        # 오른쪽 프레임(선택버튼 클릭시 나타남)
        self.right_frame = tk.Frame(self)
        self.right_frame.pack(side='right', expand=True)
        self.frame = Inventory_right_UI(parent=self.right_frame, controller=self)  # 오른쪽 화면 객체
        self.right_frame.pack_forget()
