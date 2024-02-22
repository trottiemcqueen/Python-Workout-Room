import sys

def quicksorts(values):
    if len(values) <= 1:
      return values
    
    less_than_pivot = []
    greater_than_pivot = []
    pivot = [0]
    
    for value in values[1:]:
      if value <= pivot:
        less_than_pivot.append(value)
      else:
        greater_than_pivot.append(value)
    return quicksorts(less_than_pivot) + [pivot] + (greater_than_pivot)
    
    sorted_numbers = quicksorts(numbers)
    print(sorted_numbers)
    
    
#AFTER LIST IS SORTED - NOW CONVERT SORTED LIST INTO A VAR AND PRINT A NEW FILE TO NOW 
#RUN THE SEARCH OF CHOICE
sorted_names = quicksorts#'names' belong to a import load file that's not present
for n in sorted_names:
  print(n)    
  
  #PERFORM A FILE REDIRECT IN THE TERMINAL - TO WHERE WE WANT THE FILE TO GO
    #quicksort.py folderpath of file(names/unsorted.txt) > names/sorted.txt
    
    #LINEAR SEARCH - now can use names/sorted.txt for any type of search
    
#def index_of_item(collection, target):
 # for i in range(0, len(collection)):
  #  if target == collection[i]:
   #   return i
  #return None

#for n in search_names: #file name
 # index = index_of_item(names, n)
  #print(index)
  