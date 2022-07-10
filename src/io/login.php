<?php
$cookie_name = "nameTrackingCookie";
$cookie_value = "fucking yert";
setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
?>
<html lang="en">
  <head>
    <link rel="stylesheet" href="ioStyles.css">
  </head>
  <body>

    <div class="headerContainer">

      <div class="grid-item0">
        <h1>Welcome to<br>shardHive</h1>
      </div>

        <div class="grid-item1">
          <img src="https://shardhive.com/wp-content/uploads/2022/02/logoTransparent.svg" alt="shardHive Logo">
        </div>
    </div>
    <!-- end of header container transactionContainer starts-->

    <h1>Test Login Form for PHP and SQL practice</h1>
    <br>
    <div style="font-size: 1.5em; " ><a href="https://io.shardhive.com/login.php">login page</a></div>
    <?php
    if(!isset($_COOKIE[$cookie_name])) {
      echo "<h2>Testing Cookie named '" . $cookie_name . "' is not set!</h2>";
    } else {
      echo '<form action="/handleIt.php">';
        echo '<label for="name">Name</label>';
        echo '<input type="text" id="name" name="name" value="' . $_COOKIE[$cookie_name] . '">';
      echo '</form>';
      echo "<h2>Cookie '" . $cookie_name . "' is set!<br></h2>";
      echo "<h2>Value is: " . $_COOKIE[$cookie_name] . "</h2>";
    }
    ?>
    <div>
      <form action="/handleLogin.php">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" placeholder="Name">

        <label for="pass">Password</label>
        <input type="text" id="pass" name="pass" placeholder="pass">

        <label for="userId">userId</label>
        <input type="text" id="userId" name="userId" placeholder="userId: ">

        <label for="currency">Currency</label>
        <select id="currency" name="currency">

          <option value="ETH">ETH</option>
          <option value="BTC">BTC</option>
          <option value="KAVA">KAVA</option>
          <option value="XMR">XMR</option>

        </select>

        <input type="submit" value="Submit">
      </form>
    </div>

  </body>
</html>
