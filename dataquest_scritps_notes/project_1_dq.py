def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice= dataset[1:]
    for row in dataset_slice:
        print(row)
        print('\n')
    if rows_and_columns:
        print('Number of row:', len(dataset))
        print('Number of columns:', len(dataset[0]))

def open_dataset(file_name, header=True):
    opened_file = open(file_name, encoding='utf8')
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    if header:
        header= data[0]
        rows= data[1:]
        return header, rows
    else:
        return data

def missimg_value(dataset):
    counter = -1
    for cel in google_data:
        counter +=1
        column= len(cel)
        if column != 13:
            print("This column:", counter, 'has missing value')


            apple_data= open_dataset('AppleStore.csv')[1]
            apple_header= open_dataset('AppleStore.csv')[0]
            google_data= open_dataset('googleplaystore.csv')[1]
            google_header=open_dataset('googleplaystore.csv')[0]

explore_data(apple_data, 0, -1, rows_and_columns=True)
explore_data(google_data, 0, -1, rows_and_columns=True)
missimg_value(apple_data)
