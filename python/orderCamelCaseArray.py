from typing import List


def orderCamelCase(arr: List[int]) -> List[int]:
    left = 0
    right = len(arr) - 1
    arr.sort()
    result: List[int] = []

    while left <= right:
        if left == right:
            result.append(arr[left])
        else:
            result.append(arr[left])
            result.append(arr[right])
        left += 1
        right -= 1

    return result


print(orderCamelCase([5, 9, 1, 4, 10]))  # --> [1, 10, 4, 9, 5]
