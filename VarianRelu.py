def  VarianCEE(x):
    Ex = sum(x)/len(x)
    Exx2 = sum(val ** 2 for val in x) / len(x)
    veary = Exx2 - Ex ** 2
    return veary

X = [fig for fig in range(1,50)]
print(f'The variance of X is: {VarianCEE(X)}')