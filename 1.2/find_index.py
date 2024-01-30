def main(num_list: list) -> int:
    max_value = 0
    max_index = 0

    for index, num in enumerate(num_list):
        if num > max_value:
            max_value = num
            max_index = index
    print(max_index)
    return max_index


if __name__ == '__main__':
    main([1, 9, 1, 3, 5, 6, 4])
