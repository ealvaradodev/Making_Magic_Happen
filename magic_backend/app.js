const express = require('express');
const app = express();
const mysql = require('mysql');
const bodyParser = require('body-parser');
const cors = require('cors');

app.use(bodyParser.json());
app.use(cors());

const db = mysql.createConnection({
    host : 'localhost',
    user : 'root',
    password : '',
    database : 'MagicHappen'
});

//Creating the table in the databse MagicHappen//
db.connect(function(err){
    if(err) throw err;
    console.log("Connected!!");
    //query doesnot run if the table is already existed//
    var sql = "Create table if not exists Rabbit_info(rabbit_id INT AUTO_INCREMENT, Name VARCHAR(225) NOT NULL, Breed VARCHAR(225),Gender VARCHAR(100), Size VARCHAR(225), Description Text NOT NULL, image varchar(225), Update_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(rabbit_id))";
    db.query(sql, function(err, result){
        if(err) throw err;
        console.log("Table Created");
        console.log(result);
        })
});

app.get('/data', function(req,res){
var sql = 'SELECT * FROM Rabbit_info';
db.query(sql, (err, result)=>{
    if(err) throw err;
    console.log(result);
    res.send(result);
});
});

app.post('/data', function(req, res){
	console.log(req.body); 
    var data = {Name:req.body.name, Breed:req.body.breed, Gender:req.body.gender, Size:req.body.size};
    var sql = 'INSERT INTO rabbit_info SET ?';
    db.query(sql, data, (err, result)=>{
    if(err) throw err;
    console.log(result);
    res.send({
        status: 'Data input!',
        rabbit_id: null,
		Name: req.body.name,
        Breed: req.body.Breed,
        Gender: req.body.Gender,
        Size:req.body.Size
	});
});
});

app.listen(3210, ()=>{
    console.log('Server Connected port 3210')
});