# config                    
from flask import Flask

# factory
def create_app():
    app = Flask(__name__)

    # index route
    @app.route('/')
    def index(): 
        return 'Hello, PetFax!'

    # register pet blueprint 
    from . import pets 
    app.register_blueprint(pets.bp)

    # register fact blueprint 
    from . import fact
    app.register_blueprint(fact.bp)

    # return the app 
    return app