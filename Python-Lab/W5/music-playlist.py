p1 = ["kiwi", "reminder", "sunflower", "505"] 
p2 = ["cherry", "radio", "505", "heartless"] 

merged_playlist = p1 + p2 
print(merged_playlist)

final_playlist = set(merged_playlist) 
print(list(final_playlist)) 

n = int(input("enter n to rotate playlist: ")) 
print(list(final_playlist)[n:] + list(final_playlist)[:n])

v = [ ] 
c = [ ] 

for i in final_playlist: 
    if i[0] in "AEIOUaeiou": 
        v.append(i) 
    else: 
        c.append(i) 
print("vowels: ", v) 
print("consonants: ", c)