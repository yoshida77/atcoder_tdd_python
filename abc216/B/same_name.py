def detect_same_name(list_name):
    # 名字と名前の分離
    # list_name_split = [name.split(" ") for name in list_name]
    for name in list_name:
        list_name.remove(name)
        if name in list_name:
            return "Yes"

    return "No"


if __name__ == "__main__":
    n = int(input())
    list_name = [input() for i in range(n)]
    ans = detect_same_name(list_name)
    print(ans)