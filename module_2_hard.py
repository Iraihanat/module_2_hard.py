for i in range(3, 21):
    result = [i, '-']
    for j in range(1, 21):
        for k in range(1, 21):
            if (i % (j + (k))) == 0:
                if k > j:
                    result.append(int(f'{j}{k}'))
    print(*result)


