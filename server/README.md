# How to set up backend dev environment

1.  Make sure you have Python 3.8.2 or higher (Best if its 3.8.2)

2.  Create a virtual environment by doing ```python3 -m venv venv```

3.  Start the virtual environment by doing  ```source ./venv/bin/activate```

4.  Install all the dependencies by doing ```pip install -r requirements.txt```

5.  Create a directory named "private" in the root of server directory and place the Google Natural Language json api key in there

6.  duplicate .flaskenv.temp to another file named .flaskenv, change GOOGLE_APPLICATION_CREDENTIALS to your system pathway to that Google Natural Language json api key json 



# Starting up flask backend server

1. Run ```flask run``` in root directory of server or ```./run.sh``` if you wish to perform logging (note: outputs will be buffered until the flask app is stopped)




