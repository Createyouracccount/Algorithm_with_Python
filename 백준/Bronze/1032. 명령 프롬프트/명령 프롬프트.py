def what_is_pattern(insert_name):
    pattern = ''
    for i in range(len(insert_name[0])):
        char_set = set(file_name[i] for file_name in insert_name)
        if len(char_set) == 1:
            pattern += char_set.pop()
        else:
            pattern += '?'
    return pattern

def main():
    n = int(input())
    insert_name = [input().strip() for _ in range(n)]
    pattern = what_is_pattern(insert_name)
    print(pattern)

if __name__ == "__main__":
    main()