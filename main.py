import os
import inquirer
import pandas as pd

from report1 import report1
from report5 import report5
from report3 import report3
from report4 import report4
from report2 import report2
from report6 import report6
from report7 import report7
from report8 import report8
from report9 import report9
from report10 import report10
from report11 import report11
from report12 import report12
from report13 import report13
from report14 import report14
from report15 import report15
from report16 import report16
from report17 import report17
from report18 import report18
from report19 import report19

data_paths = os.listdir('../zCSV')

questions = [
  inquirer.List(
    'file_path',
    message="What file do you want to analyze?",
    choices=data_paths,
  ),
  inquirer.Text(
    'folder_name',
    message="What folder do you want to save the data to?"
  )
]

answers = inquirer.prompt(questions)

data = pd.read_csv(f"../zCSV/{answers['file_path']}")
folder_name = answers['folder_name']

report1(data, folder_name)
report5(data, folder_name)
report3(data, folder_name)
report4(data, folder_name)
report2(data, folder_name)
report6(data, folder_name)
report7(data, folder_name)
report8(data, folder_name)
report9(data, folder_name)
report10(data, folder_name)
report11(data, folder_name)
report12(data, folder_name)
report13(data, folder_name)
report14(data, folder_name)
report15(data, folder_name)
report16(data, folder_name)
report17(data, folder_name)
report18(data, folder_name)
report19(data, folder_name)