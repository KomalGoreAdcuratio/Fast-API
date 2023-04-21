## step 1   ==> import
from fastapi import FastAPI

### step 2   ==> Create app

app=FastAPI()

### step 3    ==>decorate
@app.get('/')

#### step4   ===> define function
def index():
    return {'data':{'name':'Komal'}}

@app.get('/qu')
def getQueryData(limit:int=0,data:int=0):
    print(limit)
    return {'limit':limit , 'data':data}
@app.get('/{i}')
def index(i:int):
    try:
        return {'data':int(i)}
    except:
        return {'data':'ERROR'}
    
@app.post('/data/')
def index(request):
    return request

