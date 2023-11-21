# императивный
def sort_arr(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


my_arr = [1, 5, 7, 2, 10, 17, 12, 5, 6, 0]
sort_arr(my_arr)
print(my_arr)

# декларативный
my_arr = [4, 2, 1, 3]
sorted_list = sorted(my_arr)
print(sorted_list)
