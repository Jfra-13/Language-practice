<?php 
declare(strict_types = 1);
include 'includes/header.php';

function sumar(int $num1 = 0, int $num2 = 0){
    echo $num1 + $num2;
};

sumar(4, 30);




include 'includes/footer.php';