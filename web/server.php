<?php


if($_GET["task"]=="cpuusage") {
    echo sys_getloadavg;
}
?>