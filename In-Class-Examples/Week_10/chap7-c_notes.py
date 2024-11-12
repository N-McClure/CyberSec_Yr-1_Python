# Searching:
#===========#

# In Python: in / not in, index(), count()
# - Linear Search: go through the list from start to end.
# - Binary Search: used for sorted lists.
# - custom search: 

# Example: Write a search function,taking a list and a list from the user, returns a new list of the Indexes of the Key.
#   Inputed List = [1,2, 2, 3, 2, 2, 4, 2, 5, 2, 6]

def mySearch(lst, key):
    result = []
    for i in range(len(lst)):
        if lst[i] == key:
            result.append(i)
    return result

print(mySearch([1,2, 2, 3, 2, 2, 4, 2, 5, 2, 6], 2))

# Sorting:
#=========#

# In Python: list.sort() method
# - what re-order items in a list in ascending or descending order.
# - Algorithms: bubble sort, selection sort, heap sort, insertion sort, merge sort, quick sort...etc

# Example: Bubble Sort
def bubbleSort(lst):
    n = len(lst)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                swapped = True
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if not swapped:
            return

print(bubbleSort([1,2, 2, 3, 2, 2, 4, 2, 5, 2, 6]))

# 2-D Lists:
#==========#

# In Python: 
# - what: a list where each element is a list.

def twoDLists():
    lst = [1,2,3,4,5,6] # 1-D List.
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]] # 3x3 Matrix...aka: 2-D List.
    # Access a matrix via [Row][Col].
    
    print(matrix[0][2], matrix[1][2], matrix[2][2])
    
    # Loop: outer loop for rows, inner for columns.
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(f'[{r}][{c}] = {matrix[r][c]}\t', end=' ')
            
twoDLists()