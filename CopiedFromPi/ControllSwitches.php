<?php

exec("gpio mode 0 out");
exec("gpio mode 2 out");
exec("gpio mode 3 out");
exec("gpio mode 27 out");
exec("gpio mode 28 out");
exec("gpio mode 29 out");

if (isset($_POST["seekBarValue"])){
	$receivedValue = $_POST["seekBarValue"];
	exec("sudo php /var/www/html/runFan.php $receivedValue");
}
if ($_POST["btnToggle1"] = "ON1") {
	exec("gpio write 0 1");
}
if ($_POST["btnToggle1"] = "OFF1") {
	exec("gpio write 0 0");
}
if ($_POST["btnToggle1"] = "ON2") {
	exec("gpio write 2 1");
}
if ($_POST["btnToggle1"] = "OFF2") {
	exec("gpio write 2 0");
}
if ($_POST["btnToggle1"] = "ON3") {
	exec("gpio write 3 1");
}
if ($_POST["btnToggle1"] = "OFF3") {
	exec("gpio write 3 0");
}
if ($_POST["btnToggle1"] = "ON4") {
	exec("gpio write 27 1");
}
if ($_POST["btnToggle1"] = "OFF4") {
	exec("gpio write 27 0");
}
if ($_POST["btnToggle1"] = "ON5") {
	exec("gpio write 28 1");
}
if ($_POST["btnToggle1"] = "OFF5") {
	exec("gpio write 28 0");
}
if ($_POST["btnToggle1"] = "ON6") {
	exec("gpio write 29 1");
}
if ($_POST["btnToggle1"] = "OFF6") {
	exec("gpio write 29 0");
}

//if($_POST["GET_RESTART"] = "RESTART") {
//	exec("sudo reboot");
//}


?>