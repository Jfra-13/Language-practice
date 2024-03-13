<?php include 'includes/header.php';

$autenticado = true;
$admin = false;

if($autenticado || $admin) {
    echo "Usuario autenticado correctamente";
} else {
    echo "Usuario no autenticado, inicia sesion";
}
echo "<br>";
//if anidado...
$cliente = [
    'nombre' => 'Juan',
    'saldo' => 200,
    'informacion' => [
        'tipo' => 'Premium'
    ]
];
//Empty verifica si una variable esta vacia
if (!empty($cliente)) {
    echo "Arreglo del cliente completo";
    echo "<br>";
    if ($cliente['saldo'] > 0) {
    echo "Cuenta con saldo disponible";
    } else {
    echo "No hay saldo";
    }
}

//else if...
echo "<br>";
if($cliente['saldo'] > 0){
    echo "El cliente tiene saldo";
} else if ($cliente['informacion']['tipo'] === 'Premium'){
    echo "El cliente es Premium";
} else {
    echo "No hay cliente definido o no tiene saldo o no es premium";
}


//Switch.
echo "<br>";
$tecnologia = 'JavaScript';
switch ($tecnologia){
    case 'PHP':
        echo "PHP, un excelente lenguaje!!";
        break;
    case 'JavaScript':
        echo "Genial, lenguaje de la red...";
        break;
    case 'HTML5':
        echo "Emmmm";
        break;
    default: 
        echo "Algun lenguaje que no se cual es";
        break;

}


include 'includes/footer.php';