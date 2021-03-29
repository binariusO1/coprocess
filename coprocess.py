NUMBERS = "coprocess_input.txt"

SUM_ARRAY = []
VALUES_ARRAY = []
BINARY_ARRAY = []
BINARY_STR = ""


def binary():
    print("def binary()")
    global BINARY_STR
    for i in range(len(VALUES_ARRAY)):
        BINARY_ARRAY.append(0)
        BINARY_STR += "0"


def count():
    print("def count()")
    global BINARY_STR

    n = 2
    sumOfsum = 0
    binary_num = ""

    for i in range(len(VALUES_ARRAY)):
        n *= 2;
        #print(n)
    print(n)
    for i in range(1, n, 1):

        if (i == 100000000):
            print("7 100 000 000")
        if (i == 1000000000):
            print("8 1 000 000 000")
        sum = 0
        # convert i to 8-bit binary number
        binary_num = "{0:{fill}32b}".format(i, fill='0')

        for j in range(len(VALUES_ARRAY) - 1, 0, -1):
            sum = sum + (int(binary_num[j])*int(VALUES_ARRAY[j]))

        for k in SUM_ARRAY:
            if sum == k:
                print("For sum: ", k)
                for j in range(len(VALUES_ARRAY)-1, 0, -1):
                    #print(BINARY_STR[j])
                    if int(binary_num[j])*int(VALUES_ARRAY[j]):
                        print(VALUES_ARRAY[j])
            #k = 0
                sumOfsum = sumOfsum + 1

                if sumOfsum == len(SUM_ARRAY):
                    print("end count()")
                    return ""





def read(file_name):
    print("def read()")
    file = open(file_name, "r", encoding="utf8")

    _isspace = False
    lines = file.readlines()

    for value in lines:
        value = value[:-1]
        if len(value) < 1 and not _isspace:
            _isspace = True
            continue

        if not _isspace:
            SUM_ARRAY.append(value)
            #print(value)
        else:
            VALUES_ARRAY.append(value)
            #print(value)

    file.close()


read(NUMBERS)
binary()
count()