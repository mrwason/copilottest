def multiply_large_numbers(a, b):
    a = a[::-1]
    b = b[::-1]
    result = [0] * (len(a) + len(b))

    for i in range(len(a)):
        for j in range(len(b)):
            result[i + j] += int(a[i]) * int(b[j])
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return ''.join(map(str, result[::-1]))