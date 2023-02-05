import pandas as pd
from datetime import datetime

column_names = ["Item","Quantity","Unit","Expiration Date","Status","Expired"]
class user_data(object):
    def __init__(self):
        self.inventory = pd.DataFrame(columns=column_names)

    # code to add new item to the dataframe
    def add_data(self, item, quantity, unit, exp_date):
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
                            "Unit": [unit if unit != None else "unit"],
                            "Expiration Date": [exp_date],
                            "Status": [0], # we will update this when we call .update()
                            "Expired": [False]
                            })
        self.inventory = self.inventory.append(tmp, ignore_index=True)
        self.update()

    def update(self):
        # sort the dataframe by exp_date (use date_time module)
        self.inventory['Expiration Date'] = pd.to_datetime(self.inventory['Expiration Date'], dayfirst=True)
        self.inventory.sort_values(by='Expiration Date', inplace = True)

        # update item expiry status
        current_date = datetime.today()
        self.inventory["Expired"] = current_date > self.inventory["Expiration Date"]
        self.inventory["Status"] = (self.inventory["Expiration Date"] - current_date).round("D")

    def del_data(self, item):
        self.inventory.drop(self.inventory[self.inventory["Item"]==item].index, inplace=True)

    def mod_data(self, item, column, new_data):
        # modify existing data, specify item name, column of data to modify, and the new data
        self.inventory.loc[self.inventory["Item"]==item, column] = new_data
        self.update()

    def use_quantity(self, item, quantity_used):
        quantity = self.inventory.loc[self.inventory["Item"]==item]["Quantity"].values
        new_quantity = quantity-quantity_used
        if new_quantity > 0:
            self.mod_data(item, "Quantity", new_quantity)
        else:
            self.del_data(item)
    
    def top_items(self, n = None):
        output = self.inventory[self.inventory["Expired"] == False]
        if n:
            return list(output.head(n)["Item"].values)
        return list(output["Item"].values)
    
    # returns a json of items
    def items(self):
        output = self.inventory
        output["Expiration Date"] = output["Expiration Date"].astype("string")
        output["Status"] = output["Status"].astype("string")
        return output.to_json(orient="table", index=False)

    # take json input, update the dataframe and return a list of top items for recipes
    def parse_input(self, data, n=8):
        [item, quantity, unit, exp_date] = [data[key] for key in ["Item","Quantity","Unit","Expiration Date"]]
        self.add_data(item, quantity, unit, exp_date)
        return self.top_items(n)

# a=user_data()
# print(a.parse_input({"Item":"apple","Quantity":6,"Unit":"kg","Expiration Date":"06-12-2023"}))
# print(a.inventory)
# print(a.top_items(4))