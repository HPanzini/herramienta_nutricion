# -*- coding: utf-8 -*-
"""Herramienta para nutricionistas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Nuya6ud19t1ImHzNh-566MzfYPfDHqKU
"""

## inputs para cálculos ##

nombre = input('Su nombre:')
while True:
  sexo = input('Seleccione su sexo: Hombre o Mujer\n' )
  if not sexo in ['Hombre', 'hombre', 'h', 'Mujer', 'mujer', 'm']:
    print('No entiendo')
    continue
  else:
    break
peso = input('Su peso: ')
altura = input('Su altura: ')
edad = input('Su edad: ')
ex_horas_sem  = input('Cuantas horas por semana entrena?')
mets = input('Introducir constante de tabla MET:')

pc_carbs = float(input('Porcentaje de carbohidratos:'))
pc_prote = float(input('Porcentaje de proteínas:'))
pc_grasas = float(input('Porcentaje de grasas:'))

## ecuaciones

hb_hombres = 66.47 + (13.7 * float(peso)) + (5 * float(altura)) - (6.7 * float(edad))
hb_mujeres =  665.09 + (9.5 * float(peso)) + (1.84 * float(altura)) - (4.67 * float(edad))

## TMB

if sexo in ['Hombre', 'hombre', 'h']:
  tmb = round(hb_hombres/24,1)
  print("Su gasto basal es de:",round(hb_hombres, 1), "kcal")
else: 
  tmb = round(hb_mujeres/24, 1)
  print("Su gasto basal es de:",round(hb_mujeres, 1), "kcal")

## ejercicio

ex_horas_diarias = float(ex_horas_sem)/7
ex_gasto = tmb*ex_horas_diarias*float(mets)
print("Su gasto entrenando es de:",round(ex_gasto, 1), "kcal")

## gasto total

if sexo in ['Hombre']:
  get=round((hb_hombres + ex_gasto)*1.3,1)
else: 
  get=round((hb_mujeres + ex_gasto)*1.3,1)
print("Su GET es de:",get, "kcal")

## macronutrientes
carbohidratos  = round((get*pc_carbs)/4,1)
print('CHO:',carbohidratos, 'gr')
proteinas  = round((get*pc_prote)/4,1)
print('PRO:',proteinas, 'gr')
grasas  = round((get*pc_grasas)/9,1)
print('GRA:',grasas, 'gr')

## cargar base de desayunos + input para saber el tipo de desayuno a elegir

import pandas as pd
data_des = pd.read_excel('desayuno.xlsx')
while True:
  tipo_des = input('Seleccione el tipo de desayuno: \n a. Descenso\n b. Aumento\n c. Vegetariano\n d. Vegano\n e. Trabajando\n\n')
  if not tipo_des in ['a', 'b', 'c', 'd', 'e']:
    print('Te confundiste de letra amigo...')
    continue
  else:
    break

while True:
  tipo_mer = input('Seleccione el tipo de merienda: \n a. Descenso\n b. Aumento\n c. Vegetariano\n d. Vegano\n e. Trabajando\n\n')
  if not tipo_mer in ['a', 'b', 'c', 'd', 'e']:
    print('Te confundiste de letra amigo...')
    continue
  else:
    break

while True:
  des_leche = input('\nDesayuna con leche?: \n Si\n No\n\n')
  if not des_leche in ['si', 'no', 's', 'n', 'Si', 'No','SI','NO']:
    print('Te pregunte si SI o NO...')
    continue
  else:
    break

while True:
  mer_leche = input('\nDesayuna con leche?: \n Si\n No\n\n')
  if not mer_leche in ['si', 'no', 's', 'n', 'Si', 'No','SI','NO']:
    print('Te pregunte si SI o NO...')
    continue
  else:
    break

## función para elegir el desayuno sacando gustos

gusto1, gusto2 = input('que no te gusta:').split(' ')

data_gustos_des_dc = data_des['des_dc'][(~data_des['des_dc'].str.contains(gusto1,na=False)) & (~data_des['des_dc'].str.contains(gusto2,na=False))]
data_gustos_des_dc = data_gustos_des_dc.dropna()
data_gustos_des_au = data_des['des_au'][(~data_des['des_au'].str.contains(gusto1,na=False)) & (~data_des['des_au'].str.contains(gusto2,na=False))]
data_gustos_des_au = data_gustos_des_au.dropna()
data_gustos_des_vegeta = data_des['des_vegeta'][(~data_des['des_vegeta'].str.contains(gusto1,na=False)) & (~data_des['des_vegeta'].str.contains(gusto2,na=False))]
data_gustos_des_vegeta = data_gustos_des_vegeta.dropna()
data_gustos_des_vegan = data_des['des_vegan'][(~data_des['des_vegan'].str.contains(gusto1,na=False)) & (~data_des['des_vegan'].str.contains(gusto2,na=False))]
data_gustos_des_vegan = data_gustos_des_vegan.dropna()
data_gustos_des_trabajo = data_des['des_trabajo'][(~data_des['des_trabajo'].str.contains(gusto1,na=False)) & (~data_des['des_trabajo'].str.contains(gusto2,na=False))]
data_gustos_des_trabajo = data_gustos_des_trabajo.dropna()

if tipo_des in ['a']:
  desayuno1 = data_gustos_des_dc.sample()
  desayuno2 = data_gustos_des_dc.sample()
  desayuno3 = data_gustos_des_dc.sample()
  desayuno4 = data_gustos_des_dc.sample()
  desayuno5 = data_gustos_des_dc.sample()
  desayuno6 = data_gustos_des_dc.sample()
else:
  if tipo_des in ['b']:
    desayuno1 = data_gustos_des_au.sample()
    desayuno2 = data_gustos_des_au.sample()
    desayuno3 = data_gustos_des_au.sample()
    desayuno4 = data_gustos_des_au.sample()
    desayuno5 = data_gustos_des_au.sample()
    desayuno6 = data_gustos_des_au.sample()
  else:
    if tipo_des in ['c']:
      desayuno1 = data_gustos_des_vegeta.sample()
      desayuno2 = data_gustos_des_vegeta.sample()
      desayuno3 = data_gustos_des_vegeta.sample()
      desayuno4 = data_gustos_des_vegeta.sample()
      desayuno5 = data_gustos_des_vegeta.sample()
      desayuno6 = data_gustos_des_vegeta.sample()
    else:
      if tipo_des in ['d']:
        desayuno1 = data_gustos_des_vegan.sample()
        desayuno2 = data_gustos_des_vegan.sample()
        desayuno3 = data_gustos_des_vegan.sample()
        desayuno4 = data_gustos_des_vegan.sample()
        desayuno5 = data_gustos_des_vegan.sample()
        desayuno6 = data_gustos_des_vegan.sample()
      else:
        if tipo_des in ['e']:
          desayuno1 = data_gustos_des_trabajo.sample()
          desayuno2 = data_gustos_des_trabajo.sample()
          desayuno3 = data_gustos_des_trabajo.sample()
          desayuno4 = data_gustos_des_trabajo.sample()
          desayuno5 = data_gustos_des_trabajo.sample()
          desayuno6 = data_gustos_des_trabajo.sample()


print('\nDesayuno: \n')
if des_leche in ['s','Si','SI','si']:
  desayuno1 = print('Leche con',str(desayuno1.values).lstrip('[').rstrip(']').strip('\''))
  desayuno2 = print('Leche con',str(desayuno2.values).lstrip('[').rstrip(']').strip('\''))
  desayuno3 = print('Leche con',str(desayuno3.values).lstrip('[').rstrip(']').strip('\''))
  desayuno4 = print('Leche con',str(desayuno4.values).lstrip('[').rstrip(']').strip('\''))
  desayuno5 = print('Leche con',str(desayuno5.values).lstrip('[').rstrip(']').strip('\''))
  desayuno6 = print('Leche con',str(desayuno6.values).lstrip('[').rstrip(']').strip('\''))
else:
  desayuno1 = print('Infusión con',str(desayuno1.values).lstrip('[').rstrip(']').strip('\''))
  desayuno2 = print('Infusión con',str(desayuno2.values).lstrip('[').rstrip(']').strip('\''))
  desayuno3 = print('Infusión con',str(desayuno3.values).lstrip('[').rstrip(']').strip('\''))
  desayuno4 = print('Infusión con',str(desayuno4.values).lstrip('[').rstrip(']').strip('\''))
  desayuno5 = print('Infusión con',str(desayuno5.values).lstrip('[').rstrip(']').strip('\''))
  desayuno6 = print('Infusión con',str(desayuno6.values).lstrip('[').rstrip(']').strip('\''))
print('\nMerienda: \n')

## función para elegir el merienda 

data_gustos_mer_dc = data_des['des_dc'][(~data_des['des_dc'].str.contains(gusto1,na=False)) & (~data_des['des_dc'].str.contains(gusto2,na=False))]
data_gustos_mer_dc = data_gustos_mer_dc.dropna()
data_gustos_mer_au = data_des['des_au'][(~data_des['des_au'].str.contains(gusto1,na=False)) & (~data_des['des_au'].str.contains(gusto2,na=False))]
data_gustos_mer_au = data_gustos_mer_au.dropna()
data_gustos_mer_vegeta = data_des['des_vegeta'][(~data_des['des_vegeta'].str.contains(gusto1,na=False)) & (~data_des['des_vegeta'].str.contains(gusto2,na=False))]
data_gustos_mer_vegeta = data_gustos_mer_vegeta.dropna()
data_gustos_mer_vegan = data_des['des_vegan'][(~data_des['des_vegan'].str.contains(gusto1,na=False)) & (~data_des['des_vegan'].str.contains(gusto2,na=False))]
data_gustos_mer_vegan = data_gustos_mer_vegan.dropna()
data_gustos_mer_trabajo = data_des['des_trabajo'][(~data_des['des_trabajo'].str.contains(gusto1,na=False)) & (~data_des['des_trabajo'].str.contains(gusto2,na=False))]
data_gustos_mer_trabajo = data_gustos_mer_trabajo.dropna()

if tipo_mer in ['a']:
  merienda1 = data_gustos_mer_dc.sample()
  merienda2 = data_gustos_mer_dc.sample()
  merienda3 = data_gustos_mer_dc.sample()
  merienda4 = data_gustos_mer_dc.sample()
  merienda5 = data_gustos_mer_dc.sample()
  merienda6 = data_gustos_mer_dc.sample()
else:
  if tipo_mer in ['b']:
    merienda1 = data_gustos_mer_au.sample()
    merienda2 = data_gustos_mer_au.sample()
    merienda3 = data_gustos_mer_au.sample()
    merienda4 = data_gustos_mer_au.sample()
    merienda5 = data_gustos_mer_au.sample()
    merienda6 = data_gustos_mer_au.sample()
  else:
    if tipo_mer in ['c']:
      merienda1 = data_gustos_mer_vegeta.sample()
      merienda2 = data_gustos_mer_vegeta.sample()
      merienda3 = data_gustos_mer_vegeta.sample()
      merienda4 = data_gustos_mer_vegeta.sample()
      merienda5 = data_gustos_mer_vegeta.sample()
      merienda6 = data_gustos_mer_vegeta.sample()
    else:
      if tipo_mer in ['d']:
        merienda1 = data_gustos_mer_vegan.sample()
        merienda2 = data_gustos_mer_vegan.sample()
        merienda3 = data_gustos_mer_vegan.sample()
        merienda4 = data_gustos_mer_vegan.sample()
        merienda5 = data_gustos_mer_vegan.sample()
        merienda6 = data_gustos_mer_vegan.sample()
      else:
        if tipo_mer in ['e']:
          merienda1 = data_gustos_mer_trabajo.sample()
          merienda2 = data_gustos_mer_trabajo.sample()
          merienda3 = data_gustos_mer_trabajo.sample()
          merienda4 = data_gustos_mer_trabajo.sample()
          merienda5 = data_gustos_mer_trabajo.sample()
          merienda6 = data_gustos_mer_trabajo.sample()

if mer_leche in ['s','Si','SI','si']:
  merienda1 = print('Leche con',str(merienda1.values).lstrip('[').rstrip(']').strip('\''))
  merienda2 = print('Leche con',str(merienda2.values).lstrip('[').rstrip(']').strip('\''))
  merienda3 = print('Leche con',str(merienda3.values).lstrip('[').rstrip(']').strip('\''))
  merienda4 = print('Leche con',str(merienda4.values).lstrip('[').rstrip(']').strip('\''))
  merienda5 = print('Leche con',str(merienda5.values).lstrip('[').rstrip(']').strip('\''))
  merienda6 = print('Leche con',str(merienda6.values).lstrip('[').rstrip(']').strip('\''))
else:
  merienda1 = print('Infusión con',str(merienda1.values).lstrip('[').rstrip(']').strip('\''))
  merienda2 = print('Infusión con',str(merienda2.values).lstrip('[').rstrip(']').strip('\''))
  merienda3 = print('Infusión con',str(merienda3.values).lstrip('[').rstrip(']').strip('\''))
  merienda4 = print('Infusión con',str(merienda4.values).lstrip('[').rstrip(']').strip('\''))
  merienda5 = print('Infusión con',str(merienda5.values).lstrip('[').rstrip(']').strip('\''))
  merienda6 = print('Infusión con',str(merienda6.values).lstrip('[').rstrip(']').strip('\''))

## almuerzo y cena inputs

while True:
  tipo_alm = input('Seleccione el tipo de almuerzo: \n a. Con carne\n b. Sin carne\n c. Vegetariano\n\n')
  if not tipo_alm in ['a', 'b', 'c']:
    print('Te confundiste de letra amigo...')
    continue
  else:
    break

if tipo_alm in ['a']:
  tipo_cena='b'
else:
  if tipo_alm in ['b']:
    tipo_cena='a'
  else:
    tipo_cena='c'

gusto3, gusto4 = input('que no te gusta:').split(' ')

## almuerzo

data_gustos_alm_carne = data_des['alm_carne'][(~data_des['alm_carne'].str.contains(gusto3,na=False)) & (~data_des['alm_carne'].str.contains(gusto4,na=False))]
data_gustos_alm_carne = data_gustos_alm_carne.dropna()
data_gustos_alm_sincarne = data_des['alm_sin_carne'][(~data_des['alm_sin_carne'].str.contains(gusto3,na=False)) & (~data_des['alm_sin_carne'].str.contains(gusto4,na=False))]
data_gustos_alm_sincarne = data_gustos_alm_sincarne.dropna()
data_gustos_alm_vegetariano = data_des['alm_vegetariano'][(~data_des['alm_vegetariano'].str.contains(gusto3,na=False)) & (~data_des['alm_vegetariano'].str.contains(gusto4,na=False))]
data_gustos_alm_vegetariano = data_gustos_alm_vegetariano.dropna()

if tipo_alm in ['a']:
  almuerzo1 = data_gustos_alm_carne.sample()
  almuerzo2 = data_gustos_alm_carne.sample()
  almuerzo3 = data_gustos_alm_carne.sample()
  almuerzo4 = data_gustos_alm_carne.sample()
  almuerzo5 = data_gustos_alm_carne.sample()
  almuerzo6 = data_gustos_alm_carne.sample()
else:
  if tipo_alm in ['b']:
    almuerzo1 = data_gustos_alm_sincarne.sample()
    almuerzo2= data_gustos_alm_sincarne.sample()
    almuerzo3 = data_gustos_alm_sincarne.sample()
    almuerzo4 = data_gustos_alm_sincarne.sample()
    almuerzo5 = data_gustos_alm_sincarne.sample()
    almuerzo6 = data_gustos_alm_sincarne.sample()
  else:
    if tipo_alm in ['c']:
      almuerzo1 = data_gustos_alm_vegetariano.sample()
      almuerzo2 = data_gustos_alm_vegetariano.sample()
      almuerzo3 = data_gustos_alm_vegetariano.sample()
      almuerzo4 = data_gustos_alm_vegetariano.sample()
      almuerzo5 = data_gustos_alm_vegetariano.sample()
      almuerzo6 = data_gustos_alm_vegetariano.sample()

print('Almuerzos: \n')
print(str(almuerzo1.values).lstrip('[').rstrip(']').strip('\''))
print(str(almuerzo2.values).lstrip('[').rstrip(']').strip('\''))
print(str(almuerzo3.values).lstrip('[').rstrip(']').strip('\''))
print(str(almuerzo4.values).lstrip('[').rstrip(']').strip('\''))
print(str(almuerzo5.values).lstrip('[').rstrip(']').strip('\''))
print(str(almuerzo6.values).lstrip('[').rstrip(']').strip('\''))
print('\nCenas: \n')

## cena

if tipo_cena in ['a']:
  cena1 = data_gustos_alm_carne.sample()
  cena2 = data_gustos_alm_carne.sample()
  cena3 = data_gustos_alm_carne.sample()
  cena4 = data_gustos_alm_carne.sample()
  cena5 = data_gustos_alm_carne.sample()
  cena6 = data_gustos_alm_carne.sample()
else:
  if tipo_cena in ['b']:
    cena1 = data_gustos_alm_sincarne.sample()
    cena2 = data_gustos_alm_sincarne.sample()
    cena3 = data_gustos_alm_sincarne.sample()
    cena4 = data_gustos_alm_sincarne.sample()
    cena5 = data_gustos_alm_sincarne.sample()
    cena6 = data_gustos_alm_sincarne.sample()
  else:
    if tipo_cena in ['c']:
      cena1 = data_gustos_alm_vegetariano.sample()
      cena2 = data_gustos_alm_vegetariano.sample()
      cena3 = data_gustos_alm_vegetariano.sample()
      cena4 = data_gustos_alm_vegetariano.sample()
      cena5 = data_gustos_alm_vegetariano.sample()
      cena6 = data_gustos_alm_vegetariano.sample()

print(str(cena1.values).lstrip('[').rstrip(']').strip('\''))
print(str(cena2.values).lstrip('[').rstrip(']').strip('\''))
print(str(cena3.values).lstrip('[').rstrip(']').strip('\''))
print(str(cena4.values).lstrip('[').rstrip(']').strip('\''))
print(str(cena5.values).lstrip('[').rstrip(']').strip('\''))
print(str(cena6.values).lstrip('[').rstrip(']').strip('\''))

print('Desayuno: ',desayuno1,'\n')
print(almuerzo1)
print(merienda1)
print(cena1)