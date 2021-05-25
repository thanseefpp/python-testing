list_new = ['SGST Sale 2.5%', 'CGST Sale 2.5%', 'SGST Sale 14%', 'CGST Sale 14%', 'SGST Sale 2.5%', 'CGST Sale 2.5%']
new_list = []
for i in range(0,len(list_new)):
    for j in range(1,len(list_new)):
        if i == j:
            pass
        else:
            if list_new[j] == list_new [i]:
                if i == len(list_new):
                    break
                else:
                    print(i,j,list_new[i])