import csv

def get_data():
    data_array = []

    with open('IDV.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_array.append(row)

    datas = []

    for row in data_array:
        data_dict = {
            "survivor": row[0],
            "counter": row[1],
            "hunter": row[2]
        }
        datas.append(data_dict)

    # Print the users list
    # print(data_array)
    #print(datas)

    # Print the data array
    
    return datas[1:]
