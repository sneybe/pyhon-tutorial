import sys
var= sys.version_info
print(var)
for i in var: print(i)
str(var)
l= list(var)
print(l)


version = ",".join(str(x) for x in v )
print("hello python (version " + version + ")")