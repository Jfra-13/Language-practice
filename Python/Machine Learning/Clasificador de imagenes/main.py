from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import tensorflow as tf
# from keras.utils import np_utils

import matplotlib.pyplot as plt
import numpy as np


# Lectura, visualizacion y pre-procesamiento de datos
#  Primera tupla contiene los dato de entrenamiento
#  Segunda tupla contiene los datos de prueba
(x_train, y_train), (x_test, y_test) = mnist.load_data()


# Visualizaremos 16 imagenes aleatorias tomadas del set x_train
#  Linea 1 -> Genera 16 enteros (Entre 0 y el numero de imagenes [60000])
#  Linea 2 -> Recorre los 16 y muestra las imagenes
#       plt.subplot crea una subparcela con 4 fil 4 col
#       plt.imshow muestra la imagen en escala de grises
#       plt.axis oculta las etiquetas de los ejes
#       plt.title agrega un titulo a la trama secundaria
# linea 3 y 4 -> Agrega titulo a la figura y la muestra

ids_imgs = np.random.randint(0, x_train.shape[0], 16)
for i in range(len(ids_imgs)):
    img = x_train[ids_imgs[i], :, :]
    plt.subplot(4, 4, i+1)
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.title(y_train[ids_imgs[i]])
plt.suptitle('16 imagenes del set MNIST')
plt.show()

# Pre-procesamiento para introducirlas a la red neuronal
# Remodela los datos de entrenamiento de una matriz 2D a una matriz 1D
X_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1]*x_train.shape[2]))
X_test = np.reshape(x_test, (x_test.shape[0], -1))

# Dividimos cada valor de pixel por 255
# Motivo: Hace que los datos sean mas coherentes y mejora el rendimiento
# Normalizamos las intensidades al rango 0-1
X_train = X_train/255.0
X_test = X_test/255.0

# Definimos el numero de clases en 10
# Convierte las etiquetas de entrenamiento y prueba a un formato codificado de un solo golpe
nclasses = 10
Y_train_one_hot = tf.keras.utils.to_categorical(y_train, nclasses)
Y_test_one_hot = tf.keras.utils.to_categorical(y_test, nclasses)

# Reinicio de la semilla aleatoria para reproducir el entrenamiento
# Definen las dimenciones de entrada y salida del modelo
# Dimencion de entrada: numero de caracteristicas en los datos
# Dimencion de salida: numero de clases en los datos
np.random.seed(1)
input_dim = X_train.shape[1]
output_dim = X_test.shape[1]


# Creacion del modelo secuencial (secuencia de capas)
modelo = Sequential()

# Añadimos una capa densa de 15 neuronas al modelo
# input_dim especifica numero de caracteristicas 'datos de entrada'
# activacion='relu' -> activa la unidad lineal rectificada (ReLU)
modelo.add(Dense(15, input_dim=input_dim, activation='relu'))
# Añadimos una capa densa con output_dim
# Softmax se usa para problemas de clasificacion
modelo.add(Dense(nclasses, activation='softmax'))
# Imprime un resumen del modelo
# Incluye: numero de parametros del modelo, la forma de cada capa, funcion de activacion
print(modelo.summary())

# Controlamos la rapidez con la que aprende el modelo usando SGD y lr
# sgd = SGD(lr=0.2)

# loss='categorical_crossentropy' especifica la función de pérdida que debe utilizarse.
# La función de pérdida se utiliza para medir el error entre la salida prevista del modelo y la salida real.
# optimizer=sgd especifica el optimizador que debe utilizarse
# metrics=['accuracy'] especifica la métrica que debe utilizarse
modelo.compile(loss='categorical_crossentropy', optimizer=SGD(learning_rate=0.2), metrics=['accuracy'])

# El modelo se entrena durante 50 epocas (retroaliemto de datos) usando un tamaño de lote (actualizaciones) 1024
num_epochs = 50
batch_size = 1024
# El parámetro verbose puede establecerse en 0, 1 ó 2. Un valor de 0 significa que no se imprimirá ninguna
# salida durante el entrenamiento. Un valor de 1 imprimirá el progreso del entrenamiento después de cada época.
# Un valor de 2 imprimirá el progreso del entrenamiento después de cada lote.
historia = modelo.fit(X_train, Y_train_one_hot, epochs=num_epochs, batch_size=batch_size, verbose=2)
# historia contiene el historial del modelo, que incluye los valores de pérdida y precisión de cada iteración.

# Parcela que representa la perdida del modelo en funcion del numero de interaciones
plt.subplot(1, 2, 1)
plt.plot(historia.history['loss'])
plt.title('Perdida vs Iteraciones')
plt.ylabel('Perdida')
plt.xlabel('Iteracion')

# Parcela que representa la precision del modelo en funcion del numero de iteraciones
plt.subplot(1, 2, 2)
plt.plot(historia.history['accuracy'])
plt.title('Precision vs Iteraciones')
plt.ylabel('Precision')
plt.xlabel('Iteracion')

plt.show()

# Evaluamos el modelo en conjunto de validacion
# Devuelve una tupla de dos valores: Perdida y precision
# verbose controla si el progreso de la evaluacion se imprime o no en consola
puntaje = modelo.evaluate(X_test, Y_test_one_hot, verbose=0)
print('Precision en el set de validacion:{:.1f}%'.format(100*puntaje[1]))

# Predice las etiquetas de las imagenes del conjunto de validacion
# El metodo predict devuelve una matriz de probabilidades, donde cada fila corresponde a una sola imagen
# argmax devuelve el valor maximo de cada fila
Y_pred_prob = modelo.predict(X_test)
Y_pred = np.argmax(Y_pred_prob, axis=1)


# linea 1 -> generamos 9 indices aleatorios del conjunto de validacion ( Evalua el rendimiento del modelo )
# linea 2 -> comenzamos un bucle sobre los 9 indices aleatorios
# linea 3 -> asiganmos el indice actual en el bucle a la variable idx
# linea 4 -> Recuperamos la imagen del indice actual y redimencionamos a un tamaños 28x28
# linea 5 -> Se codifica la etiqueta y se devuelve el indice con el valor mas alto
# linea 6 -> Recupera la prediccion para la imagen actual
# linea 7 -> Crea una subtrama igual al indice actual del bucle + 1
# linea 8 -> muestra la imagen en escala de grises
# linea 9 -> oculta los ejes de la subtrama
# linea 10 -> mustra la etiqueta original y la prediccion del modelo para cada imagen
# linea 11 -> Titulo de la imagen
# linea 12 -> muestra el grafico completo
ids_imgs = np.random.randint(0, X_test.shape[0], 9)
for i in range(len(ids_imgs)):
    idx = ids_imgs[i]
    img = X_test[idx, :].reshape(28, 28)
    cat_original = np.argmax(Y_test_one_hot[idx, :])
    cat_prediccion = Y_pred[idx]

    plt.subplot(3, 3, i+1)
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.title('"{}"clasificado como"{}"'.format(cat_original, cat_prediccion))
plt.suptitle('Ejemplos de clasificacion en el set de validacion')
plt.show()
