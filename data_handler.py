# from sklearn import LinearRegression
import pandas as pd
import recommender
from datetime import datetime

column_names = ["Item","Quantity","Expiration Date", "Status", "Expired"]
class user_data(object):
    def __init__(self):
        self.inventory = pd.DataFrame(columns=column_names)
        # self.inventory.set_index('Item', inplace=True)

    # code to add new item to the dataframe
    def add_data(self, item, quantity, exp_date, status = "Unopened"):
        # check if repeated item name
        if item in list(self.inventory["Item"]):
            item_id = 1
            while (item+str(item_id) in list(self.inventory["Item"])):
                item_id += 1
            item+=str(item_id)
        # add item
        tmp = pd.DataFrame({
                            "Item": [item],
                            "Quantity": [quantity],
                            "Expiration Date": [exp_date],
                            "Status": [status],
                            "Expired": [False]
                            })
        self.inventory = self.inventory.append(tmp, ignore_index=True)
        self.update()

    def update(self):
        # sort the dataframe by exp_date (use date_time module)
        self.inventory['Expiration Date'] = pd.to_datetime(self.inventory['Expiration Date'])
        self.inventory.sort_values(by='Expiration Date', inplace = True)

        # update item expiry status
        current_date = datetime.today()
        self.inventory["Expired"] = current_date > self.inventory["Expiration Date"]

    def del_data(self, item):
        self.inventory.drop(self.inventory[self.inventory["Item"]==item].index, inplace=True)

    def mod_data(self, item, column, new_data):
        # modify existing data, specify item name, column of data to modify, and the new data
        self.inventory.loc[self.inventory["Item"]==item, column] = new_data

    def use_quantity(self, item, quantity_used):
        quantity = self.inventory.loc[self.inventory["Item"]==item]["Quantity"]
        new_quantity = quantity-quantity_used
        if new_quantity > 0:
            self.mod_data(item, "Quantity", new_quantity)
        else:
            self.del_data(item)
    
    def recommend(self):
        # call the recommender API code
        # input = self.inventory.head(5)["Item"].to_list()
        pass

a = user_data()
a.add_data("apple", 3, "15/11/2022", 0)
a.add_data("apple", 4, "13/8/2022", 0)
print(a.inventory)
a.del_data("apple1")
print(a.inventory)