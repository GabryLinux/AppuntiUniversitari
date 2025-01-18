import numpy as np


def filtro_equazione_differenze(a, b, x):
    """
    Calcola l'output di un filtro tramite equazione alle differenze.
    
    :param a: Coefficienti del feedback (-a_i, a[0] = 1 per normalizzazione).
    :param b: Coefficienti del feedforward (b_j).
    :param x: Segnale di input (numpy array o lista).
    :return: Output del filtro (numpy array).
    """
    # Convertiamo x in numpy array per semplicità
    x = np.array(x)
    
    # Lunghezza del segnale
    L = len(x)
    
    # Numero di coefficienti del feedback e feedforward
    N = len(a)  # Coefficienti feedback
    M = len(b)  # Coefficienti feedforward
    
    # Inizializziamo l'output y con zeri
    y = np.zeros(L)
    
    # Iterazione sui campioni del segnale
    for n in range(L):
        # Feedback: Somma pesata dei valori passati di y[n-i]
        feedback = sum(-a[i] * y[n-i] if n-i >= 0 else 0 for i in range(1, N))
        
        # Feedforward: Somma pesata dei valori passati di x[n-j]
        feedforward = sum(b[j] * x[n-j] if n-j >= 0 else 0 for j in range(M))
        
        # Combinazione di feedforward e feedback
        y[n] = feedback + feedforward
    
    return y

# Esempio di utilizzo
a = [0]  # Coefficienti del feedback (a_0=1, a_1=-0.5)
b = [-1,-1,0,1,3]  # Coefficienti del feedforward (b_0=0.2, b_1=0.5)
x = [ 1, 0, 1]  # Segnale di input (impulso unitario)

y = filtro_equazione_differenze(a, b, x)
print("Output del filtro:", y)