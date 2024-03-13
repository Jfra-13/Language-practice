<?php include 'includes/header.php';

$clientes = [];
$clientes2 = array();
$clientes3 = array('Pedro','Juan','Karen');
$clientes = [
    'nombre' => 'Juan',
    'saldo' => 200
];
//Empty
var_dump( empty($clientes) );
var_dump( empty($clientes3) );
var_dump( empty($clientes2) );

//Isset
echo "<br/>";
var_dump( isset($clientes4));
var_dump( isset($clientes));
var_dump( isset($clientes2));
var_dump( isset($clientes3));

echo "<br/>";
var_dump( isset($clientes['nombre']) );
var_dump( isset($clientes['codigo']) );

include 'includes/footer.php';