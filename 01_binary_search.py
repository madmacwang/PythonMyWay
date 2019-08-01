# 定義二分查找 binary_search()
def binary_search(list, item):

  # low and high keep track of which part of the list you'll search in.
  # low 和 high 用於追蹤你將搜尋列表的哪個部分
  low = 0
  high = len(list) - 1 # high值等於列表長度減 1，因為 low = 0

  # While you haven't narrowed it down to one element ...
  # 只要搜尋範圍沒有縮小到只剩下一個元素
  while low <= high:

    # ... check the middle element
    # ... 搜尋列表中位於 low 和 high 中間的那個元素
    mid = (low + high) // 2
    guess = list[mid]

    # Found the item.
    # 如果找到了要搜尋的項目
    if guess == item:
      return mid

    # The guess was too high.
    # 如果大於欲搜尋的項目
    if guess > item:
      high = mid - 1

    # The guess was too low.
    # 如果小於欲搜尋的項目
    else:
      low = mid + 1

  # Item doesn't exist
  # 如果項目不在列表中
  return None

# 設定列表元素
my_list = [1, 3, 5, 7, 9]
print (binary_search(my_list, 3)) # => 1 程式搜尋結果是位於第1號位置的元素

# 'None' means nil in Python. We use to indicate that the item wasn't found.
print (binary_search(my_list, -1)) # => None 程式搜尋的結果是沒有發現欲搜尋的項目