#MCU_Vending_Machine
#Client
import socket
import pandas as pd

import tkinter.messagebox as msg
from Item_DB import*

'''
#서버에 연걸
server_ip = 'localhost' #서버 ip
server_port = 9090      #포트번호

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #소켓 객체 생성
socket.connect((server_ip, server_port))    #연결
'''

#물품수량 확인
#컨트롤 클래스
class Inventory_System():
    def __init__(self):
        self.ItemDB = Item_DB() #Item_DB객체 생성

    #CSV파일 내의 제품목록들 테이블에 출력
    def repaint(self,treeview):
        #기존 값 제거
        for item in treeview.get_children() :
            treeview.delete(item)

        #새로운 값 추가
        for index, row in self.ItemDB.get_df().iterrows() :
            treeview.insert('','end',text='',value=(row['ItemName'],row['ItemCount'],row['ItemPrice']))

    def modify(self,focus_item,treeview):
        item_name = treeview.item(focus_item).get('values')[0]
        print(item_name)
