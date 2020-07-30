from flask import Flask 

app = Flask(__name__) 


#tells us the url that has to be accessed for the function to be called

@app.route('/')
def home():
	return "homepage"


@app.route('/test') 
def test():
	return "Flask is being used for development"

@app.route('/swag')
def swag():
	return "SODMG"

if __name__ == "__main__":
	app.run()

