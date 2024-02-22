
                #COMPARISON BASED SORTS

            #def sort_by_length(self, lst: List[str]) -> None:
            #def selection_sort(self, lst: List[int]) -> None:
            
            
 # """
  #Sorts a list of strings by the length of each string
  #"""        
  #lst.sort(key=lambda x: len(x)) # Note we can also do lst.sort(key=len)
  #for loop when finding range with a int list
  #for i in range(len(lst)):
   # min_index = i
    #for j in range(i + 1, len(lst)):
      #update minimum index
     # if lst[j] < lst[min_index]:
      #  min_index = j
        
    # swap current index(j) with minimum element in rest of list
    #lst[min_index], lst[i] = lst[i], lst[min_index]
  
#print(sort_by_length(['hello', 'your', 'above', 'year', 'alone', 'friendly', 'crazy']))

          #BUBBLE SORT
 
#def sort(nums):
  #for i in range(len(nums)-1,0,-1):
   # for j in range(i):
    #  if nums[j]>nums[j+1]:
     #   temp = nums[j]
      #  nums[j] = nums[j+1]
       # nums[j+1] = temp 
 
 
          
#nums = [4, 6, 3, 8, 2, 10, 5, 7]
#sort(nums)
#-------------------------------------------------------

#def sorts(numbers):
  #for s in range(len(numbers)-1,0,-1):
   # for p in range(s):
    #  if numbers[p]>numbers[p+1]:
     #   temp = numbers[p]
      #  numbers[p] = numbers[p+1]
       # numbers[p+1] = temp
  
#numbers = [12, 3, 1, 111, 36, 87, 78, 50, 90, 83]
#sorts(numbers)

#print(nums)
#print(numbers)

          #HEIGHT CHECKER
          
#def heightChecker(heights):
  #h1 = sorted(heights)
  #sum = 0
  #for i in range(len(heights)):
   # if h1[i] != heights[i]:
    #  sum += 1
  #return sum
  
  #for i in range(len(heights)-1,0,-1):
   # for j in range(i):
    #  if heights[j]<= heights[j+1]:
     #   temp = heights[j]
      #  heights[j] = heights[j+1]
       # heights[j+1] = temp
      #return heights[j]
        
          
          
#heights = [1, 1, 4, 2, 1, 3]
#heightChecker(heights)
#print(heightChecker(heights))

def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = head, head.next
        
        while cur:
            if cur.val >= prev.val:
                prev, cur = cur, cur.next
                continue
                
            tmp = dummy
            while cur.val > tmp.next.val:
                tmp = tmp.next
                
            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next
        return dummy.next


          

