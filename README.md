# Game-review-rating-predictor

I have attached ipynb file for comaparison of the different classifiers..
I have attached html file for the jupyter notebook file.

requirements to resolve for the flask-app
pip install -r requirements.txt

I have save my different classifier models as .sav files

STEPS TO DEPLOY THE APP ON ibm CLOUD:

First install the cloud foundry CLI
log into the CF cli
 * cf login -a https://api.ng.bluemix.net
deploy the application
 * cf push APPNAME -m 128M
