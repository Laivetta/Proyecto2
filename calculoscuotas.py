



def calculo_cuota (monto, tasa, cuotas):
    """
    Retorna el valor actual de la cuota, según el método francés,
    en donde las cuotas son fijas. -> float(x)
 
    Formula = R = P [(i (1 + i)**n) / ((1 + i)**n – 1)].
    Donde:
    R = renta (cuota)
    P = principal (préstamo adquirido)
    i = tasa de interés
    n = número de periodos
    -> (Moneda valor, Moneda interes, Moneda monto)
    """
    tasa=0.09
    cantidad=20
    monto=26600
    valor = monto * ( (tasa * ((1 + tasa)**cuotas)) / (((1 + tasa)**cuotas) - 1) )
    #amortizacion = monto (n-1) + tasa / ((1+tasa)**n -1)
    return valor

#def calculo_amortizacion():
    #A1= capital0 x interes / (((1 + interes)** periodo )-1)
    # la amortizacion en el periodo 1 esta en funcion del capital en el periodo 0
    #https://blogs.udima.es/administracion-y-direccion-de-empresas/9-2-prestamo-frances-fraccionado-html/


    

#el append de la lista lo tengo que hacer afuera del loop porque sino se va borrando y me queda
#solo el ultimo valor



tasa=0.09
cantidad=20
monto=26600

cuota = round(calculo_cuota(monto, tasa, cantidad),2)

lista_periodos = []
lista_interes = []
lista_amortizacion = []
diccionario = {}
x = range (cantidad)
for n in x:
    lista_periodos.append(cuota)
    interes = round (monto * tasa ,2)
    amortizacion =  round (cuota - interes, 2)
    monto = round (monto - amortizacion, 2)
    print (f"Esta es la cuota: {n+1}, interes: {interes}, amortizacion: {amortizacion}, monto adeudado {monto}")
    lista_interes.append(interes)
    lista_amortizacion.append(amortizacion) 
    diccionario [n+1]:lista_interes
    


print(f"{lista_periodos[18]}")
print(f"{lista_interes[18]}")
print(f"{lista_amortizacion[18]}")
print(f"{diccionario}")
print(f"{cuota}")

"""
ahora =date.today()
despues = ahora + relativedelta(years=+0, months=+2, weeks=+0)
#relativedelta le suma un mes a la fecha y por la dudas le puedo sumar una semana
# https://dateutil.readthedocs.io/en/stable/examples.html#relativedelta-examples
print (ahora)
print (despues)
 
x = range (cantidad)
for n in x:
    despues = ahora + relativedelta(months=+n)
    print (despues)
    
    print (list(rrule(DAILY, count=2, dtstart=parse("20191129T090000"))))

"""