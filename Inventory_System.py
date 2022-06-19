# MCU_Vending_Machine
# Client
import socket
import pandas as pd

import tkinter.messagebox as msg
from Item_DB import *

'''
#서버에 연걸
server_ip = 'localhost' #서버 ip
server_port = 9090      #포트번호

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #소켓 객체 생성
socket.connect((server_ip, server_port))    #연결
'''


# 물품수량 확인
# 컨트롤 클래스
class Inventory_System():
    def __init__(self):
        self.ItemDB = Item_DB()  # Item_DB객체 생성
        self.Item_df = self.ItemDB.get_df()

    # CSV파일 내의 제품목록들 테이블에 출력
    def repaint(self, treeview):
        self.ItemDB = Item_DB()  # Item_DB객체 생성
        self.Item_df = self.ItemDB.get_df()

        # 기존 값 제거
        for item in treeview.get_children():
            treeview.delete(item)

        # 새로운 값 추가
        for index, row in self.Item_df.iterrows():
            treeview.insert('', 'end', text='', value=(row['ItemName'], row['ItemCount'], row['ItemPrice']))

        #msg.showinfo('새로고침 완료', '새로고침이 완료되었습니다!')

    #선택한 제품에 따라 프레임 정보 변경
    def frame_modify(self, focus_item, treeview, name_label, count_entry):
        item_name = treeview.item(focus_item).get('values')[0]
        name_label.configure(text=f'{item_name}')
        count_entry.delete(0, 'end')


    #제품의 수량 변경
    def count_modify(self,name_label,count_entry):
        self.ItemDB = Item_DB()  # Item_DB객체 생성
        self.Item_df = self.ItemDB.get_df()
        self.Item_df.loc[name_label['text'],'ItemCount'] = count_entry.get()
        print(f'{count_entry.get()}으로 값 변경 완료')
        print(self.Item_df.loc[name_label['text'],'ItemCount'])
        #msg.showinfo('수량변경 완료', '수량변경이 완료되었습니다!')

        #파일 저장
        self.Item_df.to_csv("csv/Item.csv",index=False,encoding='cp949')

