from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'  # Add your root password here
app.config['MYSQL_DATABASE_DB'] = 'company_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def index():
    return 'Hello, Flask with MySQL!'


if __name__ == '__main__':
    app.run(debug=True)