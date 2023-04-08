from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '123456qwerty'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    check = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


class AddTodo(FlaskForm):
    start_date = DateField('시작한 날', validators=[DataRequired()], render_kw={'style': 'width: 170px'})
    end_date = DateField('끝나는 날', validators=[DataRequired()], render_kw={'style': 'width: 170px'})
    content = StringField('할 일', validators=[DataRequired()])
    submit = SubmitField('등록', validators=[DataRequired()])


@app.route('/', methods=['GET', 'POST'])
def home():
    all_todo = db.session.query(Todo).order_by(Todo.start_date)
    todo_list = [todo.to_dict() for todo in all_todo]
    form = AddTodo(
        start_date=datetime.date(datetime.today()),
        end_date=datetime.date(datetime.today())
    )
    if form.validate_on_submit():
        if form.start_date.data <= form.end_date.data:
            new_todo = Todo(
                content=form.content.data,
                start_date=form.start_date.data,
                end_date=form.end_date.data,
                check=False
            )
            db.session.add(new_todo)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            flash("시작 날짜가 끝나는 날짜보다 뒤에 있을 순 없다!")
    return render_template('index.html', form=form, todo_list=todo_list)


@app.route('/delete')
def delete_todo():
    todo_id = request.args.get('todo_id')
    todo_to_delete = db.session.query(Todo).get(todo_id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/change_check')
def change_check():
    todo_id = request.args.get('todo_id')
    todo_to_change = db.session.query(Todo).get(todo_id)
    if todo_to_change.check:
        todo_to_change.check = False
    else:
        todo_to_change.check = True
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
