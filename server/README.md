### Prerequisites
Python3 and Pip3.7 (or pip3)

### Installing
First, create a virtual environment
```
python3 -m virtualenv env
```

After creating the virtual environment, start the environment using the following command.
```
source env/bin/activate
```

Now, install all the dependencies as specified in requirements.txt
```
make init
```

Be sure to set the environment variable for flask
```
export FLASK_APP=app.py
```

### Running the server
To start the server, run the following command
```
flask run
```

### Database
When setting up the database, make sure to have a file called DBinfo which stores
the credentials for the sql server. For more information, look at DBinfo_template 
for how to format the information
