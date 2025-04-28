from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for
import os.path

db = SQLAlchemy()

app = Flask(__name__)
application = app

db_name = 'rowing-database.db'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, db_name)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

class Rowing(db.Model):
    __tablename__ = 'rowing'
    id = db.Column(db.Integer, primary_key=True)
    Workout_number = db.Column(db.String)
    First_name = db.Column(db.String)
    Last_name = db.Column(db.String)
    Date = db.Column(db.String)
    Workout = db.Column(db.String)
    Rate = db.Column(db.String)
    Land_or_water = db.Column(db.String)
    Meters = db.Column(db.Integer)
    Splits = db.Column(db.String)
    Calories = db.Column(db.String)
    Heart_rate = db.Column(db.String)
    Team = db.Column(db.String)
    Level = db.Column(db.String)
    Pronouns = db.Column(db.String)
    Image = db.Column(db.String)
    Photo_credits = db.Column(db.String)
    FLCR_website = db.Column(db.String)


@app.route('/')
def index():
    result = db.session.query(
        db.func.min(Rowing.Workout_number),
        Rowing.First_name,
        Rowing.Last_name
    ).group_by(
        Rowing.First_name,
        Rowing.Last_name
    ).all()
    
    rower_list = [(workout_num, first_name, last_name) for workout_num, first_name, last_name in result]
    
    return render_template('index.html', rowers=rower_list)

@app.route('/rowing-tracker/<name>')
def detail(name):
    try: 
        parts = name.split('-')
        first_name = parts[0]
        last_name = ' '.join(parts[1:]) if len(parts) > 1 else ""
        
        rower_workouts = db.session.query(Rowing).filter(
            Rowing.First_name.ilike(first_name),
            Rowing.Last_name.ilike(last_name)
        ).all()
        
        if not rower_workouts:
            return f"<h1>No workouts found for: {first_name} {last_name}</h1>"
        
        first_workout = rower_workouts[0]
        
        rower_info = {
            'First-name': first_workout.First_name,
            'Last-name': first_workout.Last_name,
            'Team': first_workout.Team,
            'Level': first_workout.Level,
            'Pronouns': first_workout.Pronouns,
            'Image': first_workout.Image,
            'Photo-credits': first_workout.Photo_credits,
            'FLCR-website': first_workout.FLCR_website
        }
        
        workouts_list = []
        for workout in rower_workouts:
            workouts_list.append({
                'Date': workout.Date,
                'Workout': workout.Workout,
                'Rate': workout.Rate,
                'Land-or-water': workout.Land_or_water,
                'Meters': workout.Meters,
                'Splits': workout.Splits,
                'Calories': workout.Calories,
                'Heart-rate': workout.Heart_rate
            })
        
        workout_count = len(workouts_list)

    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>"
    
    return render_template('rowing.html', rower=rower_info, workouts=workouts_list, workout_count=workout_count)

def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app.run(debug=True)