def char_Occurrence(str):
    dict={}
    for ch in str:
        keys = dict.keys()
        if (ch.isspace())==True:
                continue
        if ch in keys:
            dict[ch]+=1
        else:
            dict[ch]=1
    return dict

print(char_Occurrence(input("Enter you string : ")))