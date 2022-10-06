import csv

input_file_name = "random_name.csv"
output_file_name = "sorted_name.csv"

# initializing the titles and rows list
fields = []
rows = []


def take_second(elem):
    return elem[1]
 
# reading csv file
with open(input_file_name, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

#sort by first name then last name
rows.sort()
rows.sort(key=take_second)


with open(output_file_name, 'w', encoding='UTF8', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # write the header
    writer.writerow(fields)

    # write the data
    writer.writerows(rows)

    