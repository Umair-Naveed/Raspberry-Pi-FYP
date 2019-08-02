<?php 
exec("gpio mode 0 out");

if($_POST["btnToggle"] == "ON") {
	exec("gpio write 0 1");
}
if($_POST["btnToggle"] == "OFF") {
	exec("gpio write 0 0");
}

?>