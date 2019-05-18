def exp(x, b):
    if x >= 0:
        return 1/b*pow(2.718281828459045235360287, (-x/b))
    else:
        return 0

print(exp(1,2))