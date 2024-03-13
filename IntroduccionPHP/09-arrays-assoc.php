<?php include 'includes/header.php';

$cliente = [
    'nombre' => 'Juan',
    'saldo' => 200,
    'informacion' => [
        'tipo' => 'premium',
        'disponible' => 100
    ],
    'dni' => '8287343'
];

$cliente['codigo'] = 232426;

echo '<pre>';
var_dump($cliente);
echo

include 'includes/footer.php';