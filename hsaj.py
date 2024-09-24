import random

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
def main():
    a=random.randint(10,30)
    kopaytma=factorial(a)
    with open('C:/Users/bekmu/OneDrive/Ishchi stol/bekmurod.txt', 'w') as file:
        file.write(f" {kopaytma}")

if __name__ == "__main__":
    main()
