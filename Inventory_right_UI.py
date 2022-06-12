# MCU_Vending_Machine
# Client
import socket
import pandas as pd
import tkinter as tk
from tkinter import ttk
import tkinter.font
from Inventory_System import *

'''
#서버에 연걸
server_ip = 'localhost' #서버 ip
server_port = 9090      #포트번호

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #소켓 객체 생성
socket.connect((server_ip, server_port))    #연결
'''


# 물품수량 변경
# 바운더리 클래스
class Inventory_right_UI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.action = Inventory_System()  # 컨트롤 객체 생성

        self.controller = controller
        self.parent = parent

        self.name_label = tk.Label(self.parent, text='검색')
        self.name_label.pack()

        # 변경 프레임
        count_change_frame = tk.Frame(self.parent)
        # 레이블
        self.count_label = tk.Label(count_change_frame, text='변경할 수량을 입력하세요 :')
        self.count_label.grid(row=0, column=0)

        # 엔트리
        self.count_entry = tk.Entry(count_change_frame, width=10, justify='right')
        self.count_entry.grid(row=0, column=1, padx=10)

        # 버튼
        self.count_btn = tk.Button(count_change_frame, text='변경',
                                   command=lambda : self.action.count_modify(self.name_label,self.count_entry))
        self.count_btn.grid(row=0, column=2, padx=10)

        count_change_frame.pack()

    # 선택 값에 따라 프레임의 정보변경
    def modify(self, focus_item, treeview):
        self.action.frame_modify(focus_item, treeview, self.name_label, self.count_entry)
        self.parent.pack(side='right', expand=True)
