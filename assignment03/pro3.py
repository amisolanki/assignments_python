l=[1,9,10,'abc','xyz',27.1,36.1,[100,55.0,'a'],1000,{'a':'astro','b':'bender','c':'cupcake','d':'donut','e':'eclair'}]
print("The main list with some integer and strings along with sublist and dictonary:")
print(l)
print()
for i in range(0,10): 
    if type(l[i])==dict:
        print(l[i].keys())
        print(l[i].values())
