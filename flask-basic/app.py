import os
import shutil
import csv
import sys
from flask import Flask,render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_bootstrap import Bootstrap
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask import Flask ,render_template ,request
import numpy as np
import joblib
app = Flask(__name__)
bootstrap = Bootstrap(app)

# # Configurations
app.config['SECRET_KEY'] = 'blah blah blah blah'

class NameForm(FlaskForm):
	name = StringField('Enter the text', default="worst game")
	submit = SubmitField('Submit')

class dropdownMenu(FlaskForm):
	dropdown_list = ['Bernoulli NB', 'Multinomial NB', 'Multinomial NB with TF IDF', 'Linear Support Vector classifier'] 
	seqSimilarity = SelectField('Choose Model type', choices=dropdown_list)

# ROUTES!
# @app.route('/',methods=['GET','POST'])
# def index():
# 	form = NameForm()
# 	if form.validate_on_submit():
# 		name = form.name.data
# 		return render_template('index.html',form=form,name=name)
# 	return render_template('index.html',form=form,name=None)

@app.route("/",methods=['GET','POST'])
def index():
	# form1= dropdownMenu()
	form = NameForm()
	if form.validate_on_submit():
		text = form.name.data
		message=[text]
		vector = joblib.load('vectorizer.sav')
		mNB = joblib.load('nb.sav')
		text = vector.transform(message)
		print(text)
		result = (mNB.predict(text))
		print("krupa ", result)
		result=str(result).strip('[.]')
		print(result)
		return render_template('index.html',form=form,result=result)
	return render_template('index.html',form=form, result=None)

@app.route('/help')
def help():
	text_list = []
	# Python Version
	text_list.append({
		'label':'Python Version',
		'value':str(sys.version)})
	# os.path.abspath(os.path.dirname(__file__))
	text_list.append({
		'label':'os.path.abspath(os.path.dirname(__file__))',
		'value':str(os.path.abspath(os.path.dirname(__file__)))
		})
	# OS Current Working Directory
	text_list.append({
		'label':'OS CWD',
		'value':str(os.getcwd())})
	# OS CWD Contents
	label = 'OS CWD Contents'
	value = ''
	text_list.append({
		'label':label,
		'value':value})
	return render_template('help.html',text_list=text_list,title='help')

@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
	return render_template('404.html',title='404')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
	return render_template('500.html',title='500')

# port = int(os.getenv('PORT'))
# app.run()
# @app.route('/')
# def home():
#     return render_template('index.html')


port = int(os.getenv('PORT', '3000'))
app.run(host='0.0.0.0', port=port)
