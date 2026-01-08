def removeLastVowel(txt: str) -> str :
    x = txt.split()
    update = []

    for i in range(len(x)):
        temp = x[i]
        for j in range(len(temp) - 1, -1, -1):
            if temp[j].lower() == 'e':
                temp = temp[:j] + temp[j+1:]
                update.append(temp)
                break
            elif temp[j].lower() == 'a':
                temp = temp[:j] + temp[j+1:]
                update.append(temp)
                break
            elif temp[j].lower() == 'i':
                temp = temp[:j] + temp[j+1:]
                update.append(temp)
                break
            elif temp[j].lower() == 'o':
                temp = temp[:j] + temp[j+1:]
                update.append(temp)
                break
            elif temp[j].lower() == 'u':
                temp = temp[:j] + temp[j+1:]
                update.append(temp)
                break
            else:
                continue

    sep = ' '
    new = sep.join(update)
    return new
