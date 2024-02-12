import threading
import time

semaphore = threading.Semaphore(1)

shared_resource = 0

def critical_section():
    global shared_resource
    semaphore.acquire()
    
    try:
        print(f'{threading.current_thread().name} entró a la sección crítica')
        shared_resource += 1
        time.sleep(2)
        print(f'{threading.current_thread().name} salió de la sección crítica. Recurso compartido: {shared_resource}')
    finally:
        semaphore.release()

def worker():
    for _ in range(3): 
        critical_section()

thread1 = threading.Thread(target=worker, name='Hilo 1')
thread2 = threading.Thread(target=worker, name='Hilo 2')


thread1.start()
thread2.start()

thread1.join()
thread2.join()
