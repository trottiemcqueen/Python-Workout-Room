import sys
#from load import load_numbers

#numbers = load_numbers(sys.argv[1])

def quicksort(values):
  if len(values) <= 1:  #BASECASE FOR RECURSION
    return values
  
  pivot = values[0]
  less_than_pivot = []
  greater_than_pivot = []
  
  for value in values[1:]:
    if value <= pivot:
      less_than_pivot.append(value)
    else:
      greater_than_pivot.append(value)
  return quicksort(less_than_pivot) + [pivot] + (greater_than_pivot)
 
  
  ###############################################
  
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
    
    
  
  


