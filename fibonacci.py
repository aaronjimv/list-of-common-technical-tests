"""
Fibonacci series
"""


def fibonnaci(n):  # n -> number of series
    fib_series = [0, 1]

    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)

    return fib_series


if __name__ == '__main__':
    n = int(input(
        "Enter number of digits of the fibonacci series to calculate : "
        ))
    serie = fibonnaci(n)
    print(f"Fibonacci serie of {n} is: ")
    for s in serie:
        print(s)
