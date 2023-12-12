import math


def pearson_correlation(arr_1, arr_2):
    if len(arr_1) != len(arr_2):
        raise ValueError("Массивы должны быть одинаковой длины")

    n = len(arr_1)

    mean_x = sum(arr_1) / n
    mean_y = sum(arr_2) / n

    variance_x = sum([(xi - mean_x) ** 2 for xi in arr_1]) / float(len(arr_1))
    variance_y = sum([(yi - mean_y) ** 2 for yi in arr_2]) / float(len(arr_2))

    covariance = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(arr_1, arr_2)]) / float(len(arr_1))
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation


array_1 = [11, 40, 61, 17, 45, 39, 80]
array_2 = [10, 31, 14, 11, 29, 71, 56]

correlation = round(pearson_correlation(array_1, array_2), 3)
print(f"Корреляция Пирсона: {correlation}")