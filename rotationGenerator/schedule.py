import numpy as np
import pandas as pd
import openpyxl as xl

class schedule():

    def __init__(self, wb):
        self.scheduleWb = xl.load_workbook(filename = wb)
        self.scheduleSheet = self.scheduleWb["Pool Attendants"]
        self.employeeRows = {
            "7": "Chynna",
            "8": "Jared",
            "10": "Gabrielle",
            "11": "Cheyenne",
            "12": "Ricardo",
            "13": "Gillian",
            "14": "Shawn",
            "15": "EJ",
            "16": "1Stephanie",
            "17": "Asheton",
            "18": "David",
            "19": "Tiffany",
            "20": "Jacob",
            "21": "Josabet",
            "22": "Cassidy",
            "23": "Haley",
        }
    def test(self):
        for x in self.employeeRows:
            print(x + " " + self.employeeRows[x])
