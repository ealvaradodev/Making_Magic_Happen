# Making_Magic_Happen<br>
Front end and back end rebuild of MHRR website lets go<br>
=================================<br>
magic_backend<br>
=================================<br>
requirement for program to run.. <br>
python version 3.6.2 or 3.6.5 <br>
Video for setup for python :
  https://www.youtube.com/watch?v=3lGhtIqT0Tk
  
  
Video for setup for pip :
https://www.youtube.com/watch?v=zPMr0lEMqpo  
  
(not sure if it will get automatically installed, but make sure pip is installed) 


python -m pip install -U pip 


if you have already make sure you upgrade you pip 

pip install Django==2.0.6


xampp:


1.) install xampp using standard install

2.) run xampp after install run Apache and MySQL

3.) Paste http://localhost/phpmyadmin into your browser

4.) Go to database tab and create magichappen database

 [make sure xampp is on] 
inside the folder Making_Magic_Happen/makingMagicHappen (in cmd) 

          python manage.py runserver
   
(might need to install mysqlclient):


pip install mysqlClient 


should work if not use:


pip install --only-binary :all: mysqlclient

