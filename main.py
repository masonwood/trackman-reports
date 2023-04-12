import os
import glob
import pandas as pd

from report1 import report1
from report2 import report2
from report3 import report3
from report4 import report4
from report5 import report5
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
from report20 import report20
from report21 import report21
from report22 import report22
from report23 import report23
from report24 import report24
from report25 import report25
# from report26 import report26
from report27 import report27
from report28 import report28
from report29 import report29

data_folder = "../zCSV"

csv_files = glob.glob(os.path.join(data_folder, "*.csv"))

for csv_file in csv_files:
    data = pd.read_csv(csv_file)
    folder_name = os.path.splitext(os.path.basename(csv_file))[0]
    
    report1(data, folder_name)
    report2(data, folder_name)
    report3(data, folder_name)
    report4(data, folder_name)
    report5(data, folder_name)
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
    report20(data, folder_name)
    report21(data, folder_name)
    report22(data, folder_name)
    report23(data, folder_name)
    report24(data, folder_name)
    report25(data, folder_name)
    # report26(data, folder_name)
    report27(data, folder_name)
    report28(data, folder_name)
    report29(data, folder_name)
