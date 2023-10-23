# pickling in python 
# ------------------
# > often used in ml 

# pickling in pyhon is used to convert code to bytes ( 0s and 1s ) 
# and store it or vice - versa 

# > the process of converting code to bytes is called serialization 
# and converting a bytecode to pyhon data is called deserialization 

import pickle

mydict = {'1':'a','2':'b'}

pickle_file = open('picklefile.txt','wb') # wb means write in bytes 

pickle.dump(mydict,pickle_file)

pickle_file = open('picklefile.txt','rb') # read in byte mode

new_dict = pickle.load(pickle_file)

print(new_dict)