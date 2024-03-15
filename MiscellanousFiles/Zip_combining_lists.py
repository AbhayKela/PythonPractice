names = ['abhay', 'anu', 'anup']
ages = [36,36,40]

#for i in range (len(names)):
#    print (names[i] , ages[i])

for names , ages in zip(names , ages): 
    print (names, ages)