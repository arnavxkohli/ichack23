# from sklearn import LinearRegression
import pandas as pd
import numpy as np
import recommender
import datetime

column_names = ["Item","Quantity","Expiration Date", "Status"]
class user_data(object):
    def __init__(self):
        self.inventory = pd.DataFrame(columns=column_names)

    def add_data(self, item, quantity, exp_date, status = 0):
        # code to add new item to the dataframe
        tmp = pd.DataFrame({
        "Item": [item],
        "Quantity": [quantity],
        "Expiration Date": [exp_date],
        "Status": [status]})

        self.inventory = self.inventory.append(tmp)

        # TODO: sort the dataframe by exp_date (use date_time module)

    def del_data(self, item, quantity, exp_date, status):
        # TODO: delete specific data from the dataframe
        pass

    def mod_data(self, column, data):
        # modify existing data
        self.inventory[column] = data
    
    def recommend(self):
        # call the recommender code, leave for now
        pass

a = user_data()
print(a.inventory)
a.add_data("apple", 3, "12.12.2022", 0)
a.add_data("pear", 4, "13.12.2022", 0)
print(a.inventory)