from api.init import app


@app.route('/')
def index():
    return "hello, capstone!"