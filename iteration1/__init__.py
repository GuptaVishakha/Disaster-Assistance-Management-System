import os
from flask import Flask
from flask import url_for
from flask import redirect

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev',DATABASE=os.path.join(app.instance_path,'iteration1.mysql'))
    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    from iteration1 import createaccount
    app.register_blueprint(createaccount.bp)
    from iteration1 import loginauth
    app.register_blueprint(loginauth.bp)
    from iteration1 import createrequest
    app.register_blueprint(createrequest.bp)
    #app.add_url_rule("/", endpoint="register")
    @app.route('/')
    def hello():
        return redirect(url_for("auth.login"))

    return app