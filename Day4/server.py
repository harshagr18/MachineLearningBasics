from flask import Flask
import routes

f=Flask("ATw")
f.register_blueprint(routes.model_predictor)
f.run(host="0.0.0.0",port=6969)

