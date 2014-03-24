### How to Run the Flask WEB Servcie

#### Create virtual python environment
virtualenv venv
. venv/bin/activate

#### Install dependent modules
pip install flask
pip install flask-restful

#### Run Server
python app.py

#### Access the WEB Service
curl -i http://mbpr2013.local:5000/api/news/headline