def print_multiplication_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(str(i) + "*" + str(j) + "=" + str(i * j), end="\t")
        print()



def print_mutiplication_table_():
    for i in range(9, 0, -1):
        for j in range(i, 0, -1):
            print(str(i) + "*" + str(j) + "=" + str(i * j), end="\t")
        print()