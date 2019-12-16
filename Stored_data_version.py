# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:53:08 2019

@author: Admin
"""

import csv
import pandas as pd
from textblob import TextBlob
import nltk
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from selenium import webdriver
import time
from flask import Flask
from flask import render_template,request
app = Flask(__name__)

sia = SentimentIntensityAnalyzer()
data = pd.read_csv("C:/Users/Admin/Desktop/Project/ticker_stock.csv")

ticker = ['AMZN','FB','GOOGL','MCHP','MU','MSFT','AAPL','BEST','NFLX','VTI','ISRG','WMT','NVDA','RPD','SPLK','PYPL','SNPS','BIDU','NXPI','BABA','STNE','ADBE']
l = dict()

for i in ticker:
    temp = {i:{'POS':[],'NEG':[]}}
    l.update(temp)


@app.route("/home")
def home():
    result = []
    link_all = []
    return render_template('home.html',result = zip(result,link_all))

input_form = []

@app.route("/input",methods = ['POST', 'GET'])
def input_html():
   if request.method == 'POST':
      input_form = []
      result = request.form
      for key,value in result.items():
          input_form.append(value)
      result = stckdata[input_form[0]][input_form[1]]
      r = []
      link_all = []
      for i in result:
          r.append(i.split('^')[0])
          link_all.append(i.split('^')[1])    
      return render_template('home.html',result = zip(result,link_all))
      
if __name__ == '__main__':
   app.run(debug = False)
   

      
