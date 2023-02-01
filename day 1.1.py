def manoj(x,y):
    if len(x)!=len(y):
        return False
    for i in range(len(x)):
        count=0
        if x.count(x[i])!=y.count(y[i]):
            return False
    return True
print(manoj("fool","poor"))
print(manoj("foal","poor"))
print(manoj("too","bar"))
print(manoj("toto","yaya"))
