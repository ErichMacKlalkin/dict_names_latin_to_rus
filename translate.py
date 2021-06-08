import sys 
from flask import Flask, render_template, request
from datetime import datetime
from database import database
app = Flask(__name__)



@app.route('/')
def entry_page() -> 'html':
    return render_template('translate.html',the_title='Translate the names!')



@app.route('/translated', methods=['POST'])
def win():
    data = [name for name in request.form['names'].title().split()]
    result = []
    for ele in data:
        for key, val in database.items():
            if ele in val:
                result.append(key)
                break
        else:
            result.append(ele)
            log_names(ele)
    print(result)
    return render_template('translated.html',the_title='Translated names', res=result)        
            
    #data_title = [num.title() for num in data]
    #result = [key for ele in data for key, val in database.items() if ele in val]
    
    

def log_names(ele):
    with open('log.txt','a') as log:
        print(ele,'||',datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M"),file=log)
        
if __name__ == '__main__':
    app.run(debug=True)
