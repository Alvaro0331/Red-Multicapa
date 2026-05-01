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


#Creacion de los widgets
def crear_widgets(fig):
    #Texto de clase
    class0Text=ax.text(0.75, 0.6, "Click izquierdo:", transform=fig.transFigure, fontsize=10, color='black')
    class0Text = ax.annotate(" Clase 0",xycoords=(class0Text),xy=(1, 0), verticalalignment='bottom', fontsize=10, color='blue')
    class1Text=ax.text(0.75, 0.5, "Click derecho:", transform=fig.transFigure, fontsize=10, color='black')
    class1Text = ax.annotate(" Clase 1",xycoords=(class1Text),xy=(1, 0), verticalalignment='bottom', fontsize=10, color='red')
    
    # Botones
    plotButton=widgets.Button(plt.axes([0.75, 0.3, 0.1, 0.15]), 'Train', color='lightblue', hovercolor='skyblue')
    clearButton=widgets.Button(plt.axes([0.75, 0.2, 0.1, 0.05]), 'Clear', color='lightcoral', hovercolor='salmon')
    
    return plotButton, clearButton





fig, ax = crear_figura()
plotButton, clearButton = crear_widgets(fig)
plt.show()