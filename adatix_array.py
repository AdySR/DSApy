from array import array
from operator import indexOf
class Adatix_Array:
    def array_sort(array_unsorted):
        for i in range(len(array_unsorted)):
            for j in range(i+1,len(array_unsorted)):
                if array_unsorted[i]>array_unsorted[j]:
                    array_unsorted[i],array_unsorted[j] =array_unsorted[j], array_unsorted[i]

        return array_unsorted



# array =[13,11,33,5,33,5,211,52,433,5,3,5,7,8,5,4,33,3]
# print(array_sort(array))