def linear_search(lst, to_find):
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
  for i in range(len(lst)):
    if lst[i] == to_find:
      return i
  return -1
