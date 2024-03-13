<?php 
declare (strict_types = 1);
include 'includes/header.php';

function authenticatedUser (bool $authenticated ) : string {
    if ($authenticated) {
        return "The user is authenticated";
    } else {
        return "Not authenticated";
    }
}

$user = authenticatedUser(false);
echo $user;

include 'includes/footer.php';