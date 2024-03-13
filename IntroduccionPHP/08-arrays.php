<?php include 'includes/header.php';

//Arreglos indexados

$carrito = ['Tablet','Television', 'Computadora'];

//Agregar un elemento al array indice 3
$carrito[3] = 'Nuevo producto..';

//Añadir elemento nuevo al final
array_push($carrito,'Audifonos');

//Añadir al inicio 
array_unshift($carrito,'Smartwatch');

//Util para ver los contenidos de un array
echo '<pre>';
var_dump($carrito);
echo '</pre>';

//Acceder a un elemento del array
echo $carrito[1];


$vehiculo = array('Timon', 'Asiento','Radio');

array_push($vehiculo,'Espejo');
array_unshift($vehiculo, 'Ventana');

echo '<pre>';
var_dump($vehiculo);
echo '</pre>';



include 'includes/footer.php';