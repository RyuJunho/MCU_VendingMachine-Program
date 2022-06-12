# MCU_Vending_Machine
# Client
import socket
import pandas as pd

from Sale_System import *

import tkinter as tk
from tkinter import ttk
import tkinter.font

from datetime import datetime, timedelta

'''
#서버에 연걸
server_ip = 'localhost' #서버 ip
server_port = 9090      #포트번호

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #소켓 객체 생성
socket.connect((server_ip, server_port))    #연결
'''


# 거래내역 확인
# 바운더리 클래스
class Sale_UI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.action = Sale_System()

        self.title('거래내역 UI')
        self.geometry('600x500')
        self.resizable(False, False)

        # 레이블('재고관리')
        font = tkinter.font.Font(family='궁서', size=20, underline=True, slant='italic')
        self.label = tk.Label(self, text='\u2665 거래내역 \u2665', font=font)
        self.label.pack(pady=10)

        # 새로고침 버튼
        font = tkinter.font.Font(family='궁서', size=20, underline=True, slant='italic')
        self.repaint_btn = tk.Button(self, text='새로고침', font=font
                                     , command=lambda: self.action.repaint(self.Sale_Table))
        self.repaint_btn.pack(pady=30)

        #추가 버튼
        font = tkinter.font.Font(family='궁서', size=20, underline=True, slant='italic')
        self.repaint_btn = tk.Button(self, text='추가', font=font
                                     , command=lambda: self.action.sale_append(self.Sale_Table))
        self.repaint_btn.pack(pady=30)


        # 테이블과 스크롤바를 부착할 프레임
        transaction_frame = tk.Frame(self)

        # 테이블 생성
        self.Sale_Table = ttk.Treeview(transaction_frame, selectmode='browse')
        self.Sale_Table['columns'] = ('one', 'two')
        self.Sale_Table['show'] = 'headings'
        self.Sale_Table.pack(side='left')

        # 스크롤바 생성
        self.scrollbar = ttk.Scrollbar(transaction_frame, command=self.Sale_Table.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.Sale_Table.configure(yscrollcommand=self.scrollbar.set)

        # 테이블 속성 설정
        self.Sale_Table.column("one", width=200, )
        self.Sale_Table.heading("one", text="거래일자", anchor="center")

        self.Sale_Table.column("two", width=100, )
        self.Sale_Table.heading("two", text="제품명", anchor="center")

        transaction_frame.pack(padx=50)  # 검색 결과 테이블 프레임 부착




