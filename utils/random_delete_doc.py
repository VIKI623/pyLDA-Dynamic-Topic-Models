# coding: utf-8

import csv, time
import numpy as np

if __name__ == "__main__":
    # Read doc data
    total_count = 1.0/800.0 #保留比率
    doc_list = [[] for i in range(10)]
    with open("doc_data.csv", "r") as csvfile_in:
        csv_reader = csv.reader(csvfile_in)
        csv_header = next(csv_reader)
        index = 0
        now_year = 2006
        for row in csv_reader:
            year_time = int(row[1][0:4])
            if year_time != now_year:
                now_year = year_time
                index += 1
            doc_list[index].append(row)
    
    _time = int(time.time())
    _out_path = "data_" + str(_time) + ".csv"
    with open(_out_path, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id","date","abstract"])
        for i in range(0, 10):
            doc_count = len(doc_list[i])
            size = int(total_count * doc_count)
            delete_item = sorted(list(set(np.random.randint(0, doc_count, size))))
            size = len(delete_item)
            delete_index = 0
            for j in range(0, doc_count):
                if delete_index < size and j == delete_item[delete_index]:
                    writer.writerow(doc_list[i][j])
                    delete_index += 1

    print("Done! All data has been saved into " + _out_path + "\n")