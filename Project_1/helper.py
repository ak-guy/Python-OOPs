def generateTransactionIds(start):
    while True:
        start += 1
        yield start

if __name__ == '__main__':
    t = generateTransactionIds(100)
    print(next(t))
    print(next(t))