import flask
# Probably going to make a incident reporting API for cybersecurity incidents. This is a good idea to have internal operations, and I will host my own vulernability service like dradis in the future. This will be the backend server side API for adding the vulnerabilites and notes. Any suggestions for other cybersecurity needs should be given please! I just have some free time. 
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# We will probably use mysql for the database storage, and encrypt it if possible.

@app.route('/', methods=['GET'])
def home():
      return "<h1>GCyberAPI by GrifKies </h1><p>This site is a prototype API for pentesting users to manage their vulnerabilites across pentesting jobs.</p>"
app.run()