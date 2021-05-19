from json import dumps, loads
import csv

with open("users.json", 'r') as json_file:
    data = json_file.read()
    json_data = loads(data)
    # print(json_data)
    new_json_data = []
    header = ["name", "age", "address"]
    for item in json_data:
        new_json_data.append(dict(zip(header, (item["name"], item["age"], item["address"]))))
    # for item in new_json_data:
    #     print(item)

with open('books.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    header = ['Title', 'Author', 'Height']
    book_data = []
    for item in csv_reader:
        book_data.append((dict(zip(header, (item[0], item[1], item[3])))))
    # for item in book_data:
    #     print(item)

# print(len(book_data), len(new_json_data))

if len(book_data) >= len(new_json_data):
    for i in range(0, len(new_json_data)):
        new_json_data[i]['books'] = [book_data[i]]

else:
    for i in range(0, len(book_data)):
        new_json_data[i]['books'] = [book_data[i]]
    for i in range(len(book_data), len(new_json_data)):
        new_json_data[i]['books'] = []

with open("result.json", 'w') as write_file:
    s = dumps(new_json_data, indent=2)
    write_file.write(s)
