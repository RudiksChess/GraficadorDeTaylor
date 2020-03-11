"""
Nombre: Rudik Roberto Rompich
Carnet: 19857

Actividad Graficador de series de Taylor
Herramientas tecnológicas para matemática
"""


import matplotlib.pyplot as plt
import numpy as np
import math



def e(x, n):
    e_sumatoria = 0
    for i in range(n):
        e_sumatoria += x**i/math.factorial(i)
    return e_sumatoria

def cos(x, n):
    cos_sumatoria = 0
    for i in range(n):
        signo = (-1)**i
        num = x**(2*i)
        denom = math.factorial(2*i)
        cos_sumatoria += (signo)*((num)/(denom))
    return cos_sumatoria


def sen(x, n):
    sen_sumatoria = 0
    for i in range(n):
        signo = (-1)**i
        num = x**(2*i+1)
        denom = math.factorial(2*i+1)
        sen_sumatoria += (signo) * ((num)/(denom))
    return sen_sumatoria

def graficar(tipo,min, max, a, num):

    eje_x = np.linspace(min, max, 100)
    if tipo ==1:
        func_orginal = [np.sin(a*i) for i in eje_x]
        func_taylor = [sen(a*i,num) for i in eje_x]
        func_error =  [np.sin(a*i) - sen(a*i,num)  for i in eje_x]
        numerito= f"{a}x"
        titulo = f"$\ sin{numerito}$"
        tay= f"$\ T_{num}(x) $"
        elerror= f" {titulo} - {tay}"

    elif tipo ==2:
        func_orginal = np.cos(a*eje_x)
        func_taylor = [cos(a*i,num) for i in eje_x]
        func_error =  [np.cos(a*i) - cos(a*i,num)  for i in eje_x]
        numerito= f"{a}x"
        titulo = f"$\ cos{numerito}$"
        tay= f"$\ T_{num}(x) $"
        elerror= f" {titulo} - {tay}"
    elif tipo ==3:
        func_orginal = np.exp(a*eje_x)
        func_taylor = [e(a*i,num) for i in eje_x]
        func_error =  [np.exp(a*i) - e(a*i,num)  for i in eje_x]

        numerito= f"{a}x"
        titulo = f"$\ e^{numerito}$"
        tay= f"$\ T_{num}(x) $"
        elerror= f" {titulo} - {tay}"


    plt.figure()
    plt.subplot(211)
    plt.grid()
    plt.plot(eje_x,func_orginal)
    plt.plot(eje_x,func_taylor)
    plt.title(label="Comparativo polinomios de Taylor")
    plt.legend([titulo,f"$\ T_{num}(x) $"])


    plt.subplot(212)
    plt.grid()
    plt.plot(eje_x,func_error)
    plt.title(label="Error en la aproximación de Taylor")
    plt.legend(elerror)
    plt.savefig("LaGrafiquita.png")

    plt.show()





lol = int(input("\n|BIENVENIDO AL GRAFICADOR DE SERIES DE MCLAURIN: | \n" +

                "SELECCIONE UNA FUNCIÓN PARA GRAFICAR: \n\n" +
                "1. e^(a)(x) \n" +
                "2. cos(ax)\n" +
                "3. sin(ax) \n" +
                "0. Salir \n\n" +
                "OPCIÓN:"))

while lol != 0:

    try:

        if lol == 1:

            w = int(input("¿En dónde comienza el intervalo?: "))
            x = int(input("¿En dónde termina el intervalo?: "))
            y = int(input("Asignar valor a: "))
            z = int(input("Número de términos:"))

            graficar(3,w,x,y,z)


        elif lol == 2:
            w = int(input("¿En dónde comienza el intervalo?: "))
            x = int(input("¿En dónde termina el intervalo?: "))
            y = int(input("Asignar valor a: "))
            z = int(input("Número de términos:"))

            graficar(2,w,x,y,z)



        elif lol == 3:
            w = int(input("¿En dónde comienza el intervalo?: "))
            x = int(input("¿En dónde termina el intervalo?: "))
            y = int(input("Asignar valor a: "))
            z = int(input("Número de términos:"))

            graficar(1,w,x,y,z)







        else:

            print("Vuelva a ingresar un valor válido")

        lol = int(input("\n|BIENVENIDO AL GRAFICADOR DE SERIES DE MCLAURIN: | \n" +

                        "SELECCIONE UNA FUNCIÓN PARA GRAFICAR: \n\n" +
                        "1. e^(a)(x) \n" +
                        "2. cos(ax)\n" +
                        "3. sin(ax) \n" +
                        "0. Salir \n\n" +
                        "OPCIÓN:"))


    except ValueError:

        print("ERROR: Está ingresando un valor no númerico")