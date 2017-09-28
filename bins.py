import binpacking
from DynamicProgrammingAlgorithm import ProcessSizesIntoDictionary

def bulk_to_array(bulk):
    output = []
    for key in bulk:
        output += bulk[key]*[int(key)]
    return output

def toBins(dictionary,max_length):
    arr = bulk_to_array(dictionary)
    bins = binpacking.to_constant_volume(arr,max_length)
    return bins

print(toBins({'3':10,'2':10,'5':10}, 10))
