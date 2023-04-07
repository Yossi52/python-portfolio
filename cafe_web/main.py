from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, URL, InputRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '123456qwerty'
Bootstrap(app)

# DB 연결
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# 테이블 구조
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(50), nullable=False)
    coffee_price = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# 카페 추가 form
class AddCafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField('Map URL', validators=[DataRequired(), URL(require_tld=True)])
    img_url = StringField('Image URL', validators=[DataRequired(), URL(require_tld=True)])
    location = StringField('Location', validators=[DataRequired()])
    has_sockets = SelectField('Sockets', choices=[(1, '🟢'), (0, '🔴')], validators=[InputRequired()])
    has_toilet = SelectField('Toilet', choices=[(1, '🟢'), (0, '🔴')], validators=[InputRequired()])
    has_wifi = SelectField('WIFI', choices=[(1, '🟢'), (0, '🔴')], validators=[InputRequired()])
    can_take_calls = SelectField('Calls', choices=[(1, '🟢'), (0, '🔴')], validators=[InputRequired()])
    seats = StringField('Seats', validators=[DataRequired()])
    coffee_price = StringField('Coffee Price', validators=[DataRequired()])
    submit = SubmitField('Submit')


# 카페 업데이트 form
class UpdateCafe(FlaskForm):
    map_url = StringField('Map URL', validators=[DataRequired(), URL(require_tld=True)])
    img_url = StringField('Image URL', validators=[DataRequired(), URL(require_tld=True)])
    location = StringField('Location', validators=[DataRequired()])
    has_sockets = SelectField('Sockets', choices=[(1, '🟢'), (0, '🔴')], validators=[InputRequired()])
    has_toilet = SelectField('Toilet', choices=[(1, '🟢'), (0, '🔴')], validators=[InputRequired()])
    has_wifi = SelectField('WIFI', choices=[(1, '🟢'), (0, '🔴')], validators=[InputRequired()])
    can_take_calls = SelectField('Calls', choices=[(1, '🟢'), (0, '🔴')], validators=[InputRequired()])
    seats = StringField('Seats', validators=[DataRequired()])
    coffee_price = StringField('Coffee Price', validators=[DataRequired()])
    submit = SubmitField('Submit')


# 카페 삭제 폼
class DeleteCafe(FlaskForm):
    delete_bool = BooleanField("Delete the Cafe?")
    submit = SubmitField("Submit")


# 홈페이지
@app.route('/')
def home():
    return render_template('index.html')


# 카페 리스트
@app.route('/cafes')
def cafes():
    all_cafes = db.session.query(Cafe).all()
    all_cafes_list = [cafe.to_dict() for cafe in all_cafes]
    return render_template('cafes.html', cafes=all_cafes_list)


# 카페 추가
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = AddCafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=int(form.has_sockets.data),
            has_toilet=int(form.has_toilet.data),
            has_wifi=int(form.has_wifi.data),
            can_take_calls=int(form.can_take_calls.data),
            seats=form.seats.data,
            coffee_price=form.coffee_price.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


# 카페 업데이트
@app.route('/update', methods=['GET', 'POST'])
def update_cafe():
    cafe_id = request.args.get('cafe_id')
    cafe_to_update = db.session.query(Cafe).get(cafe_id)
    form = UpdateCafe(
        map_url=cafe_to_update.map_url,
        img_url=cafe_to_update.img_url,
        location=cafe_to_update.location,
        has_sockets=1 if cafe_to_update.has_sockets else 0,
        has_toilet=1 if cafe_to_update.has_toilet else 0,
        has_wifi=1 if cafe_to_update.has_wifi else 0,
        can_take_calls=1 if cafe_to_update.can_take_calls else 0,
        seats=cafe_to_update.seats,
        coffee_price=cafe_to_update.coffee_price
    )
    if cafe_to_update:
        if form.validate_on_submit():
            cafe_to_update.map_url = form.map_url.data
            cafe_to_update.img_url = form.img_url.data
            cafe_to_update.location = form.location.data
            cafe_to_update.has_sockets = int(form.has_sockets.data)
            cafe_to_update.has_toilet = int(form.has_toilet.data)
            cafe_to_update.has_wifi = int(form.has_wifi.data)
            cafe_to_update.can_take_calls = int(form.can_take_calls.data)
            cafe_to_update.seats = form.seats.data
            cafe_to_update.coffee_price = form.coffee_price.data
            db.session.commit()
            return redirect(url_for('cafes'))
        return render_template('update.html', form=form, cafe=cafe_to_update)
    else:
        return redirect(url_for('home'))


# 카페 삭제
@app.route('/delete', methods=['GET', 'POST'])
def delete_cafe():
    cafe_id = request.args.get('cafe_id')
    cafe_to_delete = db.session.query(Cafe).get(cafe_id)
    form = DeleteCafe()
    if cafe_to_delete:
        if form.validate_on_submit():
            if form.delete_bool.data:
                db.session.delete(cafe_to_delete)
                db.session.commit()
            return redirect(url_for('cafes'))
        return render_template('delete.html', form=form, cafe=cafe_to_delete)
    else:
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
