import os, sys

ano_actual = int (input ('Ingresa el valor de ano actual: '))
ano_nacimiento = int (input ('Ingresa el valor de ano nacimiento: '))
dia_actual = int (input ('Ingresa el valor de dia actual: '))
dia_nacimiento = int (input ('Ingresa el valor de dia nacimiento: '))
dias_del_mes=0
print ('Selecciona el valor de mes actual.')
print ('\t1.- Enero')
print ('\t2.- Febrero')
print ('\t3.- Marzo')
print ('\t4.- Abril')
print ('\t5.- Mayo')
print ('\t6.- Junio')
print ('\t7.- Julio')
print ('\t8.- Agosto')
print ('\t9.- Septiembre')
print ('\t10.- Octubre')
print ('\t11.- Noviembre')
print ('\t12.- Diciembre')
sys.stdout.write ('\t')
mes_actual = 0
while mes_actual<1 or mes_actual>12:
    mes_actual = int (input (': '))
    if mes_actual<1 or mes_actual>12:
        sys.stdout.write ('Valor incorrecto. Ingr\u00E9salo nuevamente.')
print ('Selecciona el valor de mes nacimiento.')
print ('\t1.- Enero')
print ('\t2.- Febrero')
print ('\t3.- Marzo')
print ('\t4.- Abril')
print ('\t5.- Mayo')
print ('\t6.- Junio')
print ('\t7.- Julio')
print ('\t8.- Agosto')
print ('\t9.- Septiembre')
print ('\t10.- Octubre')
print ('\t11.- Noviembre')
print ('\t12.- Diciembre')
sys.stdout.write ('\t')
mes_nacimiento = 0
while mes_nacimiento<1 or mes_nacimiento>12:
    mes_nacimiento = int (input (': '))
    if mes_nacimiento<1 or mes_nacimiento>12:
        sys.stdout.write ('Valor incorrecto. Ingr\u00E9salo nuevamente.')
if mes_actual==1 or mes_actual==3 or mes_actual==5 or mes_actual==7 or mes_actual==8 or mes_actual==10 or mes_actual==12:
    dias_del_mes=31
if mes_actual==2:
    dias_del_mes=28
if mes_actual==4 or mes_actual==6 or mes_actual==9 or mes_actual==11:
    dias_del_mes=30
anos=ano_actual-ano_nacimiento
meses=mes_actual-mes_nacimiento
dias=dia_actual-dia_nacimiento
if dias<0:
    dias=dias+dias_del_mes
    meses=meses-1
if meses<0:
    meses=meses+12
    anos=anos-1
print ('Valor de anos: ' + repr (anos))
print ('Valor de dias: ' + repr (dias))
print ('Valor de dias del mes: ' + repr (dias_del_mes))
print ('Valor de meses: ' + repr (meses))
print ()
os.system ('pause')