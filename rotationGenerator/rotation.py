import numpy as np
import pandas as pd
import openpyxl as xl

class rotation():

    def __init__(self, wb):
        self.rotationWb = xl.load_workbook(filename = wb)
        self.rotationSheet = self.rotationWb["Sheet1"]

    def test(self):
        print("works")
