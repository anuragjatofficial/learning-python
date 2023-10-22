# PIP in python 

# > PIP is a package manager in python, used to organize different packages 

# > let's install any package using pip

# > pip install camelcase

import camelcase

x = camelcase.CamelCase()
a = 'hi this text needs to be capitalized'

print(x.hump(a))