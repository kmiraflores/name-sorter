import csv
import sys

input_file_name = sys.argv[1]
output_file_name = "sorted_name.csv"

class CSVOperations:
    def __init__(self, input_file, output_file):
        self.field_names = []
        self.rows = []
        self.input_file = input_file
        self.output_file = output_file

    def set_rows_data_from_csv(self):
        # read input csv file
        with open(self.input_file, 'r') as csvfile:
        # creating a csv reader object
            csvreader = csv.reader(csvfile)
        
            # extracting field names through first row
            self.field_names = next(csvreader)
        
            # extracting each data row one by one
            for row in csvreader:
                self.rows.append(row)

    def create_output_csv(self, field_names, row_data):
        #write output csv file
        with open(self.output_file, 'w', encoding='UTF8', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # write the header
            writer.writerow(field_names)

            # write the data
            writer.writerows(row_data)

    def get_rows(self):
        return self.rows

    def get_field_names(self):
        return self.field_names


#takes the second element of array
def take_second(elem):
    return elem[1] 

def sort_names(rows = list):
    rows.sort() 
    rows.sort(key=take_second)
    return rows




### Implementations of class and methods declared above ###

csv_process = CSVOperations(input_file_name, output_file_name)
csv_process.set_rows_data_from_csv()

unsorted_rows = csv_process.get_rows()
field_names = csv_process.get_field_names()

sorted_rows = sort_names(unsorted_rows)

csv_process.create_output_csv(field_names, sorted_rows)


    