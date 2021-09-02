def many_balls(n):
    list_magic = []
    while n > 0:
        if n % 2 == 1:
            n -= 1
            list_magic.append("A")
        else:
            n = n // 2 # 型のためWA
            list_magic.append("B")

    list_magic = list_magic[::-1]
    return ''.join(list_magic)

if __name__ == "__main__":
    n = int(input())
    output_value = many_balls(n)
    print(output_value)