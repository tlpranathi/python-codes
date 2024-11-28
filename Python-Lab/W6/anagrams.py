word1 = list(input("word1: "))
word2 = list(input("word2: "))
if len(word1) == len(word2):
    word1.sort()
    word2.sort()                     
    if word1 == word2:              
        print(word1[0], ",", word2[0], "are anagrams!!!")             
    else:
        print(word1[0], ",", word2[0], "are not anagrams!!!")             
else:
    print(word1[0], ",", word2[0], "are not anagrams!!!")