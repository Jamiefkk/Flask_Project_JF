from flask import Flask, render_template

from controllers.visits_country_controller import visit_countries_blueprint
from controllers.visits_city_controller import visit_cities_blueprint
# from controllers.visits_attraction_controller import visit_attractions_blueprint

app = Flask(__name__)

app.register_blueprint(visit_countries_blueprint)
app.register_blueprint(visit_cities_blueprint)
# app.register_blueprint(visit_attractions_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)