# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:30:30 2019

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

ticker = ['AMZN','FB','GOOGL','MCHP','MU','MSFT']
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
      #result = stckdata[input_form[0]][input_form[1]]
      result = []
      link_all = []
      base_url = "https://quotes.wsj.com/"+input_form[0]
      chrome_options = webdriver.ChromeOptions()
      driver = webdriver.Chrome()
      driver.get(base_url)
      for i in range(5):
          element = driver.find_element_by_xpath('//a[normalize-space(text())="load more"]') 
          driver.execute_script("arguments[0].click();", element)
      for i in driver.find_elements_by_class_name('headline'):
          p = i.text
          if p:
              link = i.find_element_by_tag_name('a').get_attribute('href')
              sentiment = sia.polarity_scores(p)
              blob = TextBlob(p)
              sentimenter = blob.sentiment
              if(input_form[1]=='POS'):
                  if(sentimenter.polarity >= 0):
                      #print(p, "--->>", sentiment)
                      print(p, "---->",sentimenter,"---->",link)
                      result.append(p)
              if(input_form[1]=='NEG'):
                  if(sentimenter.polarity < 0):
                      #print(p, "--->>", sentiment)
                      print(p, "---->",sentimenter,"---->",link)
                      result.append(p)
                      link_all.append(link)
      print(link_all)   
      print(result)
      return render_template('home.html',result = zip(result,link_all))
      
if __name__ == '__main__':
   app.run(debug = False)
   
'''from textblob import TextBlob
import nltk
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from selenium import webdriver
import time

company_ticker = 'FB'
input_form = ['POS','NEG']

sia = SentimentIntensityAnalyzer()

base_url = "https://quotes.wsj.com/"+company_ticker

 

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome()
driver.get(base_url)

for i in range(5):
    element = driver.find_element_by_xpath('//a[normalize-space(text())="load more"]') 
    driver.execute_script("arguments[0].click();", element)

for i in driver.find_elements_by_class_name('headline'):
    p = i.text
    if p:
        link = i.find_element_by_tag_name('a').get_attribute('href')
        sentiment = sia.polarity_scores(p)
        blob = TextBlob(p)
        sentimenter = blob.sentiment
        if(input_form[1]=='POS'):
            if(sentimenter.polarity >= 0):
                #print(p, "--->>", sentiment)
                print(p, "---->",sentimenter,"---->",link)
        if(input_form[1]=='NEG'):
            if(sentimenter.polarity < 0):
                #print(p, "--->>", sentiment)
                print(p, "---->",sentimenter,"---->",link)'''
      
