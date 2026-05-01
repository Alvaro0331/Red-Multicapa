import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import MLP as model
import numpy as np


# Creacion de la figura
def crear_figura():
    fig = plt.figure(figsize=(10, 6))
    ax = plt.axes([0.1, 0.1, 0.6, 0.8]) # [left, bottom, width, height]
    ax.set_title("Práctica 4: MLP")
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlabel("X2", fontsize=12)
    ax.set_ylabel("X1", fontsize=12)
    #Dibujo de ejes
    ax.axhline(y=0, color='black', linewidth=0.7)
    ax.axvline(x=0, color='black', linewidth=0.7)
    
    #Leyenda
    leyenda = [
        plt.Line2D([0], [0], marker='o', color='w', label='Clase A', markerfacecolor='blue', markersize=8),
        plt.Line2D([0], [0], marker='o', color='w', label='Clase B', markerfacecolor='red', markersize=8),
        plt.Line2D([0], [0], linestyle='-', color='green', label='Frontera'),
    ]
    ax.legend(handles=leyenda, loc='upper right', fontsize=8)
    return fig, ax


fig, ax = crear_figura()
plt.show()