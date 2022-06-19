# MCU_Vending_Machine
# Client
import pandas as pd

from Sale_System import *

import tkinter as tk
from tkinter import ttk
import tkinter.font
import socket


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

        #추가 버튼
        font = tkinter.font.Font(family='궁서', size=20, underline=True, slant='italic')
        self.repaint_btn = tk.Button(self, text='추가', font=font
                                     , command=lambda: self.action.sale_repaint(self.Sale_Table,'사과'))
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

        #닫기 버튼
        font = tkinter.font.Font(family='궁서', size=20, underline=True, slant='italic')
        self.repaint_btn = tk.Button(self, text='닫기', font=font
                                     , command=lambda: self.socket_close())
        self.repaint_btn.pack(pady=30)




