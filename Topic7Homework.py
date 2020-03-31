from urllib.request import urlopen
with urlopen('https://www.gutenberg.org/files/2701/old/moby10b.txt') as mdata:
   atw = []
for eil in mdata:
    low = eil.decode('utf-8').split()
    x=+1
    print(x,low)
    for ew in low:
        atw.append(ew)

z = 0
for x in atw:
    z+=1
    print(z,x)


