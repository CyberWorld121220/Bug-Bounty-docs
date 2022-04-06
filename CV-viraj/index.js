//server.js file
var express = require('express')
var app = express()
var port = process.env.PORT || '5000';
app.use(express.static(__dirname)) //serves the static html file
app.get('/industrial-knowledge', (req, res) => {
    res.sendFile('./pages/industrial.html', { root: __dirname });
});
var server = app.listen(port, () =>{
console.log("server is listening on Port ${port}");
}) //gets express server started and listening for requests
