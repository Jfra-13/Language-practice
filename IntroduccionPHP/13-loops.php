<?php include 'includes/header.php';

//While

$i = 0;

while($i < 10){//Primero revisa la condicion luego ejecuta el codigo

    echo $i . "<br>";

    $i++;
}

echo '<br>';

//Do while
$i = 0;

do {
    echo $i . "<br>";//Primero revisa el codigo luego la condicion

    $i++;
} while ($i < 10);

echo "<br>";



//for loop.
for ($i = 1; $i < 50; $i++) { //Inicializador , condicion , incremento 
    if($i % 15 === 0){
        echo $i . "Fizz Buzz <br/>";
    } else if($i % 3 === 0){
        echo $i . "-Fizz <br/>";
    } else if ($i % 5 === 0){
        echo $i . "-Buzz <br/>";
    } else {
        echo $i . "<br/>";
    }
}

//for each
$clientes = array('Pedro','Juan', 'Karen');

foreach ($clientes as $cliente) {
    echo $cliente . '<br/>';
}

"<br/>";

for ($i = 0; $i < count($clientes); $i++){
    echo $clientes[$i] . "<br/>";
}

$cliente = [
    'nombre' => 'Juan',
    'saldo' => 200,
    'tipo' => 'Premium'
];
foreach($cliente as $key => $valor):
    echo $key . ' - '. $valor . '<br/>';
endforeach;

include 'includes/footer.php';