def get_cats_info(path:str):
    try:
        with open (path, "r", encoding="utf-8") as f:
            all_data = f.read().splitlines()

        cats_dictionary = []
        data_error_counter = 0
        for row in all_data:
            splitted_row = row.split(",")
            if len(splitted_row) ==3:
                cat_record = {"id": splitted_row[0], "name": splitted_row[1], "age": splitted_row[2]}
                cats_dictionary.append(cat_record)
            else:
                data_error_counter +=1
        if data_error_counter > 0:
                print(f'File records are processed with {data_error_counter} error(s) that are excluded from result. Please,check the soucre file \n')
        else:
            print('Records are processed successfully \n')

        return cats_dictionary
    
    except FileNotFoundError:
        print(f"Can't find file for mentioned path -> {path}")
        return []
    except Exception as error:
        print(f"Error: {error}")
        return []


# check time
print(get_cats_info('./source_data/cats.txt'))
print(get_cats_info('./other_cats.txt'))
print(get_cats_info('./bin/trash/other_cats.txt'))