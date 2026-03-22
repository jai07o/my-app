from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World from Render!"

@app.route('/about')
def about():
    return "This is About Page"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

@app.route('/page')
def page():
    return render_template_string("""
    <html>
        <head><title>Simple Page</title></head>
        <body>
            <h1>Welcome to Render App</h1>
            <p>This is a simple web application</p>
        </body>
    </html>
    """)
if __name__ == "__main__":
    app.run()