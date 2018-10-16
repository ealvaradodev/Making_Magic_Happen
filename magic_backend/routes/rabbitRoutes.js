const express = require('express');
const app = express();
const mysql = require('mysql');
const bodyParser = require('body-parser');
const cors = require('cors');

app.use(bodyParser.json());
app.use(cors());

const connection = mysql.createConnection({
    host : 'localhost',
    user : 'root',
    password : '',
    database : 'MagicHappen'
});

//Creating the table in the databse MagicHappen//
// Whenever we connect to the database for the first time in a system I want all the required table to be created/
connection.connect(function(err){
    if(err) throw err;
    console.log("Connected!!");
    //query doesnot run if the table is already existed//
    var rabbitInfo = "Create table if not exists Rabbit_info(rabbit_id INT AUTO_INCREMENT, Name VARCHAR(225) NOT NULL, Breed VARCHAR(225),Gender VARCHAR(100), Size VARCHAR(225), Update_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(rabbit_id))";
    connection.query(rabbitInfo, function(err, result){
        if(err) throw err;
        console.log("rabbitinfo Created");
        })
});

// for registering the new User 
exports.rabbitResources = function(req,res){
     var rabbit={
       "Name":req.body.name,
       "Breed":req.body.breed,
       "Gender":req.body.gender,
       "Size":req.body.size,
     }
     connection.query('INSERT INTO Rabbit_info SET ?',rabbit, function (error, results, fields) {
     if (error) {
       console.log("error ocurred",error);
       res.send({
         "code":400,
         "failed":"error ocurred"
       })
     }else{
       console.log('The solution is: ', results);
       res.send({
         "code":200,
         "success":"Rabbit inserted sucessfully"
           });
     }
     });
  }
