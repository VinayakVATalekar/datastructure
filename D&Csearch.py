def bsearch(list, val):
   list_size = len(list) - 1
   idx0 = 0
   idxn = list_size
# Find the middle most value
   while idx0 <= idxn:
      midval = (idx0 + idxn)// 2
      if list[midval] == val:
         return midval
# Compare the value the middle most value
   if val > list[midval]:
      idx0 = midval + 1
   else:
      idxn = midval - 1
   if idx0 > idxn:
      return None
# Initialize the sorted list
list = [55,67,3,2,1,78,67]
