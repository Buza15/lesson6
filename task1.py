import re

# First way

func = "   If advertisements are to he learned, there Is a need for lots of reperirion "
compiled = re.compile(r'\b[a,q,e,y,u,i,o,A,Q,E,Y,U,I,O]\w+')
print(compiled.findall(func))



#second way

print(re.findall(r'\b[a,q,e,y,u,i,o]\w+',
                 ' If advertisements are to he learned, '
                 'there Is a need for lots of reperirion ',
                 flags = re.IGNORECASE))
