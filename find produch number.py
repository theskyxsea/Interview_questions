#interview codeing question
#find 2 numners form list whos product is equal to givn number list
#list of numbers to check
checknum = int(input('Product = '))
checklist = [2,4,3,5,6]
rhough=[]
result=[]
for i in list(checklist):
    for s in list(checklist):
        if (i * s)== checknum:
            rhough.append(i)
            rhough.append(s)
for j in rhough:
    if j not in result:
        result.append(j)
if len(result)!=0:
    print(result)
else:
    print('No Match Find')
