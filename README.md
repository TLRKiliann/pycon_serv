# pycon_serv
Connection to a database MySql with (pymysql) 

How to install mysql ubuntu 18.04 :

> sudo apt-get update \
> sudo apt-get install mysql-server \
> sudo mysql_secure_installation \
> sudo mysql

Change the authentication method for root :

> mysql> SELECT user,authentication_string,plugin,host FROM mysql.user; \
> mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

Reload grant tables :

> mysql> FLUSH PRIVILEGES; 

Recheck authentication method for MySQL users :

> mysql> SELECT user,authentication_string,plugin,host FROM mysql.user; \
> mysql> exit

Commands of mysql.service :

> sudo systemctl status mysql.service \
> sudo systemctl start mysql \
> sudo systemctl stop mysql

To create a user for more security :

> mysql -u root -p \
> mysql> CREATE USER 'your_usrpseudo'@'localhost' IDENTIFIED BY 'your_new_strong_password'; \
> mysql> GRANT ALL PRIVILEGES ON *.* TO 'your_usrpseudo'@'localhost' WITH GRANT OPTION;

By connecting to MySQL Admin as root and running any administrative command :
> sudo mysqladmin -p -u root version

https://vitux.com/how-to-install-and-configure-mysql-in-ubuntu-18-04-lts/

How to install MYSQL Workbench :
