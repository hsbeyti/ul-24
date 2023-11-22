import csv
import sys
import json

from src.common.CommonFunctions import CommonFunctions


commonFunctions = CommonFunctions("../../")
data = commonFunctions.returnTheseData(True,"okay","Hello")
print(data)
