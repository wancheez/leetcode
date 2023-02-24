def merge_sort(to_sort: list[int]) -> list[int]:
    length = len(to_sort)
    if length == 1:
        return to_sort

    sorted_list = merge(
        merge_sort(to_sort[:length // 2]),
        merge_sort(to_sort[length // 2:]),
    )

    return sorted_list


def merge(left_part: list[int], right_part: list[int]):
    min_cur_length = min(len(left_part), len(right_part))
    result_list = []
    for ind in range(min_cur_length):
        if left_part[ind] < right_part[ind]:
            result_list.append(left_part[ind])
            result_list.append(right_part[ind])
        else:
            result_list.append(right_part[ind])
            result_list.append(left_part[ind])
    if len(left_part) > len(right_part):
        result_list.extend(left_part[min_cur_length:])
    elif len(left_part) < len(right_part):
        result_list.extend(right_part[min_cur_length:])
    return result_list


tests = ([3, 7, 8, 2, 14, 8],)

for test in tests:
    print(merge_sort(test))
