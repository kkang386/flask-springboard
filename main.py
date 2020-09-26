import sys
from project import db, app

#print ("###\nStarting Server in ", envs.get_env(sys.argv[1]) if len(sys.argv) == 2 else envs.get_env('dev') , " settings. \n###")

"""
@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
"""

if __name__ == '__main__':
    print ("Server env: ", app.config['ENV_NAME'], "\n")
    app.run()
