
from flask import Flask, render_template

app = Flask(__name__)

gomp="Gompada 2"

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

data = {
  'scan_clause': '( {cash} ( monthly rsi( 14 ) > 60 and weekly rsi( 14 ) > 60 and latest rsi( 14 ) > 60 and 1 day ago  rsi( 14 ) <= 60 and latest volume > 100000 ) ) '
}
def doJob():
    with requests.Session() as s:
        r = s.get('https://chartink.com/screener/time-pass-48')
        soup = bs(r.content, 'lxml')
        s.headers['X-CSRF-TOKEN'] = soup.select_one('[name=csrf-token]')['content']
        r = s.post('https://chartink.com/screener/process', data=data).json()
        #print(r.json())
        df = pd.DataFrame(r['data'])
        #print(df)
        gomp = df #"Gompada 3"
        return gomp

@app.route('/')

def hello():
    #gomp = doJob()
    #return '<div> Hello, World! I love you too '+ gomp +'</div>'
    with requests.Session() as s:
        url1 ='https://chartink.com/screener/time-pass-48'
        #r =  s.get('http://example.com').content
        r =  s.get(url1).content

        soup = bs(r, 'lxml')
        token = s.headers['X-CSRF-TOKEN'] = soup.select_one('[name=csrf-token]')['content']
        r = s.post('https://chartink.com/screener/process', data=data).json()
        df = pd.DataFrame(r['data'])

        return render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values, index=False)
        #r['data']  #r.json()   #token #r #soup 
          #soup # r #s.headers

#if __name__ == '__main__':
#   app.run()
