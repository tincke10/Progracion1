<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Input</title>
</head>
<body>
    <form method="post" action="">
        <label for="cancha">Nombre de la cancha:</label>
        <input type="text" id="cancha" name="cancha[]"><br><br>

        <label for="arbitro">Nombre del arbitro:</label>
        <input type="text" id="arbitro" name="arbitro[]"><br><br>

        <label for="fecha">Fecha del partido:</label>
        <input type="date" id="fecha" name="fecha[]"><br><br>

        <label for="telefono">Telefono de la cancha:</label>
        <input type="text" id="telefono" name="telefono[]"><br><br>

        <label for="mail">Mail de la cancha:</label>
        <input type="email" id="mail" name="mail[]"><br><br>

        <input type="submit" value="Submit">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $cancha = $_POST['cancha'];
        $arbitros = $_POST['arbitro'];
        $fecha = $_POST['fecha'];
        $telefono = $_POST['telefono'];
        $mail = $_POST['mail'];

        echo "<h2>Submitted Data:</h2>";
        for ($i = 0; $i < count($cancha); $i++) {
            echo "Entry " . ($i + 1) . ":<br>";
            echo "Cancha: " . htmlspecialchars($cancha[$i]) . "<br>";
            echo "Arbitro: " . htmlspecialchars($arbitros[$i]) . "<br>";
            echo "Fecha: " . htmlspecialchars($fecha[$i]) . "<br>";
            echo "Telefono: " . htmlspecialchars($telefono[$i]) . "<br>";
            echo "Mail: " . htmlspecialchars($mail[$i]) . "<br><br>";
        }
    }
    ?>
</body>
</html>