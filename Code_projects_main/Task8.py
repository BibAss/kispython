import re


def main(x):
    bible = {}
    word_1 = re.findall(r'\w+\d*\s?:', x)
    word_2 = re.findall(r'-?\d+\.', x)
    for i in range(0, len(word_1)):
        a = re.findall(r'\w+', word_1[i])
        word_1[i] = a[0]
        word_2[i] = int(word_2[i][:-1])
        bible[word_1[i]] = word_2[i]
    return bible

var1 = "begin<: declare xeanor_545 := 3628. :> <: declare lean :=-4933. :> <:declare dibius := -5480. :><: declare " \
       "arondi := -5628. :> end "
var2 = "begin<:declare erge := 8331. :> <:declare souste := -4590. :> <:declare bexeza:=-2848.:> end"
print(main(var1))
