def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    son=natija_son
    natija= factorial(son)
    print(natija)

if __name__ == "__main__":
    main()
