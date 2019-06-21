import numpy as np
import pandas as pd
import openpyxl as xl
from schedule import schedule as sc
from rotation import rotation as rt

schedule = sc('exSchedule.xlsx')
schedule.test()

rotation = rt('template.xlsx')
rotation.test()


rotation.fillBlanks()
