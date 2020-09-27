import sys
from project import db, app

if __name__ == '__main__':
    print ("Server env: ", app.config['ENV_NAME'], "\n")
    app.run()
