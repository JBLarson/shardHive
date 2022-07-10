<?php
$cookie1_name = "username";
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



    <div class="ioHeaderMenu">
        
        <button class="button ioHeaderMenuObject" onclick="window.location.href='https://shardhive.com'">shardHive.com</button>

        <button class="button ioHeaderMenuObject" onclick="window.location.href='https://io.shardhive.com/'">IO Landing</button>
        
        <button class="button ioHeaderMenuObject" onclick="window.location.href='https://io.shardhive.com/login.php'">IO Login</button>

        <button class="button ioHeaderMenuObject" onclick="window.location.href='https://io.shardhive.com/register.php'"><a>IO Registration</a></button>

    </div>


    <h2>Practice</h2>


    <div>
      <form action="/hf.php">
        <label for="username">Username</label>
        <?php
          echo '<input type="text" id="username" name="username" value="' . $_COOKIE[$cookie1_name] . '">';
        ?>
        <label for="amount">Test Amount</label>
        <input type="text" id="amount" name="amount" placeholder="Test Amount: $">

        <label for="currency">Currency</label>
        <select id="currency" name="currency">

          <option value="ETH">ETH</option>
          <option value="BTC">BTC</option>
        </select>

        <input type="submit" value="Submit">
      </form>
    </div>

  </body>
</html>
