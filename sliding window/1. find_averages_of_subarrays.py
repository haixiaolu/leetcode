def find_average_of_subarrays(k, arr):
    result = []
    for i in range(len(arr) - k + 1):
        # find sum of next 'k' elements
        _sum = 0.0
        for j in range(i, i + k):
            _sum += arr[j]
        result.append(_sum / k)  # calculate average
    return result


def main():
    result = find_average_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size k: " + str(result))


main()