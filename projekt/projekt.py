from flask import Flask, jsonify
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
# from datatime import datatime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projekt.db'

db = SQLAlchemy(app)

# Flask and Flask-SQLAlchemy initialization here

admin = Admin(app, name='projekt', template_mode='bootstrap3')


class Member (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    date_of_birth = db.Column(db.String(20), nullable=False)
    adress = db.relationship('Address', backref='member', lazy=True)
    mail = db.relationship('Mail', backref='member', lazy=True)
    phone = db.relationship('Contact_phone', backref='member', lazy=True)
    tag = db.relationship('Tag', backref='member', lazy=True)
    group = db.relationship('Group_member', backref='member', lazy=True)

    def __repr__(self):
        return f"Member('{self.id}','{self.name}','{self.surname}','{self.date_of_birth}')"


class Contact_phone (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(40), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=True, unique=True)

    def __repr__(self):
        return f"Phone('{self.phone}','{self.priority}')"


class Mail (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(40), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=True, unique=True)

    def __repr__(self):
        return f"Mail('{self.mail}','{self.priority}')"


class Address (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street_and_number = db.Column(db.String(50), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=True)

    def __repr__(self):
        return f"Address('{self.street_and_number}')"


class Tag (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(50), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=True)

    def __repr__(self):
        return f"Tag('{self.tag}')"


class Group (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    group_members = db.relationship('Group_member', backref='group', lazy=True)

    def __repr__(self):
        return f"Group('{self.id}','{self.name}')"


class Group_member (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=True, unique=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=True)

    def __repr__(self):
        return f"Group('{self.user_id}','{self.group_id}')"


admin.add_view(ModelView(Member, db.session))
admin.add_view(ModelView(Address, db.session))
admin.add_view(ModelView(Contact_phone, db.session))
admin.add_view(ModelView(Mail, db.session))
admin.add_view(ModelView(Tag, db.session))
admin.add_view(ModelView(Group, db.session))
admin.add_view(ModelView(Group_member, db.session))


@app.route("/index")
def home():
    return "Prvi mikroservis ispravan!"


@app.route("/podaci")
def podaci():
    podaci = Group.query.all()
    return str(podaci)


@app.route("/grupe/<ime>")
def grupe(ime):
    memeri = Group_member.query.filter_by(group_id=ime).all()
    #print(memeri)

    konacni = []

    for y in memeri:
        trenutni = Member.query.filter_by(id=str(y)[7]).first()
        #print("ovo je pokusaj: " + str(y)[7])
        konacni.append(trenutni)
        #print("ovo je trenutni: " + str(trenutni))
        # print(y)
    return str(konacni)


if __name__ == "__main__":
    app.run()
