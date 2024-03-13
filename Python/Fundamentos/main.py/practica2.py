dic1 = {'a':1,'b':2,'c':3,'d':4}
dic2 = {'c':1,'b':2,'e':3,'f':4}
dic1.update(dic2)
for key in dic1:
    print(key,": ", dic1[key])

