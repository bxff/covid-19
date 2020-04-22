import os

def getOrderedFileNames(directory:str):
    # Getting all file names
    files_list = os.listdir(directory)
    
    # Automated sorting(not fully affective, but required)
    files_list.sort()

    files_ordered_list = []
    # Clearing the first data(`.DONT_DELETE_THIS_FILE`)
    del(files_list[0])

    # Ordering the data manualy
    for i in range(1,13):  # 1..12
        for file_name in files_list:
            if int(file_name[9:10]) == i:
                files_ordered_list.append(file_name)
    
    return files_ordered_list