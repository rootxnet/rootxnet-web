rootxnet-web
============
[![Requirements Status](https://requires.io/github/rootxnet/rootxnet-web/requirements.svg?branch=master)](https://requires.io/github/rootxnet/rootxnet-web/requirements/?branch=master)

The source code of http://www.rootxnet.com/ website.

This project serves as a playgrond for some of my ideas:

### NanoDJ:
IPython Notebook publishing platform, it makes easier to keep .ipynb along with all includes in one 
place to make version control and collaboration easier. 

Additional information like tags, title, short description can be added to the .ipynb metadata:

```javascript  
"publisher": {
  "title": "IPython Notebook is neat!",
  "tags": "python, notebook"
  "short": "The IPython Notebook is an interactive computational environment [...]"
}
```

These tasks can be automatized with included tools:
* compilation to html
* metadata extraction
* testing
* docker image creation
* automatic deployments (docker)

### Installation for development:
```
git clone https://github.com/rootxnet/rootxnet-web.git testproj

# create a virtual environment
virtualenv --no-site-packages .env

# activate environment
source .env/bin/activate

# install required libraries
pip install --upgrade ./testproj/requirements.txt

cd testproj/web

# build the notebooks found in testproj/web/source directory
python nano.py build_ipynb

# run the dev server
python nano.py runserver 0.0.0.0:8000
```

### Docker build
```
git clone https://github.com/rootxnet/rootxnet-web.git testproj
cd testproj

# build the container and name it testproj
docker build -t testproj .

# run the container, make port 8000 accessible from host, name the instance as testproj.instance
docker run --publish=8000:8000 --name=testproj.instance -t testproj:latest
```
From now on the website will be available at the http://<host IP>:8000

### Testing
Docker can also be used to test the project:
```
docker run -e RUN_TESTS=true -t testproj:latest
```
Alternatively, the tests can be run with:
```
cd testproj
tox
```
