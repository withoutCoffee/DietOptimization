import json
import pandas as pd
import numpy as np
import re

class HandleSheet:

    def __init__(self,*args,**kwargs):
        """_summary_
        """        
        try:
            self._sheets_url = kwargs.get("sheet_url")
        except:
            self._sheets_url = None

    def read_sheet(self, *args, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """        
        self._sheet_id = HandleSheet.get_sheet_id(self._sheets_url)
        nutrients_url = f"https://docs.google.com/spreadsheets/d/{self._sheet_id}/gviz/tq?tqx=out:csv&sheet=nutrients"
        foods_url = f"https://docs.google.com/spreadsheets/d/{self._sheet_id}/gviz/tq?tqx=out:csv&sheet=foods"
        try:
            self._nutrients = pd.read_csv(nutrients_url)
            self._foods = pd.read_csv(foods_url)
        except:
            self._nutrients = None
            self._foods = None
        return self
        
    def get_data(self):
        """_summary_

        Returns:
            pandas dataframe: _description_
        """        
        return self._nutrients, self._foods
    def data_to_json(self):
        self._nutrients = HandleSheet.to_json(data = self._nutrients)
        self._foods = HandleSheet.to_json(data = self._foods)
        return self 

    @staticmethod
    def to_json(*args,**kwargs):
        """Convert standard sheet to json for linear model. 
        Converting string number with (,) to float.

        Returns:
            list: List with floats
        """        
        data = kwargs.get("data")
        formated_data = []
        
        for item in np.array(data):
            arr = []
            for element in item:
                try:
                    # Converte replace number with (,) to number with (.)
                    if type(element) is str and re.search("^\d$|\d+,\d+",element):
                        arr.append(float(element.replace(",",".")))
                    else:
                        arr.append(element)
                except Exception as e:
                    print(e,element)
            formated_data.append(arr)
        
        return formated_data 
    
    @staticmethod
    def get_sheet_id(url):
        sheet_id = re.findall("spreadsheets\/d/(.+)/",url)[0]
        return sheet_id

if __name__ == "__main__":
    url = "https://docs.google.com/spreadsheets/d/1gFzQr62oK6oNVfTGdutsSUFIlNUFgtLaKt7uFwLKuJs/edit#gid=0"
    hf = HandleSheet(sheet_url = url)
    nutrients, foods = hf.read_sheet().get_data()
    data = hf.read_sheet().data_to_json().get_data()
    
    #print(data)
    #print(HandleFile.get_sheet_id(url))
    
