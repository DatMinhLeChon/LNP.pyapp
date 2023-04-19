
def viewModelTable(public_number_val):
    temp_list = []
    for index in range(1, public_number_val):
        temp_list.append(''.join(['x',str(index)]))
    print(temp_list)


if __name__ =="__main__":
    viewModelTable(10)
#python test.py