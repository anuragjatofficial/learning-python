import os

# f=open('new.java','w') # to create file
# f.close()

# to remove file

if os.path.exists('new.java'):
    os.remove('new.java') 
else:
    print('no file found new.java')

