<?php

$receiveedValue = $argv[1];
//exec("sudo python3.5 /var/www/html/pwm.py $receivedValue");

exec("gpio mode 22 out");
exec("gpio mode 23 out");
exec("gpio mode 24 out");
exec("gpio mode 25 out");

if (isset($_POST["seekBarValue"])){
	$receivedValue = $_POST["seekBarValue"];
	exec("sudo php /var/www/html/runFan.php $receivedValue");
}
if ("$receiveedValue" == "0") {
	exec("gpio write 22 0");
	exec("gpio write 23 0");
	exec("gpio write 24 0");
	exec("gpio write 25 0");
}
if ("$receiveedValue" == "25") {
	exec("gpio write 22 1");
	exec("gpio write 23 0");
	exec("gpio write 24 0");
	exec("gpio write 25 0");
}
if ("$receiveedValue" == "50") {
	exec("gpio write 22 1");
	exec("gpio write 23 1");
	exec("gpio write 24 0");
	exec("gpio write 25 0");
}
if ("$receiveedValue" == "75") {
	exec("gpio write 22 1");
	exec("gpio write 23 1");
	exec("gpio write 24 1");
	exec("gpio write 25 0");
}
if ("$receiveedValue" == "100") {
	exec("gpio write 22 1");
	exec("gpio write 23 1");
	exec("gpio write 24 1");
	exec("gpio write 25 1");
}


?>