string = input()
pos = int(input())
char = input()
string = string[:pos] + char + string[pos+1:]
print(string)
