#with open('test.txt','r') as f:
   #size = 5
   #f_contents = f.read(size)

   #while len(f_contents) > 0:
      # print(f_contents,end='*')
      # f_contents = f.read(size)

with open('test.txt','r') as rf:
    with open('test2.tx','w') as wf:
        for line in rf:
            wf.write(line)
