list_names = ["rahul", "suhas"]
output = {}
for i in list_names:
    for j in range(0,len(i)):
        if i[j] in output:
            if i not in output[i[j]]:
                output[i[j]].append(i)
        else:
            output[i[j]] = [i]
print(output)
