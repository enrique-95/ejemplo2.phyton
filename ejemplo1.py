# -*- coding: utf-8 -*-
def cambiar(cantidad):
    tipo_cambio=18.81
    return cantidad/tipo_cambio

def main():
    print('calculadora de dolares')
    print('')
    cantidad= float(input('ingresa la cantidad de pesos que quieres convertir: '))
    result = cambiar(cantidad)

    print('${} pesos mx son ${} dolares(us)'.format(cantidad,result))
    print('')
          
if __name__=='__main__':
    main()
