import threading
import time
import random

semaphore = threading.Semaphore(value=10)
bebidas_disponibles = 10

def maquina_expendora():
    global bebidas_disponibles
    
    while True: 
        if bebidas_disponibles == 0:
            print('La máquina expendedora se quedó sin bebidas')
            break 
            
        print('Máquina expendedora lista, con 10 bebidas disponibles')
        time.sleep(random.uniform(0.5, 2.0))
        
def persona():
    global bebidas_disponibles
    
    with semaphore:
        if bebidas_disponibles > 0:
            bebidas_disponibles -= 1
            print(f'Persona compra una bebida')
            print(f'Quedan {bebidas_disponibles} bebidas disponibles')
            print(f'Persona sale con su bebida')
            time.sleep(random.uniform(1.0, 3.0))

maquina_thread = threading.Thread(target=maquina_expendora)
maquina_thread.start()

threads_personas = []
for i in range(10):
    persona_thread = threading.Thread(target=persona)
    threads_personas.append(persona_thread)
    persona_thread.start()

for persona_thread in threads_personas:
    persona_thread.join()

maquina_thread.join()
