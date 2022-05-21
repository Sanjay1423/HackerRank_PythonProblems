def split_and_join(line):
    final_string = ""
    for i in line:
        if i == ' ':
            final_string += '-'
        else:
            final_string += i
    return final_string


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
