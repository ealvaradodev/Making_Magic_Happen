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
    var userInfo = "Create table if not exists users(id int(11) NOT NULL AUTO_INCREMENT, first_name varchar(100) COLLATE utf8_unicode_ci NOT NULL, last_name varchar(100) COLLATE utf8_unicode_ci NOT NULL, role varchar(100) COLLATE utf8_unicode_ci NOT NULL,userid varchar (100) COLLATE utf8_unicode_ci NOT NULL, password varchar (225), PRIMARY KEY (id))"
    connection.query(userInfo, function(err, result){
        if(err) throw err;
        console.log("userInfo Created");
        })
});

// for registering the new User 
exports.register = function(req,res){
     var users={
       "first_name":req.body.first_name,
       "last_name":req.body.last_name,
       "userid":req.body.userid,
       "password":req.body.password,
       "role":req.body.role
     }
     connection.query('INSERT INTO users SET ?',users, function (error, results, fields) {
     if (error) {
       console.log("error ocurred",error);
       res.send({
         "code":400,
         "failed":"error ocurred"
       })
     }else{
      //  console.log('The solution is: ', results);
       res.send({
         "code":200,
         "success":"user registered sucessfully"
           });
     }
     });
    // });
  
  
  }
  
  exports.login = function(req,res){
    var userid= req.body.userid;
    var password = req.body.password;
    var role = req.body.role;
    connection.query('SELECT * FROM users WHERE userid = ?',[userid], function (error, results, fields) {
    if (error) {
      console.log("error ocurred",error);
      res.send({
        "code":400,
        "failed":"error ocurred"
      })
    }else{
      // console.log('The solution is: ', results[0].password,req.body.password,req.body.role);
      if(results.length >0){
        if(results[0].password == password){
          if(results[0].role == role){
            var obj = {userid: userid}
            res.send({
              "code":200,
              "success":"login sucessfull"
            })
          }
          else{
            res.send({
              "code":204,
              "success":"You have logged in from wrong user role"
            })
          }
  
        }
        else{
          res.send({
               "code":204,
               "success":"UserId and password does not match"
          })
        }
  
      }
      else{
        res.send({
          "code":204,
          "success":"UserID does not exits"
            });
      }
  
  
    }
    });
  }