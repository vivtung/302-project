from app import db, bcrypt
from app import app
import datetime
from sqlalchemy import UniqueConstraint, update, CheckConstraint
import sys
if sys.version_info >= (3, 0):
    enable_search = False
else:
    enable_search = True
    import flask.ext.whooshalchemy as whooshalchemy

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('app_users.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('app_users.id'))
)


class app_users(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), index=True, unique=True)
	pw = db.Column(db.String(1000))
	courses = db.relationship('courses', backref='app_users', lazy='dynamic')
	followed = db.relationship('app_users', 
                               secondary=followers, 
                               primaryjoin=(followers.c.follower_id == id), 
                               secondaryjoin=(followers.c.followed_id == id), 
                               backref=db.backref('followers', lazy='dynamic'), 
                               lazy='dynamic')
	
	def is_authenticated(self):
		return True
	
	def follow(self, user):
		if not self.is_following(user):
			self.followed.append(user)
			return self
			
	def unfollow(self, user):
		if self.is_following(user):
			self.followed.remove(user)
			return self
	
	def is_following(self,user):
		return self.followed.filter(followers.c.followed_id == user.id).count() > 0
	
	def is_active(self):
		return True
	
	def is_anonymous(self):
		return False
		
	def get_id(self):
		return unicode(self.id)

	
	def __repr__(self):
		return
		
	def followed_courses(self):
		return courses.query.join(followers, \
        (followers.c.followed_id == courses.instructor_user_id)).filter(followers.c.follower_id == self.id).\
        order_by(courses.creation_date.desc())
		
	def __init__(self, email, pw):
		self.pw = bcrypt.generate_password_hash(pw)
		self.email = email

class categories(db.Model):
	category_id = db.Column(db.Integer, primary_key=True)
	category_name = db.Column(db.Text())

	def __init__(self, category_name):
		self.category_name = category_name

	def __repr__(self):
		return 
	
class courses(db.Model):

	__tablename__ = 'courses'
	__searchable__ = ['name']
	course_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	description = db.Column(db.Text())
	up_vote = db.Column(db.Integer(), default=0)
	down_vote = db.Column(db.Integer(), default=0)
	creation_date = db.Column(db.DateTime, default=db.func.now())
	instructor_user_id = db.Column(db.Integer, db.ForeignKey('app_users.id'))
	category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
	photo_url=db.Column(db.Text)
	#course_enrollment = db.relationship('course_enrollment', backref='courses', lazy='dynamic')
	
	def __repr__(self):
		return 
	
	def __init__(self, name, description, instructor_user_id, category_id, photo_url):
		self.name = name
		self.description = description
		self.instructor_user_id = instructor_user_id
		self.category_id = category_id
		self.photo_url = photo_url
		
class course_enrollments(db.Model):
	__tablename__='course_enrollments'
	
	course_enrollments_id = db.Column(db.Integer, primary_key=True)
	course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'))
	enrollment_date = db.Column(db.DateTime, default=db.func.now())
	enrolled_user = db.Column(db.Integer, db.ForeignKey('app_users.id'), nullable=False)
	__table_args__ = (UniqueConstraint("course_id", "enrolled_user"), )

	def __init__(self, course_id, enrolled_user):
		self.course_id = course_id
		self.enrolled_user = enrolled_user

	def __repr__(self):
		return 

class course_ratings(db.Model):
	__tablename__='course_ratings'

	course_rating_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('app_users.id'), nullable=False)
	course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'))
	rating = db.Column(db.Integer,CheckConstraint('rating >= 1 AND rating <= 5'),nullable=False)
	__table_args__ = (UniqueConstraint("user_id", "course_id"), )

	def __init__(self, rating, course_id, user_id):
		self.rating = rating
		self.course_id = course_id
		self.user_id = user_id

	def __repr__(self):
		return 


class course_videos(db.Model):
	course_video_id = db.Column(db.Integer, primary_key=True)
	course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'))
	added_date = db.Column(db.DateTime, default=db.func.now())
	video_url = db.Column(db.Text())
	name = db.Column(db.String(40))
	order = db.Column(db.Integer, nullable=False)

	def __init__(self, course_id, video_url, name, order):
		self.course_id = course_id
		self.video_url = video_url
		self.name = name
		self.order = order

	def __repr__(self):
		return 

if enable_search:
    whooshalchemy.whoosh_index(app, courses)


class course_video_quiz_questions(db.Model):
	course_video_quiz_questions_id = db.Column(db.Integer, primary_key=True)
	course_video_id = db.Column(db.Integer, db.ForeignKey('course_videos.course_video_id'))
	question_time = db.Column(db.Integer)
	question_string = db.Column(db.Text())
	answer_choice = db.Column(db.String(1))
	choice_A = db.Column(db.String(100))
	choice_B = db.Column(db.String(100))
	choice_C = db.Column(db.String(100))
	choice_D = db.Column(db.String(100))

	def __init__(self, course_video_id, question_time, question_string, answer_choice, choice_A, choice_B, choice_C, choice_D):
		self.course_video_id = course_video_id
		self.question_time = question_time
		self.question_string = question_string
		self.answer_choice = answer_choice
		self.choice_A = choice_A
		self.choice_B = choice_B
		self.choice_C = choice_C
		self.choice_D = choice_D

	def __repr__(self):
		return 

class course_comments(db.Model):
	course_comments_id = db.Column(db.Integer, primary_key=True)
	course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'))
	comment = db.Column(db.Text())
	comment_date = db.Column(db.DateTime, default=db.func.now())
	user_id = db.Column(db.Integer, db.ForeignKey('app_users.id'), nullable=False)

	def __init__(self, course_id, comment, user_id):
		self.course_id = course_id
		self.comment = comment
		self.user_id = user_id

	def __repr__(self):
		return 



