from flask import Flask

import website.models


           


def create_app():
    app = Flask(__name__);
    app.config['SECRET_KEY'] = 'hgfhdfjdfhjgfh';
    
    

    
    from .auth import auth
   


    
    app.register_blueprint(auth, url_prefix='/')

    
    return app


