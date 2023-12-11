
import json
import csv
import sys
from datetime import datetime
from dotenv import load_dotenv
import os

from openpyxl.workbook import Workbook


# is a super(parent) class for all other Classes
class CommonFunctions:
       env_path = "env/.env"
        # relative_env_path = "../../"
       def __init__(self,relative_env_path):

         load_dotenv(relative_env_path + self.env_path)
         #print(os.getcwd())
         #self.bva_gitlab_token = os.getenv("BVA_GITLAB_TOKEN")
         #self.user_name= os.getenv("USER_NAME")
         #self.password= os.getenv("USER_PW")
         #print (os.getenv("RELATIVE_PATH"))
         #self.relative_path = os.getenv("RELATIVE_PATH")
         #self.config_path = relative_env_path + os.getenv("CONFIG_PATH")
         #self.output_path = relative_env_path + os.getenv("OUTPUT_PATH")
         #self.config_file_name = os.getenv("CONFIG_FILE_NAME")

       #---------------------------------------
       def returnTheseData(self, success, message, data):
           return {
               "success": success,
               "message": message,
               "data"   : data #the actual data to be returned
           }
       #---------------------------------------

       #Mode can be: "w" "r" "wb" "ab" "rb"
       def openFileForAMode(self, file_name,mode):
           try:
               file_out = open(file_name, mode)
           except FileNotFoundError as fnf_error:
               print( fnf_error )
               sys.exit(1)
           return self.returnTheseData(True, "ok", file_out)
       #---------------------------------------
       #---------------------------------------
       def openFileForWriting(self, file_name):
           try:
               file_out = open(file_name, "w",newline='', encoding="utf8")
           except FileNotFoundError as fnf_error:
               print( fnf_error )
               sys.exit(1)
           return self.returnTheseData(True, "ok", file_out)
       #---------------------------------------
       def openFileForAppend(self, file_name):
           try:
               file_out = open(file_name, "a",newline='', encoding="utf8")
           except FileNotFoundError as fnf_error:
               print( fnf_error )
               sys.exit(1)
           return self.returnTheseData(True, "ok", file_out)
       #---------------------------------------
       def openFileForReadOnly(self, file_name):
           try:
               file_in = open(file_name, "r",newline='' ,encoding="utf8")
           except FileNotFoundError as fnf_error:
               print(fnf_error )
               sys.exit(1)
           return self.returnTheseData(True, "ok", file_in)
       #---------------------------------------
       #---------------------------------------
       def getSpaltePositionInThisRow(self,splate_header,row):
           postion_found = -1
           if (len(row) == 0 or len(splate_header) == 0):
               return postion_found
           position = 0
           for splate_header_value in row:
               if splate_header_value == splate_header:
                  postion_found = position
                  break
               position +=1
           return postion_found

       def getHeaderPositionInRow(self,header_tag,row):
           return self.getSpaltePositionInThisRow(header_tag,row)
               #---------------------------------------
       def convertCSVIntoJsonFile(self, file_name_source, file_name_destination):
            data_returned = self.openFileForReadOnly(file_name_source)
            file_in = data_returned.get("data")
            data_returned = self.openFileForWriting(file_name_destination)
            file_out = data_returned.get("data")
            jsonArray = []
            csvReader = csv.DictReader(file_in,delimiter=',')
            for row in csvReader:
                jsonArray.append(row)
            jsonString = json.dumps(jsonArray, indent=4)
            file_out.write(jsonString)
       #---------------------------------------
       #---------------------------------------
       def readAnyJsonFileContent(self, file_name):
         data_returned = self.openFileForReadOnly(file_name)
         file_in = data_returned.get("data")
         config_content = ""
         try:
           config_content= json.load(file_in)
           return self.returnTheseData( True, "ok", config_content)
         except :
           print( "Json file: " + file_name + ", content is not correctly formatted:" + config_content )
           sys.exit(1)
#---------------------------------------
       def checkIfValueIsIncludedInArray(self,row,data_Array):
           found = False
           if (len(row) == 0 or len(str(data_Array)) == 0):
               return found
           for value in row:
               for data in data_Array:
                   if value == data:
                       found = True
                       break
           return found


       def castDateToMonthYear(self, date_value):
           #print(date_value +"-")
           if len(date_value) == 0:
               return None
           try:
             new_date=datetime.strptime(str(date_value),'%d.%m.%Y %H:%M ').date()
             return new_date.strftime("%m.%Y")
           except:
               print("Wrong Date format:" + date_value)
               return None


       def is_a_valid_year(self,year):
           current_year = datetime.now().year
           if year and year.isdigit():
             if int(year) >= self.project_start_year and int(year) <= int(current_year):
                 return int(year)  #return an integer
           return -1

       def convertCSVIntoExcel(self,filename):
          wb = Workbook()
          ws = wb.active
          with open(filename, 'r',newline='',encoding="utf8") as f:
             for row in csv.reader(f):
              ws.append(row)

          wb.save(filename[:-7]+ ".xlsx")
       #def convertCSVIntoExcel(self,filename):

          # import pandas as pd
          # try:
             #print(os.getcwd())
            # df_new = pd.read_csv(filename)
             # saving xlsx file
             #print(df_new)
             #print(filename)
          # except:
            #   print("coudln't read: " + filename )
          # try:

           #  GFG = pd.ExcelWriter(filename[:-7]+ ".xlsx")
            # df_new.to_excel(GFG, index=False)
            # GFG.save()
           #except Exception as e:
            #  print( str(e) +"coudln't convert: " + filename + ".xlsx")
