<?php
$cookie1_name = "username";
?>
<html lang="en">


  <head>


    <link rel="stylesheet" href="ioStyles.css">


  </head>
  <body>

      <div class="headerContainer">
        <h1>shardHive Technology</h1>
        <h2>Custom PHP is responsible for all pages on io.shardhive.com</h2>. 
        
        
        <img src="https://shardhive.com/wp-content/uploads/2022/02/logoTransparent.svg" alt="shardHive Logo">
        <h3>Welcome to the Machine</h3>


      </div>
      <!-- end of header container transactionContainer starts-->






      <div class="ioHeaderMenu">
          
          <button class="button ioHeaderMenuObject" onclick="window.location.href='https://shardhive.com'">shardHive.com</button>

          <button class="button ioHeaderMenuObject" onclick="window.location.href='https://io.shardhive.com/'">IO Landing</button>
          
          <button class="button ioHeaderMenuObject" onclick="window.location.href='https://io.shardhive.com/login.php'">IO Login</button>

          <!--button class="button ioHeaderMenuObject" onclick="window.location.href='https://shardhive.com'"><a>shardHive</a></button>

          <button class="button ioHeaderMenuObject" onclick="window.location.href='https://io.shardhive.com/practice.php'"><a>IO PHP Practice</a></button-->



     </div>


    <h2>Submit File</h2>
    

    <div class="fileSubmission">
      <form action="/hf.php" method="post" enctype="multipart/form-data">
          <label for="userId">userId</label>
          <input type="text" id="userId" name="userId" placeholder="00001">
          <label for="fileName">File Name</label>
          <input type="text" id="fileName" name="fileName" placeholder="test.json">

          <label for="fileUpload">File Upload</label>
          <input type="file" id="fileUpload" name="fileUpload">

        </select>

        <input type="submit" value="uploadFile" name="submit">
      </form>
    </div>

  </body>
  
  

  <script>
    function setCookie(cookieName,value,expirationDays){
      let date = new Date();
      date.setTime(date.getTime() + (expirationDays*86400000));
      let expires = "expires=" + date.toUTCString();
      document.cookie = cookieName + "=" + value + ";" + expires + ";path=/" + ";domain=.io.shardHive.com";
    }

    let date = new Date();
    let theDt = date.setTime(date.getTime() + (1200*86400000));
    let theDate = date.toUTCString();

    let setTest3 = setCookie('jb3', theDate, theDt);
  </script>


  
</html>
