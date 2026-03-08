def sorted_squares(growthPercentages):
    n = len(growthPercentages)
    result = [0] * n

    left = 0
    right = n - 1
    pos = n - 1

    while left <= right:
        if abs(growthPercentages[left]) > abs(growthPercentages[right]):
            result[pos] = growthPercentages[left] ** 2
            left += 1
        else:
            result[pos] = growthPercentages[right] ** 2
            right -= 1

        pos -= 1

    return result


if __name__ == "__main__":
    growthPercentages = [-5, -2, 0, 3, 10]
    print("Input:", growthPercentages)
    print("Output:", sorted_squares(growthPercentages))
