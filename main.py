from flask import Flask, render_template_string
import os

app = Flask(__name__)

# 🏠 Home Page with Links
@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Render App</title>
            <style>
                body {
                    font-family: Arial;
                    text-align: center;
                    margin-top: 50px;
                }
                a {
                    display: block;
                    margin: 10px;
                    font-size: 20px;
                    color: blue;
                    text-decoration: none;
                }
                a:hover {
                    color: darkred;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to My Render Web App 🚀</h1>
            <p>Select a page:</p>
            
            <a href="/about">About Page</a>
            <a href="/greet/Student">Greeting Page</a>
            <a href="/page">HTML Page</a>
        </body>
    </html>
    """

# 📄 About Page
@app.route('/about')
def about():
    return """
    <h2>About Page</h2>
    <p>This is a simple web application deployed on Render.</p>
    <a href="/">Go Back</a>
    """

# 👤 Greeting Page
@app.route('/greet/<name>')
def greet(name):
    return f"""
    <h2>Hello, {name}! 👋</h2>
    <a href="/">Go Back</a>
    """

# 🌐 HTML Page
@app.route('/page')
def page():
    return render_template_string("""
    <html>
        <head>
            <title>Simple Page</title>
        </head>
        <body style="text-align:center;">
            <h1>Welcome to Render</h1>
            <p>This is a simple HTML page.</p>
            <a href="/">Go Back</a>
        </body>
    </html>
    """)

# 🔧 Required for Render deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
