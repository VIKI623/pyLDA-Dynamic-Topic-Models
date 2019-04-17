# coding: utf-8

import csv, time

if __name__ == "__main__":
    # Read doc data

    doc_dic = {}
    with open("data_1554363719.csv", "r") as csvfile_in:
        csv_reader = csv.reader(csvfile_in)
        csv_header = next(csv_reader)
        for row in csv_reader:
            year_time = row[1][0:10]
            if year_time not in doc_dic:
                doc_dic[year_time] = []
            doc_dic[year_time].append(row)
    
    _time = int(time.time())
    _out_path = "data_" + str(_time) + ".csv"
    with open(_out_path, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id","date","abstract"])
        for year in sorted(doc_dic.keys()):
            for doc_data in doc_dic[year]:
                writer.writerow(doc_data)

    print("Done! All data has been saved into " + _out_path + "\n")