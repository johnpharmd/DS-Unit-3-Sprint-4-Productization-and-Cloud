"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import openaq

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(APP)
API = openaq.OpenAQ()


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return '<Time {} --- Value {}>'.format(self.datetime, self.value)


def add_record(record):
    try:
        pass
    except Exception as e:
        pass
    else:
        pass


@APP.route('/')
def root():
    """Base view."""
    # return 'TODO - part 2 and beyond!'
    los_angeles_data = get_los_angeles_data()
    return str(los_angeles_data)

@APP.route('/main')
def get_los_angeles_data():
    """ Retrieves 100 observations of measurements of fine particulate
    matter (PM 2.5) in the Los Angeles area."""
    status, body = API.measurements(city='Los Angeles', parameter='pm25')
    dt_values_tups_list = [(dic['date']['utc'], dic['value']) for
                           dic in body['results']]

    return dt_values_tups_list

@app.route('/record', methods=['POST'])
@app.route('/record', methods=['GET'])
def record(name=None):
    message = ''
    try:
        pass
    except Exception as e:
        pass
    # name = name or request.values['user_name']
    # try:
    #     if request.method == 'POST':
    #         add_or_update_user(name)
    #         message = 'User {} successfully added!'.format(name)
    #     tweets = User.query.filter(User.name == name).one().tweets
    # except Exception as e:
    #     message = 'Error adding {}: {}'.format(name, e)
    #     tweets = []
    # return render_template('user.html', title=name, tweets=tweets,
    #                        message=message)

@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    # TODO Get data from OpenAQ, make Record objects with it, and add to db
    DB.session.commit()
    return 'Data refreshed!'
