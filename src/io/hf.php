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

      <div style="font-size: 1.5em;" >
    
        <a href="https://shardhive.com">shardHive.com</a>
        <a href="https://io.shardhive.com/">IO landing page</a>
        <a href="https://io.shardhive.com/login.php">login page</a>
        <a href="https://io.shardhive.com/register.php">registration page</a>
    
      </div>


    </body>

	<?php
	// handleForm.php
  echo '<div class="transactionContainer">';
  $priceETH = 2112;
  $orderSize = $_GET['amount'];
  $orderCost = $orderSize * $priceETH;
	echo '<h2>User: ' . $_GET['username'] . '</h2>';
  echo '<h3>Ordering: ' . $_GET['amount'] . '  ' . $_GET['currency'] . '</h3>';
  echo '<h3>Price of ETH: $' . $priceETH . '</h3>';
  echo '<h3>Cost: $' . $orderCost . '</h3>';
  echo '</div>';

  $cookie1_name = "username";
  $cookie1_value = $_GET['username'];
  setcookie($cookie1_name, $cookie1_value, time() + (86400 * 3000), "/");
  $cookie2_name = "loginDt";
  $cookie2_value = date("m_d_h_i_sa");
  setcookie($cookie2_name, $cookie2_value, time() + (86400 * 3000), "/");


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


  /*
  $sql = "INSERT INTO `jTest` (`name`, `userId`, `ethAddr`, `currencyPref`) VALUES ('" . $_GET['name'] . "', '" . $_GET['amount'] . "', '', '" . $_GET['currency'] . "')";


  if ($conn->query($sql) === TRUE) {
      echo 'created new record successfully';
  } else {
      echo 'error ' . $sql . '<br>' . $conn->error;
  }
  
  $sql1 = "SELECT username, pass, confirmPass FROM jTest";
  $result = $conn->query($sql1);
  if ($result->num_rows > 0) {
      while($row = $result -> fetch_assoc()) {
          $pass0=$row["pass"];
          $pass1=$row["confirmPass"];
          if($pass0 == $pass1){
            echo "<h2>Success Creating Account for : " . $row["username"] . "</h2>"
          } else{
              echo "<h2>Try Again. Passwords do not match</h2>";
          }
      }
  } else {
      echo "0 results";
  }

  */

  $conn->close();
  ?>




</html>
