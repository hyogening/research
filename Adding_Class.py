
import csv
from operator import contains

import outcome

#class1 <= 6000
#class2 >= 6001
#class3 >= 10001
#class4 >= 14001
#class5 >= 16001
#class6 >= 19501
#class7 >= 26001
#class8 >= 33001


with open('Train_Data.csv') as file_obj: #sample data we want to test the code on
    reader_obj = csv.reader(file_obj)

    for row in reader_obj: #now it read all the rows
        
        line = row[5] #read the 5th element of the row (which is the weight)
        only_nums = ''.join(i for i in line if i.isdigit())
        only_nums_five = only_nums[:5] #only read the first 5
        #print(type(only_nums_five))
        if "33001" in only_nums_five:
            #open up the row, after the first 4, split, add the class, close and then print
            #print(row)
            row.insert(5, "Class 8")
            #print("Class 8")
            #print(row)
        if "26001" in only_nums_five:
            #print(row)
            #print("Class 7")
            row.insert(5, "Class 7")

        if "19501" in only_nums_five:
            #print(row)
            #print("Class 6")
            row.insert(5, "Class 6")
        if "16001" in only_nums_five:
            #print(row)
            #print("Class 5")
            row.insert(5, "Class 5")
        if "14001" in only_nums_five:
            #print(row)
            #print("Class 4")
            row.insert(5, "Class 4")
        if "10001" in only_nums_five:
            #print(row)
            #print("Class 3")
            row.insert(5, "Class 3")
        if "6001" in only_nums_five:
            #print(row)
            #print("Class 2")
            row.insert(5, "Class 2")

        #figure out how to check class 1
        #if "6000" in only_nums_five:
            #print("Class 2")        
        #print(row)
        row_list = row
        print(row_list)

outfile = open('Train_Answer.csv', 'w',)
write_outfile = csv.writer(outfile)
write_outfile.writerows(row_list)
