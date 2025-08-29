def count_words(list1):
    count = 0
    new_list = []
    for word in list1:
        if len(word) >= 2 and word [0] == word[-1]:
            count+=1
            new_list.append(word)

    print("The no. of words which has fisrt and last character same",count)
    print(new_list)  

list1 = ['mom','civic','rest','len','acacia']
count_words(list1)          