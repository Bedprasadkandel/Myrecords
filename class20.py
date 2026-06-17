# import csv
# file_path="E:\pythonbroadway\class20filedata.csv"
# with open(file_path,mode='r') as file:
#     csv_reader=csv.reader(file)
#     header=next(csv_reader)### header part hatauxa yaslay
#     for row in csv_reader:
#         print(row)

# import csv
# file_path="E:\pythonbroadway\class20filedata.csv"
# with open(file_path,mode='r') as file:
#     csv_reader=csv.reader(file) 
#     header=next(csv_reader)### header part hatauxa yaslay
#     for row in csv_reader:
#         print(row[0:3:2])


### Example data to  write to csv

# import csv
# Data=[
#     ['Alice',30,'london'],
#     ['Bob',25,'paris'],
#     ['charlie',35,'Berlin']

# ]
# file_path='output.csv'
# with open(file_path,mode='w',newline='')as file:
#     csv_writer=csv.writer(file)
#     csv_writer.writerow(['Name','Age','City'])
#     for row in Data:
#         csv_writer.writerow(row)


# with open("E:\pythonbroadway\output.csv", mode="a",newline="") as f:
#     csv_writer=csv.writer(f)
#     name=str(input("Enter the name"))
#     age=int(input("Enter the Age"))
#     city=str(input("Enter the city name"))
#     data=[]
#     data.append(name)
#     data.append(age)
#     data.append(city)
#     csv_writer.writerow(data)

# import csv
# with open("E:\pythonbroadway\output.csv", "r") as f:     
#     data=csv.DictReader(f)
#     for row in data:
#         print(row)
import csv
data=[
    {'Name':'Alice','Age':30,'City':'london'},
    {'Name':'Bob','Age':54,'City':'Butwal'},
    {'Name':'sagar','Age':69,'City':'pokhara'}
]
file_path='output.csv'
fieldnames=['Name','Age','City']

with open(file_path,mode='w',newline='') as file:
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)