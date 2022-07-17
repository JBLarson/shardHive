<?php
  echo '<head>';
    echo '<link rel="stylesheet" href="ioStyles.css">';
  echo '</head>';


$targetDir = "hiveIO/";
$targetFile = $targetDir . basename($_FILES["fileUpload"]["name"]);
$uploadOk = 1;
$theFileType = strtolower(pathinfo($targetFile,PATHINFO_EXTENSION));


// Check if file already exists
if (file_exists($targetFile)) {
  echo "File already exists.";
  $uploadOk = 0;
}

// Check file size
if ($_FILES["fileUpload"]["size"] > 500000) {
  echo "Sorry, your file is too large.";
  $uploadOk = 0;
}

// Allow certain file formats
if($theFileType != "csv" && $theFileType != "txt" && $theFileType != "xml" && $theFileType != "json" ) {
  echo "Sorry, only JSON, CSV, TXT, and XML files are allowed.";
  $uploadOk = 0;
}

// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
  echo "<br>Your file was not uploaded.";
// if everything is ok, try to upload file
} else {
  if (move_uploaded_file($_FILES["fileUpload"]["tmp_name"], $targetFile)) {
    echo "The file ". htmlspecialchars( basename( $_FILES["fileUpload"]["name"])). " has been uploaded.";
  } else {
    echo "Sorry, there was an error uploading your file.";
  }
}



echo '<br><br>';
echo 'Attempted to upload' . $targetFile;
echo '<h2>User: ' . $_FILES['fileName'] . '.</h2>';

//echo '<br><br><br>';
//$fileContents = readfile($targetFile);
//echo '<br><br>';


$fcFile = fopen($targetFile, "r") or die("unable to open file");
$fc = fread($fcFile,filesize($targetFile));
fclose($fcFile);


//echo $fileContents;

echo '<br><br>';


//echo $fc;

//echo '<br><br>';


$explodedFile = (explode('", "', $fc));

$arrLen = count($explodedFile) - 1;



for ($i = 0; $i <= $arrLen; $i++) {
  echo "Current Key is: $i <br>";
  echo $explodedFile[$i];
  echo "<br><br>";
}


//echo $explodedFile[0];
//echo 'file contents: ' . $fileContents . " |||output done";
//echo md5($fileContents);


//$loadedJsonFile = json_encode($fileContents);

//echo $loadedJsonFile;
//echo gettype($loadedJsonFile);
//echo '<br><br>';
//echo gettype($fileContents);


//echo ;

/*
echo $fileContents;
echo '<br><br>';


//$fileLength = count($fileContents);
//echo 'File length: ' . $fileLength;
//$fileSplitLen = $fileLength / 7;

echo '<br><br>';

$explodedFile = (explode('", "', $fileContents));

echo $explodedFile;
echo $explodedFile[0];


for ($i = 0; $i <= 10; $i++) {
  echo "The number is: $i <br>";
  echo $fileContents['"' . $i . '"'];
  echo "<br><br>";
}
*/


echo '<html>';
echo '<div class="ioHeaderMenu">';
  echo '<button class="button ioHeaderMenuObject" onclick="window.location.href=""https://shardhive.com"">shardHive.com</button>';

  echo '<button class="button ioHeaderMenuObject" onclick="window.location.href="https://io.shardhive.com/"">IO Landing</button>';
  
  echo '<button class="button ioHeaderMenuObject" onclick="window.location.href=""https://io.shardhive.com/login.php"">IO Login</button>';

echo '</div>';
echo '</html>';


?>
