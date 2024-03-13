<?php include 'includes/header.php';

$productos = [
    [
        'name' => 'Tablet',
        'price' => '200',
        'available' => true
    ],
    [
        'name' => 'TV 24"',
        'price' => '300',
        'available' => true
    ],
    [
        'name' => 'Curved Monitor',
        'price' => '400',
        'available' => false
    ]
];


echo "<pre>";
var_dump($productos);

$json = json_encode($productos, JSON_UNESCAPED_UNICODE);

$json_array = json_decode($json);

var_dump($json);

var_dump($json_array);
echo "</pre>";















include 'includes/footer.php';