first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))
к на одинаковых позициях в списках first и second.

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

if __name__ == "__main__":
    print(list(first_result))
    print(list(second_result))