def extract(file_num):
    file_num = str(file_num)
    if len(file_num)<5:
        file_num = "0"*(5-len(file_num))+file_num
    file = open("PR_"+file_num+".PRX")
    arr = []
    for item in file:
        arr.append(item.replace("\n", ""))

    PRX0 = [] #0 is num not letter
    index0 = arr.index(" PRX1")
    for i in range(index0):
        PRX0.append(int(arr[i][5:arr[i].find(":")].replace(" ", "")))


    index1 = arr.index(" PRX2")
    temp = "".join(arr[index0+1:index1]).split(" ")
    PRX1 = []
    dictionary = {}
    for item in temp:
        if item != "":
            if item in PRX1:
                dictionary[item] += 1
            else:
                dictionary[item] = 1
            PRX1.append(int(item))
            


    index2 = arr.index(" PRX3")
    index3 = arr.index(" PRX4")
    temp = "".join(arr[index2+1:index3]).split(" ")
    PRX3 = []
    for item in temp:
        if item != "":
            PRX3.append(int(item))

    temp = "".join(arr[index3+1:]).split(" ")
    PRX4 = []
    for item in temp:
        if item != "":
            PRX4.append(int(item))

    return [PRX0,PRX1,dictionary,PRX3,PRX4] #PRX2 is just and array of ones


