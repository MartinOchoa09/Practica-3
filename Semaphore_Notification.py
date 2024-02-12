import threading
import time

class RecursoCompartido:
    def __init__(self):
        self.semaphore = threading.Semaphore(value=1)
        self.valor = 0
        self.condicion = threading.Condition()

    def incrementar_valor(self):
        with self.semaphore:
            self.valor += 1
            
    def es_valor_par(self):
        return self.valor % 2 == 0

    def obtener_valor(self):
        with self.semaphore:
            return self.valor

    def notificar_cambio(self):
        with self.condicion:
            self.condicion.notify()

def productor(recurso_compartido):
    for _ in range(5):
        time.sleep(1)
        recurso_compartido.incrementar_valor()
        print(f"Producido: {recurso_compartido.obtener_valor()}")
        recurso_compartido.notificar_cambio()

def consumidor(recurso_compartido):
    with recurso_compartido.condicion:
        try:
            recurso_compartido.condicion.wait_for(recurso_compartido.es_valor_par)
            print(f"Consumido: {recurso_compartido.obtener_valor()}")
        except threading.ThreadError as e:
            print(f"Error en el consumidor: {e}")

recurso_compartido = RecursoCompartido()

hilo_productor = threading.Thread(target=productor, args=(recurso_compartido,))
hilo_consumidor = threading.Thread(target=consumidor, args=(recurso_compartido,))

hilo_productor.start()
hilo_consumidor.start()

hilo_productor.join()
hilo_consumidor.join()
