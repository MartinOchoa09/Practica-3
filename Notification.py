import threading
import time
import random

condicion = threading.Condition()
num_compras = 10
bebidas_disponibles = 10

def maquina_expendora():
    global bebidas_disponibles
    
    while True: 
        with condicion:
            if bebidas_disponibles == 0:
                print('La máquina expendedora se quedo sin bebidas')
                break 
            
            print('Máquina expendedora lista, con 10 bebidas disponibles')
            condicion.notify_all()
        
        time.sleep(random.uniform(0.5, 2.0))
        
def persona():
    global bebidas_disponibles
    
    with condicion:
        condicion.wait()
        if bebidas_disponibles > 0:
            bebidas_disponibles -= 1
            print(f'Persona compra una bebida')
            print(f'Quedan {bebidas_disponibles} bebidas disponibles')
            time.sleep(random.uniform(1.0, 3.0))
            print(f'Persona sale con su bebida')

maquina_thread = threading.Thread(target=maquina_expendora)
maquina_thread.start()

threads_personas = []
for i in range(num_compras):
    persona_thread = threading.Thread(target=persona)
    threads_personas.append(persona_thread)
    persona_thread.start()

for persona_thread in threads_personas:
    persona_thread.join()

maquina_thread.join()