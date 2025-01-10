str = input()
last = len(str) - 1
find_palin = True

for i in range(len(str) // 2):
   if str[i] != str[last - i] :
       find_palin = False
       break

print(find_palin)





