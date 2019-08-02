<?php

exec("gpio mode 0 out");
exec("gpio mode 2 out");
exec("gpio mode 3 out");
exec("gpio mode 27 out");
exec("gpio mode 28 out");
exec("gpio mode 1 out");

exec("gpio mode 22 out");
exec("gpio mode 23 out");
exec("gpio mode 24 out");
exec("gpio mode 25 out");

if ($_POST["Switch1"] == "ON") {
	exec("gpio write 0 1");
}
if ($_POST["Switch1"] == "OFF") {
	exec("gpio write 0 0");
}
if ($_POST["Switch2"] == "ON") {
	exec("gpio write 2 1");
}
if ($_POST["Switch2"] == "OFF") {
	exec("gpio write 2 0");
}
if ($_POST["Switch3"] == "ON") {
	exec("gpio write 3 1");
}
if ($_POST["Switch3"] == "OFF") {
	exec("gpio write 3 0");
}
if ($_POST["Switch4"] == "ON") {
	exec("gpio write 27 1");
}
if ($_POST["Switch4"] == "OFF") {
	exec("gpio write 27 0");
}
if ($_POST["Switch5"] == "ON") {
	exec("gpio write 28 1");
}
if ($_POST["Switch5"] == "OFF") {
	exec("gpio write 28 0");
}
if ($_POST["Switch6"] == "ON") {
	exec("gpio write 1 1");
}
if ($_POST["Switch6"] == "OFF") {
	exec("gpio write 1 0");
}

//if($_POST["GET_RESTART"] = "RESTART") {
//	exec("sudo reboot");
//}

if ($_POST["speed"] == "0") {
	exec("gpio write 22 0");
	exec("gpio write 23 0");
	exec("gpio write 24 0");
	exec("gpio write 25 0");
}
if ($_POST["speed"] == "25") {
	exec("gpio write 22 1");
	exec("gpio write 23 0");
	exec("gpio write 24 0");
	exec("gpio write 25 0");
}
if ($_POST["speed"] == "50") {
	exec("gpio write 22 1");
	exec("gpio write 23 1");
	exec("gpio write 24 0");
	exec("gpio write 25 0");
}
if ($_POST["speed"] == "75") {
	exec("gpio write 22 1");
	exec("gpio write 23 1");
	exec("gpio write 24 1");
	exec("gpio write 25 0");
}
if ($_POST["speed"] == "100") {
	exec("gpio write 22 1");
	exec("gpio write 23 1");
	exec("gpio write 24 1");
	exec("gpio write 25 1");
}

?>