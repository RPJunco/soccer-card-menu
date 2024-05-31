from module_p3 import *
import random


def menu():
    print('MENU DE OPCIONES: '
          '\nOpcion 1: Cargar el arreglo pedido con los datos de las n figuritas.'
          '\nOpcion 2: Mostrar todos los datos de todas las figuritas cuyo valor de canje sea mayor a v '
          '(que se carga por teclado), a razón de una por línea en un listado ordenado de menor a mayor según '
          'el nombre del jugador.'
          '\nOpcion 3: Determinar y mostrar la cantidad de figuritas que hay por cada posible país.'
          '\nOpcion 4: Determinar si existe una figurita cuyo país sea igual a p y cuyo número de jugador sea igual '
          'a j, siendo p y j valores ingresados por teclado'
          '\nOpcion 5: Salir')


def validar_numero_int(inf, mensaje):
    num = int(input(mensaje))
    while num <= inf:
        num = int(input('¡¡¡ERROR!!!\nDebe ingresar un numero mayor a [' + str(inf) + ']: '))
    return num


def validar_range(inf, sup, mensaje):
    num = int(input(mensaje))
    while num < inf or num > sup:
        num = int(input('¡¡¡ERROR!!!\nDebe ingresar un numero en el intervalo [' + str(inf) + ';' + str(sup) + ']: '))
    return num


def cargar_arreglo_figuritas(v, n):
    nom_1 = 'Pedro', 'Juan', 'Mario', 'Luis', 'Jorge', 'Rodrigo', 'Sancho', 'Ignacio', 'Felipe'
    ap_1 = 'Gomez', 'Zanchet', 'Juncos', 'Lukaku', 'Mina', 'Santos', 'Gonzalez', 'Retano', 'Gimone'
    for i in range(n):
        #Generar nombre
        nom = random.choice(nom_1)
        apellido = random.choice(ap_1)

        #Cargar datos del registro
        pais = random.randint(1, 32)
        num_j = random.randint(1, 19)
        nombre = nom + ' ' + apellido
        posicion = random.randint(0, 3)
        valor = random.randint(1, 100)

        v.append(Figurita(pais, num_j, nombre, posicion, valor))


def ordenar_vec_figuritas_men_a_may(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].nombre > v[j].nombre:
                v[i], v[j] = v[j], v[i]


def mostrar_vec_ordenado_may_a_v(vec, v):
    tupla_posicion = ('Arquero', 'Defensor', 'Volante', 'Delantero')

    for i in range(len(vec)):
        if vec[i].valor > v:
            print(f'| Pais del jugador: {vec[i].pais} | Numero del jugador: {vec[i].numero} | Nombre del jugador: '
                  f'{vec[i].nombre} | Posicion del jugador: {tupla_posicion[vec[i].posicion]} '
                  f'| Valor de canje de la figurita: {vec[i].valor} |')


def determinar_cant_fig_por_pais(v):
    cont_figus = [0] * 32
    for i in range(len(v)):
        cont_figus[v[i].pais - 1] += 1
    return cont_figus


def mostrar_cant_fig_por_pais(cont, c):
    for i in range(len(cont)):
        if cont[i] > c:
            print('El pais ' + str(i+1) + ' tiene una cantidad de ' + str(cont[i]) + ' figuritas.')


def determinar_existencia_pj_vec(v, p, j):
    for i in range(len(v)):
        if v[i].pais == p and v[i].numero == j:
            v[i].valor = validar_numero_int(0, 'Modificar valor de canje: ')
            print(v[i])
            return

    print('Ninguna de las figuritas del registro cuenta con las especificaciones cargadas..')


def opcion_1(v, n):
    cargar_arreglo_figuritas(v, n)

    for i in range(len(v)):
        print(v[i])


def opcion_2(vec):
    v = validar_range(1, 100, 'Ingrese valor de canje para comparar en el arreglo de figuritas: ')

    ordenar_vec_figuritas_men_a_may(vec)

    mostrar_vec_ordenado_may_a_v(vec, v)


def opcion_3(v):
    c = validar_numero_int(-1, 'Ingrese la cantidad de figuritas que desea para comparar en el arreglo: ')

    cont_fig = determinar_cant_fig_por_pais(v)

    mostrar_cant_fig_por_pais(cont_fig, c)


def opcion_4(v):
    p = validar_range(1, 32, 'Ingrese el pais que desea para comparar en el arreglo: ')
    j = validar_range(1, 19, 'Ingrese el numero del jugador que desea para comprar en el arreglo: ')

    determinar_existencia_pj_vec(v, p, j)


def principal():

    v_figuritas = []
    opcion = -1
    while opcion != 5:
        menu()
        opcion = int(input('Ingrese la opcion que desee: '))

        if opcion == 1:
            num = validar_numero_int(0, 'Ingrese la cantidad de figuritas a añadir: ')
            opcion_1(v_figuritas, num)
        elif len(v_figuritas) == 0:
            print('No hay datos cargados en el registro...')
        elif opcion == 2:
            opcion_2(v_figuritas)
        elif opcion == 3:
            opcion_3(v_figuritas)
        elif opcion == 4:
            opcion_4(v_figuritas)
        elif opcion > 5:
            print('DEBE INGRESAR UNA OPCION VALIDA..')

    print('Eligio la opcion 5: Salir. \nVuelva pronto!!')


if __name__ == '__main__':
    principal()
