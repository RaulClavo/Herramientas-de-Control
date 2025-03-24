import numpy as np, control as ctrl, matplotlib.pyplot as plt

numerador = [1, 1, -6, -14, -12, 0]
denominador = [1, -1, -6, 0]

def analizar_ft(num, den):
    ft = ctrl.TransferFunction(num, den)
    polos = ctrl.poles(ft)
    ceros = ctrl.zeros(ft)

    polos_estables = []
    polos_marginales = []
    polos_inestables = []

    ceros_desaceleran = []
    ceros_inestabilizan = []
    ceros_origen = []
    ceros_imagen = []

    for polo in polos:
        if np.real(polo) < 0: polos_estables.append(polo)
        elif np.real(polo) == 0: polos_marginales.append(polo)
        else: polos_inestables.append(polo)

    for cero in ceros:
        if np.imag(cero) != 0: ceros_imagen.append(cero)
        elif np.real(cero) < 0: ceros_desaceleran.append(cero)
        elif np.real(cero) > 0: ceros_inestabilizan.append(cero)
        else: ceros_origen.append(cero)

    print("Función de transferencia:", ft)

    print("\nPolos y su comportamiento:")
    for polo in polos_estables: print(f"Polo: {polo:.2f}, Estable")
    for polo in polos_marginales: print(f"Polo: {polo:.2f}, Marginalmente Estable")
    for polo in polos_inestables: print(f"Polo: {polo:.2f}, Inestable")

    print("\nCeros y su impacto:")
    for cero in ceros_desaceleran: print(f"Cero: {cero:.2f}, Desacelera la respuesta transitoria.")
    for cero in ceros_inestabilizan: print(f"Cero: {cero:.2f}, Puede introducir inestabilidad en ciertas entradas.")
    for cero in ceros_origen: print(f"Cero: {cero:.2f}, Reduce componentes de baja frecuencia o amplifica pendientes iniciales.")
    for cero in ceros_imagen: print(f"Cero: {cero:.2f}, Modula oscilaciones en la respuesta.")

    print("\nVeredicto de Estabilidad:")
    if len(polos_inestables)>0: print("El sistema será inestable.")
    elif polos_marginales: print("El sistema será inestable." if any(polos_marginales.count(polo) > 1 for polo in polos_marginales) else "El sistema será críticamente estable.")
    elif len(polos_estables)>0: print("El sistema será estable.")
    else: print("No hay polos válidos.")

    if input("¿Quieres ver las gráficas? (Y/N): ").strip().upper() != "Y": exit()

    fig, axs = plt.subplots(1, 2, figsize=(14, 7))

    axs[0].set_title('Polos')
    axs[0].scatter(np.real(polos_estables), np.imag(polos_estables), color='blue', label='Polos Estables')
    axs[0].scatter(np.real(polos_marginales), np.imag(polos_marginales), color='green', label='Polos Marginales')
    axs[0].scatter(np.real(polos_inestables), np.imag(polos_inestables), color='red', label='Polos Inestables')

    axs[1].set_title('Ceros')
    axs[1].scatter(np.real(ceros_desaceleran), np.imag(ceros_desaceleran), color='blue', label='Ceros Desaceleradores')
    axs[1].scatter(np.real(ceros_inestabilizan), np.imag(ceros_inestabilizan), color='green', label='Ceros Inestabilizadores')
    axs[1].scatter(np.real(ceros_origen), np.imag(ceros_origen), color='red', label='Ceros Origen')
    axs[1].scatter(np.real(ceros_imagen), np.imag(ceros_imagen), color='black', label='Ceros Conjugados')

    for i in range(0,2):
        axs[i].axhline(0, color='black', linewidth=1)
        axs[i].axvline(0, color='black', linewidth=1)
        axs[i].set_xlabel('Parte Real')
        axs[i].set_ylabel('Parte Imaginaria')
        axs[i].legend()
        axs[i].grid(True)

    plt.tight_layout()
    plt.show()

analizar_ft(numerador, denominador)
