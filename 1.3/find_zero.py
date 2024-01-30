TEST_NUMBER = 7


def factorial(num):
    if num <= 1:
        return 1
    result = 1
    for i in range(1, num + 1):
        result *= i

    return result


def main() -> int:
    count_zero = 0

    factorial_result = factorial(TEST_NUMBER)
    for digit in str(factorial_result)[::-1]:
        if digit == '0':
            count_zero += 1
        else:
            break
    print(count_zero)


if __name__ == '__main__':
    main()
