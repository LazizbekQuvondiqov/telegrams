def yigindi(nom):
    sum = 0
    while nom:
        sum += nom % 10
        nom //= 10
    return sum

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
      son = int(input("Istalgan sonni kiriting: "))
      natija = yigindi(son)
      kopaytma=factorial(natija)
     
      with open('C:/Users/bekmu/OneDrive/Ishchi stol/bekmurod.txt', 'w') as file:
        file.write(f" {kopaytma}")

if __name__ == "__main__":
    main()



