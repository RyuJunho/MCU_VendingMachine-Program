#MCU_Vending_Machine
#Client
import socket
import pandas as pd
from tkinter import*

from Sale_DB import *
from datetime import datetime, timedelta

'''
#서버에 연걸
server_ip = 'localhost' #서버 ip
server_port = 9090      #포트번호

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #소켓 객체 생성
socket.connect((server_ip, server_port))    #연결
'''

#거래내역 확인
#컨트롤 클래스
class Sale_System():
    def __init__(self):
        self.SaleDB = Sale_DB()  # Item_DB객체 생성
        self.Sale_df = self.SaleDB.get_df()


    def sale_append(self,treeview):
        item_name = '사과'
        Sale_date = (datetime.today()).strftime("%Y-%m-%d")  # 대여일

        #추가할 데이터프레임
        Sale_df = pd.DataFrame({'SaleDate': Sale_date, 'SaleName': item_name},index=[0])
        #데이터 추가
        self.Sale_df = self.Sale_df.dropna()
        self.Sale_df = pd.concat([self.Sale_df,Sale_df],ignore_index=True)

        #파일 저장
        self.Sale_df.to_csv("csv/Sale.csv",index=False)

        #테이블 설정
        # 기존 값 제거
        for item in treeview.get_children():
            treeview.delete(item)

        # 새로운 값 추가
        for index, row in self.Sale_df.iterrows():
            treeview.insert('', 'end', text='', value=(row['SaleDate'], row['SaleName']))

        #msg.showinfo('새로고침 완료', '새로고침이 완료되었습니다!')
