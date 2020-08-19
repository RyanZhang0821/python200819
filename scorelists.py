scores=[]
name=[]
maxscores=0
minscores=100
total = 0
index= 0
index2= 0


for i in range(5):
    n=int(input('score:'))
    r=input('name:')
    scores.append(n)
    name.append(r)
    
    if n>maxscores:
        maxscores=n
        index = i
    if n<minscores:
        minscores=n
        index2 = i
    total=total+n
s=total/len(scores)
print('Total point:',total)
print('Average:',s)
print('Highest point:',maxscores,name[index])
print('Lowest:',minscores,name[index2])

