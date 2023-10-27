posicion_inicial = int(input("Introduzca la posición inicial en metros: "))
velocidad_inicial = int(input("Introduzca la velocidad inicial en metros/segundo: "))
aceleracion = int(input("Introduzca la aceleracion en metros/segundo^2: "))
tiempo = int(input("Introduzca el tiempo transcurrido en segundos: "))

"""
Final Position (x) = Initial Position (x0) + (Initial Velocity (v0) * time (t)) + (0.5 * Acceleration (a) * time^2)
Velocity (v) = Initial Velocity (v0) + (Acceleration (a) * time)
"""

posicion_final = posicion_inicial + (velocidad_inicial * tiempo) + (0.5 * aceleracion * (tiempo ** 2))
velocidad_final = velocidad_inicial + (aceleracion * tiempo)
print(f"La posición final es de {posicion_final} m y la velocidad final es de {velocidad_final} m/s")