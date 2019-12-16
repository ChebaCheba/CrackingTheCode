# Partition

Write code to partition a linked list around a value X, such that all nodes less than X come before all nodes greater than or equal to X. If X is contained within the list, the values of X only need to be after the elements less than X (see below). The partition element X can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.  
  
EXAMPLE  
  
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8