

# Loops through the main list and finds matching names in secondary list
# appends the requested detail to the main list
# else adds 'No record' to prevent empty lists
def add_detail_to_list(main_list,secondary_list,detail):
    for i in range(len(main_list)):
        for j in range(len(secondary_list)):
            if main_list[i][0] == secondary_list[j]['name']:
                main_list[i][1].append(secondary_list[j][detail])
        if len(main_list[i][1]) == 1:
            main_list[i][1].append('No record')


# Loops through the main list
# Finds all the pilots
# Cross references the URL with secondary list
# Pops the url and replaces it with Object ID from secondary list
# Adds main list to the desired collection
def append_list_and_add_to_collection(main_list, secondary_list, collection):
    for i in range(len(main_list)):
        for j in range(len(main_list[i]['pilots'])):
            for k in range(len(secondary_list)):
                if main_list[i]['pilots'][j] == secondary_list[k][1][1]:
                    main_list[i]['pilots'].pop(j)
                    main_list[i]['pilots'].append(secondary_list[k][1][0])
        collection.insert_one(main_list[i])