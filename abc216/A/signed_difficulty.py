def convert(input_str):
    X_str, Y_str = input_str.split(".")  # string
    Y_int = int(Y_str)
    if 0 <= Y_int <= 2:
        return X_str + "-"
    elif 3 <= Y_int <= 6:
        return X_str
    else:
        return X_str + "+"


if __name__ == "__main__":
    input_str = input()
    output_value = convert(input_str)
    print(output_value)
