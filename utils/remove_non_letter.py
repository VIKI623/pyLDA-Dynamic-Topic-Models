# coding: utf-8
import csv, time


if __name__ == "__main__":
    _time = int(time.time())
    _out_path = "data_" + str(_time) + ".csv"
    with open(_out_path, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id","date","abstract"])
        with open("data_1553608967.csv","r") as csvfile_in:
            csv_reader = csv.reader(csvfile_in)
            csv_header = next(csv_reader)
            for row in csv_reader:
                oldStr = row[2]
                newStr = ""
                for letter in oldStr:
                    if letter.isalpha():
                        newStr += letter
                    else:
                        newStr += " "
                words = newStr.split()
                row[2] = " ".join(words)
                writer.writerow(row)
    print("Done! All data has been saved into " + _out_path + "\n")