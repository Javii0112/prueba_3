import funcion as fn

menu = fn.menu()
opcion = fn.validar_opcion()

if opcion == 1:
    grabar = fn.ingresar_mascota()
elif opcion == 2:
    buscar = fn.buscar_mascota()
elif opcion == 3:
    retirar = fn.retirarse()
else:
    pass
