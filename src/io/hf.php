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
      
      </div>

    </body>

	<?php
	// handleForm.php
  echo '<div class="transactionContainer">';
  $priceETH = 2112;
  $orderSize = $_GET['amount'];
  $orderCost = $orderSize * $priceETH;
	echo '<h2>User: ' . $_GET['name'] . '</h2>';
  echo '<h3>Ordering: ' . $_GET['amount'] . '  ' . $_GET['currency'] . '</h3>';
  echo '<h3>Price of ETH: $' . $priceETH . '</h3>';
  echo '<h3>Cost: $' . $orderCost . '</h3>';
  echo '</div>';



  echo 'testing sql connection';
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



  $sql = "INSERT INTO `jTest` (`name`, `userId`, `ethAddr`, `currencyPref`) VALUES ('" . $_GET['name'] . "', '" . $_GET['amount'] . "', '', '" . $_GET['currency'] . "')";


  if ($conn->query($sql) === TRUE) {
      echo 'created new record successfully';
  } else {
      echo 'error ' . $sql . '<br>' . $conn->error;
  }


  $conn->close();
  ?>




</html>
