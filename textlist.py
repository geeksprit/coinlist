
result = [] 
with open('textlist.txt', 'r') as fa:
  for line in fa:
    t = line.strip('\n')
    result.append(int(t))

print(result)