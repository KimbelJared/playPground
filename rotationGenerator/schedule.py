import numpy as np
import pandas as pd
import openpyxl as xl

class schedule():

    def __init__(self, wb):
        self.scheduleWb = xl.load_workbook(filename = wb)
        self.scheduleSheet = self.scheduleWb["Pool Attendants"]
        self.employeeRows = {
            "Chynna": "7",
            "Jared": "8",
            "Gabrielle": "10",
            "Cheyenne": "11",
            "Ricardo": "12",
            "Gillian": "13",
            "Shawn": "14",
            "EJ": "15",
            "Stephanie": "16",
            "Asheton": "17",
            "David": "18",
            "Tiffany": "19",
            "Jacob": "20",
            "Josabet": "21",
            "Cassidy": "22",
            "Haley": "23",
        }
    def test(self):
        for x in self.employeeRows:
            print(x + " " + self.employeeRows[x])
