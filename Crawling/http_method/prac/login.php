<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HUFS Missing Semester</title>
</head>
<body>
    <?php
    if($_POST["id"] and $_POST["pwd"]) {
        $id = $_POST["id"];
        $pwd = $_POST["pwd"];
    }
    else {
        $id = $_GET["id"];
        $pwd = $_GET["pwd"];
    }
    
    echo '아이디는 '. $id . '입니다.';
    echo nl2br("\n");
    echo '비밀번호는 '. $pwd .'입니다.';

    ?>
</body>
</html>