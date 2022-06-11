#MCU_Vending_Machine
#Client
import socket
import pandas as pd
import tkinter as tk
from tkinter import ttk
import tkinter.font


'''
#서버에 연걸
server_ip = 'localhost' #서버 ip
server_port = 9090      #포트번호

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #소켓 객체 생성
socket.connect((server_ip, server_port))    #연결
'''

#물품수량 확인

class Inventory_right_UI(tk.Tk):
    def __init__(self):

        self.window = tk.Tk()
        self.window.title('재고관리 UI')
        self.window.geometry('500x500')
        self.window.resizable(False, False)



    
