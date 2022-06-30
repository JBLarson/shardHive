<!DOCTYPE html>
<html lang="en">

    <style>

      .headerContainer {
        display: grid;
        grid-template-columns: auto auto;
        padding: 10px;
        border: #000099 1px solid;
        background-color: #d4e1f5;
        text-align: center;
        align-content: center;
        align-items: center;
      }

      .grid-item0 {
        align-content: left;
        padding: 20px;
        text-align: left;
      }

      .grid-item1 {
        align-content: right;
        padding: 20px;
        text-align: right;
      }

      h1 {
        color: #000099;
        font-size: 54px;
        align-content: center;
        align-items: center;
        text-align: center;
      }

      h2, h3 {
        color: red;
        align-content: center;
        align-items: center;
        text-align: center;
      }

      p {
        text-align: center;
        align-content: center;
        align-items: center;
      }

      img {
        length: 150px;
        width: 150px;
      }

      input[type=text], select {
        width: 100%;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
      }

      input[type=submit] {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 14px 20px;
        margin: 8px 0;
        border: none;
        border-radius: 4px;
        cursor: pointer;
      }

      input[type=submit]:hover {
        background-color: #45a049;
      }

      div {
        border-radius: 5px;
        padding: 20px;
      }




    </style>

    <body>

      <div class="headerContainer">

        <div class="grid-item0">
          <h1>Welcome to<br>shardHive</h1>
        </div>

        <div class="grid-item1">
          <img src="https://shardhive.com/wp-content/uploads/2022/02/logoTransparent.svg" alt="shardHive Logo">
        </div>
      </div>

    </body>

	<?php
	// handleForm.php

	echo '<p>Name: ' . $_GET['name'] . '</p>';
	echo '<p>Email: ' . $_GET['email'] . '</p>';
	echo '<p>Currency: ' . $_GET['currency'] . '</p>';


	?>
