<html lang="en">

    <head>
      <link rel="stylesheet" href="ioStyles.css">
    </head>



    <body>

      <div class="headerContainer">

        <div class="grid-item0">
          <h1>shardHive<br>Testing</h1>
        </div>

        <div class="grid-item1">
            <img src="https://shardhive.com/wp-content/uploads/2022/02/logoTransparent.svg" alt="shardHive Logo">
        </div>
      <div style="font-size: 1.5em;" >
    
        <a href="https://shardhive.com">shardHive.com</a>
        <a href="https://io.shardhive.com/">IO landing page</a>
        <a href="https://io.shardhive.com/login.php">login page</a>
        <a href="https://io.shardhive.com/register.php">registration page</a>
    
      </div>
      </div>
    </body>

	<?php
	// handleLogin.php


  $servername = "ecngx279";
  $username = "shardh5_jTest";
  $password = "tH3SqlTestP@55";
  $dbname = "shardh5_ioTest";

  // Create connection
  $conn = new mysqli($servername, $username, $password, $dbname);
  //$conn = new mysqli($servername, $username, $password);

  // Check connection
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  echo "Connected successfully<br>";

  /**/
  $sql = "INSERT INTO `jTest` (`username`, `pass`, `confirmPass`) VALUES ('" . $_GET['username'] . "', '"  . $_GET['pass'] . "', '"  . $_GET['confirmPass'] . "')";


  if ($conn->query($sql) === TRUE) {
      echo 'created new record successfully';
  } else {
      echo 'error ' . $sql . '<br>' . $conn->error;
  }
  /*
  
  $sql1 = "SELECT name, userId, FROM jTest";
  $result = $conn->query($sql1);
  if ($result->num_rows > 0) {
      while($row = $result -> fetch_assoc()) {
          if ($row['currencyPref'] === 'XMR') {
            echo "<h1>userId: " . $row["userId"] . "</h1><h2> Name: " . $row["name"] . " Crypto Pref: " . $row['currencyPref'] . "</h2><br>";
          }
      }
  } else {
      echo "0 results";
  }
  


  $conn->close();
  
  echo '<div class="transactionContainer">';

  ?>




</html>