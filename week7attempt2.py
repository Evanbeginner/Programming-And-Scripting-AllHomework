import urllib.request

fname= input("Enter file")
Letter = input("Enter Number")

counter = 0
content = urllib.request.urlopen(fname).read().decode('utf-8')

for Letter in content:
    if(Letter=='a'):
        counter+=1

print(counter)