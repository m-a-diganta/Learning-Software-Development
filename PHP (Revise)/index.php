<?php
    include("header.html");
    session_start(); // for accessing _SESSION variables
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homepage</title>
</head>
<body>
    <br><br><br>
    <form action="<?php htmlspecialchars($_SERVER["PHP_SELF"]) ?>" method="post"> <!-- Shouldnt use get - security purpose -->
        <label>Username:</label><br>
        <input type="text" name="username"><br>
        <label>Password:</label><br>
        <input type="password" name="password"><br>
        <label>Email:</label><br>
        <input type="text" name="email"><br>
        <label>Age:</label><br>
        <input type="text" name="age"><br>

        <label>Value of X:</label><br>
        <input type="text" name="x"><br>
        <label>Value of Y:</label><br>
        <input type="text" name="y"><br>

        <input type="radio" name="job" value="student"> Student<br>
        <input type="radio" name="job" value="employed"> Employed<br>
        <input type="radio" name="job" value="unemployed"> Unemployed<br>

        <input type="checkbox" name="Java" value="Java"> Java<br>
        <input type="checkbox" name="Python" value="Python"> Python<br>
        <input type="checkbox" name="Javascript" value="Javascript"> Javascript<br>

        <input type="checkbox" name="items[]" value="item1"> item1<br>
        <input type="checkbox" name="items[]" value="item2"> item2<br>
        <input type="checkbox" name="items[]" value="item3"> item3<br>

        <input type="submit" name="submit" value="Submit here"><br>
        <hr>
    </form>

</body>
</html>

<?php
    echo"<br><br><br>";
    // Variables in PHP
    $name = "Arabi Hossain";
    echo $name."<br>";
    echo "Full name: {$name} Ahil<br>";
    $age=14;
    echo"Age: {$age} years<br>";
    $student = true;
    $employed = false;
    echo"Student? => {$student}, Employed? => {$employed} <br><br>";
    echo"<hr>";

    // Arithmetic Operations
    $x = 10;
    $y = 5;
    $z=$x+$y;
    echo $z."<br>";
    $counter= 5;
    $counter++;
    echo $counter."<br>";
    $counter-=2;
    echo $counter."<br><br>";
    // Operator Precedence  ()   **    *,/,%   +,-
    echo"<hr>";


    // GET => URL, not secure, char limit, can be bookmarked, cached, for search page
    // POST => secured, no data limit, cant be bookmarked, not cached, for credentials

    // echo "Username: {$_GET["username"]}<br>";
    // echo "Password: {$_GET["password"]}<br>";
    echo "Username: {$_POST["username"]}<br>";
    echo "Password: {$_POST["password"]}<br>"; //isset()
    echo"<hr>";


    // Math functions: abs,round,floor,ceil,sqrt,pow,mzx,min,pi(),rand()
    $total = null;
    echo $total."<br>";
    $x = $_POST["x"];
    echo "X = {$x}<br>";
    $y = $_POST["y"];
    echo "Y = {$y}<br>";
    $abs_x = abs($x);
    $round_x = round($x); // floor,ceil
    echo "Absolute Value = {$abs_x}<br>";
    echo "Rounded Value = {$round_x}<br>";
    $product = pow($x,$y);
    echo"Product = {$product}<br>";
    $random = rand(1,100);
    echo"A random number: {$random}<br>";
    echo"<hr>";


    // If-else
    $marks= rand(-10,110);
    // $marks=100;
    echo"Marks = {$marks}<br>";
    $invalid=false;
    if($marks>100 || $marks<0){ // and => &&
        echo"Invalid<br>";
        $invalid=true;
    }
    elseif(!$invalid && $marks==100){
        echo"Congrats you got full marks!";
    }
    elseif($marks>50){
        echo"You have passed<br>";
    }
    else{
        echo"You have failed<br>";
    }
    echo"<hr>";


    // Switch
    $grade= "B";
    switch($grade){
        case "A":
            echo"You did great<br>";
            break;
        case "B":
            echo"Good score<br>";
            break;
        case "C":
            echo"Need to improve<br>";
            break;
        default:
            echo"Not valid";
    }
    echo"<hr>";


    // for loop
    for($i=0;$i<=9;$i++){
        echo"$i";
    }
    echo"<br>";


    //while loop
    $c=11;
    while($c<=20){
        echo"$c,";
        $c++;
    }
    echo"<br>";
    echo"<hr>";




    // Array
    $markList = array(100,60,87,90);
    // echo $markList."<br>";
    echo $markList[2]."<br>";
    // echo $markList[5]."<br>";
    foreach($markList as $mark){
        echo $mark.",";
    }
    echo "<br>";

    array_push($markList, 80, "invalid", 65);
    foreach($markList as $mark){
        echo $mark.",";
    }
    echo "<br>";  //array_pop,shift,reverse


    // Associative Array
    $ages = array("Ahil"=>14, "Shoumick"=> 20, "Alfessani"=> 24);
    echo $ages["Shoumick"]."<br>";
    foreach($ages as $key=>$value){
        echo"{$key} is {$value} years old<br>";
    }
    echo"-------<br>";
    array_pop($ages);
    $ages["Junayed"]=7;
    foreach($ages as $key=>$value){
        echo"{$key} is {$value} years old<br>";
    }
    $ages_keys = array_keys($ages); //array_values,array_flip
    foreach($ages_keys as $key){
        echo $ages[$key]."<br>";
    }
    echo"<hr>";


    // isset() => returns true if variable is declared and not null
    //  empty() => returns true if variable isnt declared, false, null, ""
    $var1 = false;
    if(isset($var1)){
        echo"The variable is set<br>";
    }
    else{
        echo"The variable is NOT set<br>";
    }

    // foreach($_POST as $key => $value){
    //     echo"{$key} = {$value} <br>";
    // }

    if (isset($_POST["submit"])){
        $username = $_POST["username"];
        $password = $_POST["password"];
        if (empty($username)){
            echo"Username is missing<br>";    
        }
        elseif (empty($password)){
            echo"{$username} your Password is missing<br>";    
        }
        else{
            echo"Hello {$username}<br>";
        }
    }
    else{
        echo "You didnt use the submit button";
    }
    echo"<hr>";


    // Radio Buttons
    if (isset($_POST["submit"])){
        $job = null;
        if (isset($_POST["job"])){
            $job = $_POST["job"];
            echo"You are currently {$job}<br>";
        }
        else{
            echo"Select an option";
        }
    }
    echo"<hr>";

    // Checkbox
    if (isset($_POST["submit"])){
        if (isset($_POST["Java"])){
            $lang1 = $_POST["Java"];
            echo"You want to learn {$lang1}<br>";
        }
        if (empty($_POST["Java"])){
            echo"You dont want to learn Java<br>";
        }
        if (isset($_POST["Python"])){
            $lang2 = $_POST["Python"];
            echo"You want to learn {$lang2}<br>";
        }
        if (empty($_POST["Python"])){
            echo"You dont want to learn Python<br>";
        }
        if (isset($_POST["Javascript"])){
            $lang3 = $_POST["Javascript"];
            echo"You want to learn {$lang3}<br>";
        }
        if (empty($_POST["Javascript"])){
            echo"You dont want to learn Javascript<br>";
        }
    }

    $items = $_POST["items"];
    foreach($items as $item){
        echo $item."<br>";
    }
    echo"<hr>";


    // Function
    function is_prime($num){
        $count=0;
        for($i=1;$i<=$num;$i++){
            if($num % $i == 0){
                $count++;
            }
        }
        if($count == 2){
            return "Prime<br>";
        }
        else{
            return "Not Prime<br>";
        }
    }
    echo is_prime(9);



    // String Functions
    $st = "This is a Random string";
    $st_count = strlen($st);
    $st_index = strpos($st, "n");
    $sub_st = substr($st, 1, 3);
    echo"String = {$st}<br>";
    echo"Position of 'n' = {$st_index}<br>";
    echo"String length = {$st_count}<br>";
    echo"Sub String = {$sub_st}<br>";

    $st_array = explode(" ",$st);
    foreach($st_array as $char){
        echo $char.", ";
    }; // implode converts array into string

    // strlen, strpos, substr, explode, implode, strtolower, strtoupper, trim, str_pad, str_replace, strrev, str_shuffle, strcmp
    echo"<br>";
    echo"<hr>";


    // Sanitize/ Validate Input
    //Sanitization
    $filtered_username = filter_input(INPUT_POST, "username", FILTER_SANITIZE_SPECIAL_CHARS );
    $filtered_password = filter_input(INPUT_POST, "password", FILTER_SANITIZE_ADD_SLASHES );
    $filtered_email = filter_input(INPUT_POST, "email", FILTER_SANITIZE_EMAIL );
    echo"Hello {$filtered_username}<br> Your Password is {$filtered_password}<br> Your Email is {$filtered_email}<br>";
    //Validation
    $filtered_age = filter_input(INPUT_POST, "age", FILTER_VALIDATE_INT );
    if(empty($filtered_age)){
        echo"The number is invalid<br>";
    }
    else{
        echo"You are {$filtered_age} years old<br>";
    }

    $filtered_email = filter_input(INPUT_POST, "email", FILTER_VALIDATE_EMAIL);
    if(empty($filtered_email)){
        echo"Email is invalid<br>";
    }
    else{
        echo"Your email is {$filtered_email} <br>";
    } 
    echo"<hr>";



    //setting cookies

    // Session - for accessing global variables
    if($_SERVER["REQUEST_METHOD"]=="POST"){
        $_SESSION["username"] = $filtered_username;
        $_SESSION["password"] = $filtered_password;
        $_SESSION["age"] = $filtered_age;
    }
    echo $_SESSION["username"]."<br>";
    echo $_SESSION["password"]."<br>";
    echo $_SESSION["age"]."<br>"; // can use session_destroy to remove the saved values - for example logout
    echo"<hr>";



    // Hashing
    $pass = "5632154jghjg";
    $hashed_pass = password_hash($pass, PASSWORD_DEFAULT);
    if(password_verify("random pass",$hashed_pass)){
        echo"Your password matched";
    }
    else{
        echo"You entered wrong password";
    }



    include("footer.html");


?>