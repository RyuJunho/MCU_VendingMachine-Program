# MCU_Vending_Machine
# Client


from Inventory_left_UI import *
from Sale_UI import*
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


# 바운더리 클래스
class Main():
    def __init__(self):
        self.action = Sale_System()

        '''
        #서버에 연걸
        server_ip = 'localhost' #서버 ip
        server_port = 9090      #포트번호

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #소켓 객체 생성
        client_socket.connect((server_ip, server_port))    #연결
        '''


        self.window = tk.Tk()
        self.window.title('자판기 관리 UI')
        self.window.geometry('500x500')
        self.window.resizable(False, False)

        # 화면 배경화면을 Label로 설정
        self.main_bg = tk.Label(self.window)
        img_tk = ImageTk.PhotoImage(Image.open("Image/bonobono.jpg").resize((500, 500)))
        self.main_bg.configure(image=img_tk)
        self.main_bg.image = img_tk
        self.main_bg.place(x=-2, y=-2)

        # 메인화면 레이블
        font = tkinter.font.Font(family='궁서', size=20, underline=True, slant='italic')
        self.main_label = tk.Label(self.window, text='\u2665 자판기 관리 시스템 \u2665', font=font, fg='red')
        self.main_label.pack(pady=30)

        # 버튼 이미지
        btn_img = ImageTk.PhotoImage(Image.open("Image/button_bg.jpg").resize((100, 50)))

        # 재고관리 버튼
        self.Inventory_btn = tk.Button(self.window, text='재고관리', font=('굴림', 12, 'bold'),
                                       command=lambda: self.Inventory())
        self.Inventory_btn.pack(ipadx=30, ipady=10, pady=30)
        self.Inventory_btn.configure(image=btn_img, width=30, height=10)
        self.Inventory_btn.bg = btn_img
        self.Inventory_btn['compound'] = 'center'  # 그림위에 글씨 출력

        # 거래내역확인 버튼
        self.Transaction_btn = tk.Button(self.window, text='거래내역', font=("맑은고딕", 12, 'bold'),
                                         command= lambda : self.Sale())
        self.Transaction_btn.pack(ipadx=30, ipady=10, pady=30)
        self.Transaction_btn.configure(image=btn_img, width=30, height=10)
        self.Transaction_btn.image = btn_img
        self.Transaction_btn['compound'] = 'center'  # 그림위에 글씨 출력

        # 종료 버튼
        self.Exit_btn = tk.Button(self.window, text='종료', font=("맑은고딕", 12, 'bold'),
                                  command=lambda: self.socket_close())
        self.Exit_btn.pack(ipadx=30, ipady=10, pady=30)
        self.Exit_btn.configure(image=btn_img, text='종료', width=30, height=10)
        self.Exit_btn.image = btn_img
        self.Exit_btn['compound'] = 'center'  # 그림위에 글씨 출력


    #재고관리
    def Inventory(self):
        Inventory = Inventory_left_UI() #재고관리 UI 객체 생성
        Inventory.mainloop()

    #거래내역
    def Sale(self):
        Sale = Sale_UI()  #거래내역 UI 객체 생성
        Sale.mainloop()

    #종료
    def exit(self):
        self.quit()
        self.destroy()

    def mainloop(self):
        self.window.mainloop()


    def socket_close(self):
        print('소켓 닫기')
        self.window.destroy()
        #self.client_socket_close()

    def socket_rev(self):
        while True :
            data = self.client_socket.recv(1024)
            print(repr(data.decode()))
            data_list = repr(data.decode()).split(',')

            if data_list[0] == '거래내역' :
                self.action.repaint(data_list[1])


app = Main()
app.mainloop()
