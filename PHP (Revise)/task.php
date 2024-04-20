<?php
    include("header.html");
    session_start();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>task</title>
</head>
<body>
    <br><br><br>
    <h1 style="text-align: center;">Task Page</h1>
</body>
</html>

<?php
    echo $_SESSION["username"]."<br>";
    echo $_SESSION["password"]."<br>";
    echo $_SESSION["age"]."<br>";

    include("footer.html");
?>