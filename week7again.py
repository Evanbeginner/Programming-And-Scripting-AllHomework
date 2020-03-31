import urllib.request 
fname = input('enter file')
l = input('enter letter')

counter = 0
content = urllib.request.urlopen(fname).read().decode('utf-8')

for letter in content:
    if(letter==l):
     counter+=1

print(counter)