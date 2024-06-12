Switch to root user:
sudo su

Install MySQL Server:
sudo apt-get install -y mysql-server

Start MySQL Service:
sudo service mysql start

get into MySQL command line:
mysql

Create a new user and grant privileges:
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';
ALTER USER 'admin'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;

Setting Up Database and Tables:
SQL script saved in file named scheme.sql.
Run the script as root user:
mysql -u admin -p < scheme.sql
Or
mysql -u root < scheme.sql

Working with MySQL in Python
Install the MySQL Connector for Python:
pip install mysql-connector-python

run:
python3 ems.py
to use the program 