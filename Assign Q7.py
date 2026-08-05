#A
#A B C
#A B C D E
#A B C D E F G
#A B C D E F G H I

for i in range(1, 10, 2):
    ch = 65
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()