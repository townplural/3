def counter():
    counter_list = []
    with open('folder/1.txt', 'rt', encoding='utf') as file1:
        counter1 = 0
        for _ in file1:
            counter1 += 1
        counter_list.append(counter1)

    with open('folder/2.txt', 'rt', encoding='utf') as file2:
        counter2 = 0
        for _ in file2:
            counter2 += 1
        counter_list.append(counter2)
    with open('folder/3.txt', 'rt', encoding='utf') as file3:
        counter3 = 0
        for _ in file3:
            counter3 += 1
        counter_list.append(counter3)
    counter_list.sort()
    with open('folder/4.txt', 'wt', encoding='utf') as file4:
        print(counter1, counter2, counter3, counter_list)
        for a in counter_list:
            if a == counter1:
                file4.write(f'1.txt\n')
                file4.write(f'{str(counter1)}\n')
                with open('folder/1.txt', 'rt', encoding='utf') as file1:
                    for l in file1:
                        file4.write(l)
                    file4.write('\n')
            elif a == counter2:
                file4.write(f'2.txt\n')
                file4.write(f'{str(counter2)}\n')
                with open('folder/2.txt', 'rt', encoding='utf') as file2:
                    for l in file2:
                        file4.write(l)
                    file4.write('\n')
            else:
                file4.write(f'3.txt\n')
                file4.write(f'{str(counter3)}\n')
                with open('folder/3.txt', 'rt', encoding='utf') as file3:
                    for l in file3:
                        file4.write(l)
                    file4.write('\n')





print(counter())
