
def main(num):
    print("\nMultiplication Table\n")
    i = 1
    while (i<=10):
        result = num * i
        print(num," x ",i," = ",result)
        i += 1

num = int(input("Enter a number :"))
main(num)
