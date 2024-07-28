def check_monitoric_increasing_arr(array, n):
    for i in range(n - 1):
        if array[i] - array[i + 1] > 0:
            return False
    return True


def check_monitoric_decreasing_arr(array, n):
    for i in range(n - 1):
        if array[i] - array[i + 1] < 0:
            return False
    return True


def monotonic_array(array):
    n = len(array)
    if n <= 1:
        return True
    return check_monitoric_increasing_arr(array, n) or check_monitoric_decreasing_arr(
        array, n
    )
