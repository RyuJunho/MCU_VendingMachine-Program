# MCU_Vending_Machine
# Client


import tkinter as tk
from tkinter import ttk
import tkinter.font
from PIL import ImageTk, Image
from Sale_DB import *
from Item_DB import *
from datetime import datetime, timedelta
import socket

# 바운더리 클래스
class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # 제품 목록이 출력될 왼쪽 프레임
        '''
        #서버에 연걸
        server_ip = 'localhost' #서버 ip
        server_port = 9090      #포트번호

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #소켓 객체 생성
        client_socket.connect((server_ip, server_port))    #연결
        '''


        self.ItemDB = Item_DB()  # Item_DB객체 생성
        self.Item_df = self.ItemDB.get_df()

        self.SaleDB = Sale_DB()  # Item_DB객체 생성
        self.Sale_df = self.SaleDB.get_df()
        self.title('자판기관리')

        left_frame = tk.Frame(self, width=200)
        left_frame.pack(side='left')

        # 레이블('재고관리')
        self.label = tk.Label(left_frame, text='재고관리')
        self.label.pack(pady=10)

        # 새로고침 버튼
        self.repaint_btn = tk.Button(left_frame, text='새로고침'
                                     , command=lambda: self.item_repaint(self.itemTable))
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
                                      , command=lambda: self.modify(self.itemTable.focus(), self.itemTable))
        self.ChoiceButton.pack(pady=40)


        self.name_label = tk.Label(left_frame, text='선택된 항목 없음')
        self.name_label.pack()

        # 변경 프레임
        count_change_frame = tk.Frame(left_frame)
        # 레이블
        self.count_label = tk.Label(count_change_frame, text='변경할 수량을 입력하세요 :')
        self.count_label.grid(row=0, column=0)

        # 엔트리
        self.count_entry = tk.Entry(count_change_frame, width=10, justify='right')
        self.count_entry.grid(row=0, column=1, padx=10)

        # 버튼
        self.count_btn = tk.Button(count_change_frame, text='변경',
                                   command=lambda: self.count_modify(self.name_label, self.count_entry))
        self.count_btn.grid(row=0, column=2, padx=10)

        count_change_frame.pack(pady=10)





        right_frame = tk.Frame(self, width=200)
        right_frame.pack(side='left')

        # 레이블('재고관리')
        self.label = tk.Label(right_frame, text='거래내역')
        self.label.pack(pady=10)

        #추가 버튼
        self.repaint_btn = tk.Button(right_frame, text='새로고침'
                                     , command=lambda: self.sale_repaint(self.Sale_Table,'사과'))
        self.repaint_btn.pack(pady=30)


        # 테이블과 스크롤바를 부착할 프레임
        transaction_frame = tk.Frame(right_frame)

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

        transaction_frame.pack(padx=50,pady=30)  # 검색 결과 테이블 프레임 부착

        #self.socket_rev()


    # 선택 버튼 클릭시 값에 따라 프레임의 정보변경
    def modify(self, focus_item, treeview):
        item_name = treeview.item(focus_item).get('values')[0]
        self.name_label.configure(text=f'{item_name}')
        self.count_entry.delete(0, 'end')

    #변경 버튼 클릭 시
    def count_modify(self,name_label,count_entry):
        self.ItemDB = Item_DB()  # Item_DB객체 생성
        self.Item_df = self.ItemDB.get_df()
        self.Item_df.loc[name_label['text'],'ItemCount'] = count_entry.get()
        print(f'{count_entry.get()}으로 값 변경 완료')
        print(self.Item_df.loc[name_label['text'],'ItemCount'])
        #msg.showinfo('수량변경 완료', '수량변경이 완료되었습니다!')

        #파일 저장
        self.Item_df.to_csv("csv/Item.csv",index=False,encoding='cp949')
        self.item_repaint(self.itemTable)

        #self.socket_send('사과')

    #재고관리에서 새로고침 클릭 시
    def item_repaint(self,treeview):
        self.ItemDB = Item_DB()  # Item_DB객체 생성
        self.Item_df = self.ItemDB.get_df()

        # 기존 값 제거
        for item in treeview.get_children():
            treeview.delete(item)

        # 새로운 값 추가
        for index, row in self.Item_df.iterrows():
            treeview.insert('', 'end', text='', value=(row['ItemName'], row['ItemCount'], row['ItemPrice']))

    #거래내역에서 새로고침 클릭 시
    def sale_repaint(self,treeview,word):
        self.SaleDB = Sale_DB()  # Item_DB객체 생성
        self.Sale_df = self.SaleDB.get_df()
        item_name = word
        Sale_date = (datetime.today()).strftime("%Y-%m-%d")  # 대여일

        #추가할 데이터프레임
        Sale_df = pd.DataFrame({'SaleDate': Sale_date, 'SaleName': item_name},index=[0])
        #데이터 추가
        self.Sale_df = self.Sale_df.dropna()
        self.Sale_df = pd.concat([self.Sale_df,Sale_df],ignore_index=True)

        #파일 저장
        self.Sale_df.to_csv("csv/Sale.csv",index=False,encoding='cp949')

        #테이블 설정
        # 기존 값 제거
        for item in treeview.get_children():
            treeview.delete(item)

        # 새로운 값 추가
        for index, row in self.Sale_df.iterrows():
            treeview.insert('', 'end', text='', value=(row['SaleDate'], row['SaleName']))

        #msg.showinfo('새로고침 완료', '새로고침이 완료되었습니다!')


    def socket_send(self,word):
        self.client_socket.sendall(word.endcode())


    def socket_rev(self):
        while True :
            self.ItemDB = Item_DB()  # Item_DB객체 생성
            self.Item_df = self.ItemDB.get_df()

            self.SaleDB = Sale_DB()  # Item_DB객체 생성
            self.Sale_df = self.SaleDB.get_df()

            data = self.client_socket.recv(1024)
            print(repr(data.decode()))
            data_list = repr(data.decode()).split(',')

            if data_list[0] == '거래내역' :

                self.item_repaint(self.itemTable)
                self.sale_repaint(self.Sale_Table,data_list[1])

            self.Item_df.to_csv("csv/Item.csv", index=False, encoding='cp949')
            self.Sale_df.to_csv("csv/Sale.csv", index=False, encoding='cp949')



app = Main()
app.mainloop()
