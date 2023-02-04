# from sklearn import LinearRegression
import pandas as pd
import recommender
import datetime

column_names = ["Item","Quantity","Expiration Date", "Status"]
class user_data(object):
    def __init__(self):
        self.inventory = pd.DataFrame(columns=column_names)
        # self.inventory.set_index('Item', inplace=True)

    def add_data(self, item, quantity, exp_date, status = 0):
        # code to add new item to the dataframe
        tmp = pd.DataFrame({
        "Item": [item],
        "Quantity": [quantity],
        "Expiration Date": [exp_date],
        "Status": [status]})
        self.inventory = self.inventory.append(tmp, ignore_index=True)
        self.sort()

    def sort(self):
        # sort the dataframe by exp_date (use date_time module)
        self.inventory['Expiration Date'] = pd.to_datetime(self.inventory['Expiration Date'])
        self.inventory.sort_values(by='Expiration Date', inplace = True)


    def del_data(self, item, quantity, exp_date, status):
        # TODO: delete specific data from the dataframe
        pass

    def mod_data(self, item, column, new_data):
        # modify existing data, specify item name, column of data to modify, and the new data
        self.inventory.loc[self.inventory["Item"]==item, column] = new_data

    # def use_quantity(self, item, , ):

    
    def recommend(self):
        # call the recommender API code
        input = self.inventory.head(5)["Item"].to_list()


a = user_data()
a.add_data("apple", 3, "15/11/2022", 0)
a.add_data("pear", 4, "13/8/2022", 0)
print(a.inventory)
a.mod_data("apple", "Item", "cherry")
print(a.inventory)