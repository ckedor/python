import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  # and return the timestamp YYYY-MM-DD
  with open(filename, "w") as file:
    pass
  timestamp = os.path.getmtime(filename)
  datetime_string = datetime.datetime.fromtimestamp(timestamp)
  ano = datetime_string.year
  mes = datetime_string.month
  dia = datetime_string.day
  return ("{:04.0f}-{:02.0f}-{:02.0f}".format(ano, mes, dia))

def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  os.chdir("..")
  return os.getcwd()

print(parent_directory())