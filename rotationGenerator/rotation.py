import numpy as np
import pandas as pd
import openpyxl as xl

class rotation():

    def __init__(self, wb):
        self.rotationWb = xl.load_workbook(filename = wb)
        self.rotationSheet = self.rotationWb["Sheet1"]
        self.constCells = {
            "blank": "M2",
            "standE": "M3",
            "standW": "M4",
            "break": "M5",
            "roam": "M6",
            "host": "M7",
            "greet": "M8",
            "amenity": "M9",
        }

    def test(self):
        for x in self.constCells:
            print(x + " " + self.constCells[x])

    def fillBlanks(self):
        for row in range(2, 29):
            for col in range(2, 11):
                self.rotationSheet.cell(column=col, row=row, style=self.rotationSheet['M2'].style)
