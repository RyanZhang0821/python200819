import os.path

if os.path.isfile('y.txt'):
    print('exist')
    file=open('y.txt','a')
    file.write('file exists')
    file.close()
else:
    print('not exist')
    file=open('y.txt','w')
    file.write('not exists')
    file.close()
