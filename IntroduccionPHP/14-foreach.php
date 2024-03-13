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

foreach ($productos as $producto) { ?>
    

    <li>
        <p>Product: <?php echo $producto['name']; ?></p>
        <p>Price: <?php echo $producto['price']; ?></p>
        <p>Avaliable: <?php echo ($producto['available']) ? 'Available' : 'Not Available' ; ?> </p>
    </li>
    <?php

}


include 'includes/footer.php';