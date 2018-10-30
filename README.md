# erp-tsia

##versiones
> **python 3.5.2**
> **MariaDB 10.0.36**

##Modulos
Ejecutar la siguiente linea en la consola de pycharm o dentro de su directorio

pip install django django-adminlte2 mysqlclient

##Instalacion mariaDB

##Linux
+sudo apt-get install mariadb-server libmysqlclient-dev
+sudo mysql_secure_installation
+sudo su
+mysql
    
    > CREATE DATABASE erp_tsia;
    > CREATE USER ‘soporte’@’localhost’ IDENTIFIED BY ‘tsia2018'; 
    > GRANT ALL PRIVILEGES ON erp_tsia.* TO ‘soporte’@’localhost';
    > FLUSH PRIVILEGES;
