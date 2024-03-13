<?php include 'includes/header.php';

$nombreCliente = 'Juan Francisco';

//Conocer la extension de un string
echo strlen($nombreCliente);
var_dump($nombreCliente);

//Eliminar espacios en blanco
$texto = trim($nombreCliente);
echo strlen($texto);

//Convertir a mayuscula
echo strtoupper($nombreCliente);

//Convertir en minuscula
echo strtolower($nombreCliente);

//Ejemplo de uso para mayusculas y minusculas
$mail1 = 'correo@correo.com';
$mail2 = 'Correo@correo.com';
var_dump(strtolower($mail1)===strtolower($mail2));

//Reemplazo Juan por la 'J' en la variable $nombreCliente
echo str_replace('Juan', 'J',$nombreCliente);

//Revisar si un string existe o no
echo strpos($nombreCliente,'Juan');

$tipoCliente = 'Premium';
echo '<br/>';
echo 'El cliente ' . $nombreCliente . ' es ' . $tipoCliente;

include 'includes/footer.php';