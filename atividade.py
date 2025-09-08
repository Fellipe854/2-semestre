import threading
import time

# Função para a Thread-1, que imprime de 1 a 10
def imprimir_sequencia_1():
    """Imprime os números de 1 a 10, com um pequeno atraso."""
    print("Iniciando Thread-1")
    for i in range(1, 11):
        print(f"Thread-1: {i}")
        time.sleep(0.5)  # Simula tempo de processamento
    print("Finalizando Thread-1")

# Função para a Thread-2, que imprime de 50 a 60
def imprimir_sequencia_2():
    """Imprime os números de 50 a 60, com um pequeno atraso."""
    print("Iniciando Thread-2")
    for i in range(50, 61):
        print(f"Thread-2: {i}")
        time.sleep(0.5)  # Simula tempo de processamento
    print("Finalizando Thread-2")

# --- Programa Principal ---
if __name__ == "__main__":
    print("Iniciando o programa principal.")

    # Cria as threads
    thread1 = threading.Thread(target=imprimir_sequencia_1)
    thread2 = threading.Thread(target=imprimir_sequencia_2)

    # Inicia as threads
    thread1.start()
    thread2.start()

    # Garante que o programa principal só termine após as threads
    # usarem o método .join()
    print("Aguardando as threads terminarem...")
    thread1.join()
    thread2.join()

    print("Programa principal finalizado. Todas as threads terminaram.")