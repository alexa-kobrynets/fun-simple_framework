from api import API

app = API()


@app.route(path='/home')
def home(request, response):
    response.text = 'Hello home'

@app.route(path='/about')
def about(request, response):
    response.text = 'Hello about'

@app.route(path="/hello/{name}")
def greeting(request, response, name):
    response.text = f'Hello, {name}'


