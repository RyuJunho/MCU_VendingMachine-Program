import pandas as pd

class Item_DB():
    def __init__(self):
        self.index_key = None
        df_Item = pd.read_csv("csv/Item.csv",encoding='CP949')
        self.df_Item = df_Item.set_index('ItemName',drop=False)

    def set_index_key(self,index_key):
        self.index_key = index_key

    def get_df(self):
        return self.df_Item

    def get_row(self):
        self.row = self.df_Item.loc[[self.index_key],:]
        return self.row

    def get_name(self):
        name = self.df_Item['ItemName'].loc[self.index_key]
        return name

    def get_count(self):
        count = self.df_Item['ItemCount'].loc[self.index_key]
        return count

    def get_price(self):
        price = self.df_Item['ItemPrice'].loc[self.index_key]
        return price