import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import MLP as model
import numpy as np
from matplotlib.backend_bases import MouseButton


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
    class0Text=ax.text(0.75, 0.9, "Click izquierdo:", transform=fig.transFigure, fontsize=10, color='black')
    class0Text = ax.annotate(" Clase A",xycoords=(class0Text),xy=(1, 0), verticalalignment='bottom', fontsize=10, color='blue')
    class1Text=ax.text(0.75, 0.8, "Click derecho:", transform=fig.transFigure, fontsize=10, color='black')
    class1Text = ax.annotate(" Clase B",xycoords=(class1Text),xy=(1, 0), verticalalignment='bottom', fontsize=10, color='red')
    
    #RaddioButton para seleccionar dataset
    radioAx=plt.axes([0.75, 0.4, 0.1, 0.15])
    radioAx.set_title("Dataset", fontsize=10)
    radioDataset=widgets.RadioButtons(radioAx,('Custom', 'Option 1', 'Option 2'))

    # Botones
    plotButton=widgets.Button(plt.axes([0.75, 0.2, 0.1, 0.15]), 'Train', color='lightblue', hovercolor='skyblue')
    clearButton=widgets.Button(plt.axes([0.75, 0.1, 0.1, 0.05]), 'Clear', color='lightcoral', hovercolor='salmon')
    
    return plotButton, clearButton, radioDataset


#Colocar puntos
puntos=[]
markers=[]
etiquetas=[]
lineas=[]
def onclick(event):
    if event.inaxes == ax:
        if event.button is MouseButton.LEFT:
            x, y = event.xdata, event.ydata
            marker, = ax.plot(x, y, 'bo')  # Dibuja un punto azul en la posición clickeada
            puntos.append((x, y))  # Agrega el punto a la lista de puntos
            markers.append(marker)  # Agrega el objeto del punto a la lista de markers
            etiquetas.append(0)  # Agrega la etiqueta correspondiente a la lista de etiquetas
            fig.canvas.draw()  # Actualiza la figura para mostrar el nuevo punto
        elif event.button is MouseButton.RIGHT:
            x, y = event.xdata, event.ydata
            marker, = ax.plot(x, y, 'ro')  # Dibuja un punto rojo en la posición clickeada
            puntos.append((x, y))  # Agrega el punto a la lista de puntos
            markers.append(marker)  # Agrega el objeto del punto a la lista de markers
            etiquetas.append(1)  # Agrega la etiqueta correspondiente a la lista de etiquetas
            fig.canvas.draw()  # Actualiza la figura para mostrar el nuevo punto


#Limpiar puntos
def clear(event):
    for marker in markers:
        marker.remove()  # Elimina el punto de la figura
    for etiqueta in etiquetas:
        etiquetas.remove(etiqueta)  # Elimina la etiqueta de la lista de etiquetas
    markers.clear()  # Reinicia la lista de markers
    etiquetas.clear()
    puntos.clear() # Reinicia la lista de puntos
    clear_line()  # Limpia la línea de decisión


#Limpiar linea de decision
def clear_line():
    for linea in lineas:
        linea.remove()  # Elimina la línea de la figura
    lineas.clear()  # Reinicia la lista de líneas
    fig.canvas.draw()  # Actualiza la figura para reflejar los cambios


#Añadir puntos en base al dataset seleccionado
def dataset(label):
    clear(None) # Limpia los puntos y la línea de decisión antes de cargar el nuevo dataset
    rng = np.random.default_rng(42)
    if label == 'Option 1':
        # Dataset 1: XOR — Clase 0 en Q1 y Q3, Clase 1 en Q2 y Q4
        q1 = rng.uniform(1, 8, (20, 2))
        q3 = rng.uniform(-8, -1, (20, 2))
        class0 = np.vstack([q1, q3])
        q2 = np.column_stack([rng.uniform(-8, -1, 20), rng.uniform(1, 8, 20)])
        q4 = np.column_stack([rng.uniform(1, 8, 20), rng.uniform(-8, -1, 20)])
        class1 = np.vstack([q2, q4])
        puntos_dataset = [tuple(p) for p in np.vstack([class0, class1])]
        etiquetas_dataset = [0] * 40 + [1] * 40
    elif label == 'Option 2':
        # Dataset 2: Anillos — Clase 0 en círculo interior, Clase 1 en anillo exterior
        angles0 = rng.uniform(0, 2 * np.pi, 40)
        radii0 = rng.uniform(0.5, 3.5, 40)
        class0 = np.column_stack([radii0 * np.cos(angles0), radii0 * np.sin(angles0)])
        angles1 = rng.uniform(0, 2 * np.pi, 40)
        radii1 = rng.uniform(5.5, 9.0, 40)
        class1 = np.column_stack([radii1 * np.cos(angles1), radii1 * np.sin(angles1)])
        puntos_dataset = [tuple(p) for p in np.vstack([class0, class1])]
        etiquetas_dataset = [0] * 40 + [1] * 40
    else:
        # Custom dataset
        return
    # Agrega los puntos del dataset a la figura
    for (x,y), etiqueta in zip(puntos_dataset, etiquetas_dataset):
        color = 'bo' if etiqueta == 0 else 'ro'
        marker, = ax.plot(x, y, color)
        puntos.append((x, y))
        markers.append(marker)
        etiquetas.append(etiqueta)
    
    fig.canvas.draw()  # Actualiza la figura para mostrar los nuevos puntos

fig, ax = crear_figura()
plotButton, clearButton, radioDataset = crear_widgets(fig)
fig.canvas.mpl_connect('button_press_event', onclick)
clearButton.on_clicked(clear)
radioDataset.on_clicked(dataset)
plt.show()