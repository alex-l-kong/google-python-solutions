#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  # +++your code here+++

  # # the "append to a new list" version
  # # this requires checking if the len of nums is 0 first
  # # so just return immediately if that is the case
  # # since this case will cause a seg fault in the loop
  # if len(nums) == 0:
  #   return nums


  # # the list containing the returned version
  # new_list = []

  # # for each element excluding the last
  # # check if the next element is equal to the current element looked at
  # # if so, don't add it
  # # this scheme guarantees that only the last element in a series of adjacent elements is added
  # for index in range(0, len(nums) - 1):
  #   if nums[index] != nums[index + 1]:
  #     new_list.append(nums[index])

  # # always append the last element under this scheme
  # new_list.append(nums[len(nums) - 1])


  # version without a temporary list, preferred
  # again, need to test if list is empty at first
  # if so, just return
  if len(nums) == 0:
    return nums

  # keep track of where you are in list
  index = 0

  # we can keep this while loop going until we hit the last element in nums
  while index < len(nums) - 1:

    # if adjacent elements are found, simply use list slicing to create new list without element in question
    # you must decrement the index to account for the fact the list size has decreased by 1
    if nums[index] == nums[index + 1]:
      nums = nums[:index] + nums[index + 1:]
      index -= 1

    # in any case, move on to the next element
    index += 1

  return nums


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  # +++your code here+++

  # the return list
  ret_list = []

  # we will iterate over each element in each list, so we need indices to each one
  ind1 = 0
  ind2 = 0

  # the logic is that we will compare the elements the indices in each list are currently pointing at
  # if list 1's element is smaller, then add that to ret_list, and increemnt ind1
  # same goes for list 2
  # if the elements in list 1 and list 2 are the same, then add them both and increment both counters
  while ind1 < len(list1):
    if ind2 == len(list2):
      break

    if list1[ind1] < list2[ind2]:
      ret_list.append(list1[ind1])
      ind1 += 1
    elif list2[ind2] < list1[ind1]:
      ret_list.append(list2[ind2])
      ind2 += 1
    else:
      ret_list.append(list1[ind1])
      ret_list.append(list2[ind2])
      ind1 += 1
      ind2 += 1

  # at this point it is possible that list1 and list2 still contain elements not added to ret_list
  # so add them based on the index position
  # it's OK if both indices point to an element outside the array (happens if the lists were equal length)
  # list slicing will just return an empty list in that case
  return ret_list + list1[ind1:] if ind1 < len(list1) else ret_list + list2[ind2:]

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print('remove_adjacent')
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  # print
  print('linear_merge')
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
