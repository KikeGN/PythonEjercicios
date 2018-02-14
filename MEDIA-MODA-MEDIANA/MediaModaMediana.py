# LUIS ENRIQUE GUZMAN NIÑO S14120070
dataM=[1525,257,378,9543,7854,152]
dataMe=[9,5,9,4,3,6,7,1,2,3,9,1,2]

print(dataM)
print(dataMe)

dOrder=sorted(dataMe)

n=len(dOrder)
middle=n//2

# codigo para calcular la mediana
if n%2==0:
	mediana=(dOrder[middle+1] + dOrder[middle+2]) / 2
else:
	mediana=dOrder[middle+1]*1


print ('Total datos', n)
print ('Mediana: ', mediana)

# codigo para calcular la media aritmetica
print ( 'Mediana Aritmetica: ', round(sum(dataM)*1.0/n,2))

# codigo para calcular la moda
repetir = 0                                                                         
for i in dataMe:                                                                              
    aparece = dataMe.count(i)                                                             
    if aparece > repetir:                                                       
        repetir = aparece                                                       
                                                                                         
moda = []                                                                               
for i in dataMe:                                                                              
    aparece = dataMe.count(i)                                                             
    if aparece == repetir and i not in moda:                                   
        moda.append(i)                                                                  
                                                                                         
print ("moda:", moda)
