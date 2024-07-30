# METHOD 1: MY SOLUTION
# def check_monitoric_increasing_arr(array, n):
#     for i in range(n - 1):
#         if array[i] - array[i + 1] > 0:
#             return False
#     return True


# def check_monitoric_decreasing_arr(array, n):
#     for i in range(n - 1):
#         if array[i] - array[i + 1] < 0:
#             return False
#     return True


# def monotonic_array(array):
#     n = len(array)
#     if n <= 1:
#         return True
#     return check_monitoric_increasing_arr(array, n) or check_monitoric_decreasing_arr(
#         array, n
#     )


# METHOD 2
def monotonic_array(array):
    n = len(array)
    if n < 2:
        return True

    first = array[0]
    last = array[n - 1]

    if first > last:
        for i in range(n - 1):
            if array[i] < array[i + 1]:
                return False
    elif first < last:
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                return False
    else:
        for i in range(n - 1):
            if array[i] != first:
                return False
    return True
