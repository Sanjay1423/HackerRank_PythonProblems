
def mutate_string(string, position, character):
    str2_list = []
    final_string = ""
    for i in string:
        str2_list.append(i)

    str2_list[position] = character
    return final_string.join(str2_list)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)




