<?php
$cookie_string= base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSRwh6QUcIaAw%3D");

$defaultdata = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));

//echo  $cookie_string ^ $defaultdata;

$key = 'qw8J';
$newString = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));
$cookieData = '';
for ($i = 0; $i < strlen($newString); $i++) {
    $cookieData .= $key[$i % strlen($key)] ^ $newString[$i];
}
echo base64_encode($cookieData);
?>
