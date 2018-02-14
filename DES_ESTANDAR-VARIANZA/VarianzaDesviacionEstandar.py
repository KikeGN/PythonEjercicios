# LUIS ENRIQUE GUZMAN NIÑO
n = 9
datos = [13, 14, 15, 15, 15, 16, 17, 18, 20]
i = 0

promedio = sum(datos)/n 
cuadrados = [] #lista de la suma de los cuadrados de las diferencias entre los datos y el promedio
for dato in datos:
  r = (dato - promedio)**2
  cuadrados.append(r)
desviacion = (sum(cuadrados)/(n - 1))**0.5 #fórmula de desviación estándar
print ('LA DESVIACION ESANDAR ES:', desviacion)
def varianza():

    lista2 = []
    A = len(datos)
    suma=0
    varis=0
    if A>1:
        for i in datos:
            suma += i
        p = ((suma+0.0)/(A+0.0))
        for j in range((A)):
            sumat = (datos[j]-p)**2
            lista2.append(sumat)
        for k in lista2:
            varis += k
        vari = varis
        va = ((vari+0.0)/(A+0.0))
        print ('LA VARIANZA ES:', str(va))

        

varianza()

