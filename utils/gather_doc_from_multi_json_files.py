import json
import os
import sys
import csv
import time
from remove_html_tag import dehtml

class CustomError(Exception):
    def __init__(self,ErrorInfo):
        super().__init__(self) #初始化父类
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo

def list_all_files(rootdir):
    _files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for file_name in list:
           path = os.path.join(rootdir,file_name)
           if os.path.isdir(path):
              _files.extend(list_all_files(path))
           if os.path.isfile(path):
              _files.append(path)
    return _files

if __name__ == "__main__":
    _fs = list_all_files(sys.argv[1])
    _time = int(time.time())
    _out_path = "data_" + str(_time) + ".csv"
    with open(_out_path, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id","date","abstract"])
        for file_name in _fs:
            row_data = []
            try:
                with open(file_name, "r") as load_f:
                    load_dict = json.load(load_f)
                row_data.append(load_dict["id"])
                row_data.append(load_dict["date"])
                text = dehtml(load_dict["abstract"]["value"])
                row_data.append(text)
                writer.writerow(row_data)
            except Exception as e:
                #print("***************************************\n")
                #print("Error occured in " + file_name + ":\n" + str(e) + "")
                pass
    print("Done! All data has been saved into " + _out_path + "\n")
