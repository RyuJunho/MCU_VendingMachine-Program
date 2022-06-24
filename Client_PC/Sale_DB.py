import pandas as pd


#엔티티 클래스
class Sale_DB():
    def __init__(self):
        self.index_key = None
        df_Sale = pd.read_csv("csv/Sale.csv",encoding='CP949')
        self.df_Sale = df_Sale.set_index('SaleDate',drop=False)

    def set_index_key(self,index_key):
        self.index_key = index_key

    def get_df(self):
        return self.df_Sale

    def get_row(self):
        self.row = self.df_Sale.loc[[self.index_key],:]
        return self.row

    def get_name(self):
        name = self.df_Sale['ItemName'].loc[self.index_key]
        return name

    def get_count(self):
        count = self.df_Sale['ItemCount'].loc[self.index_key]
        return count

