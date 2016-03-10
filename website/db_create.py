from app import db
from app.models import *


with open ("drop_tables.sql", "r") as myfile:
	schema = myfile.read().replace('\n', '')
	result = db.engine.execute(schema)


db.engine.execute(schema)


# create the database and the db table
db.create_all()

# insert data
user1 = app_users("test33@test.com", "1234")
user2 = app_users("test34@test.com", "1234")
user3 = app_users("test35@test.com", "1234")
user4 = app_users("main@test.com", "123")
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.add(user4)
db.session.commit()

ca1 = categories("Design")
ca2 = categories("Web")
ca3 = categories("Business")
ca4 = categories("3D + Animation")
ca5 = categories("Music")

db.session.add(ca1)
db.session.add(ca2)
db.session.add(ca3)
db.session.add(ca4)
db.session.add(ca5)
db.session.commit()

course1 = courses("Data Analysis and Statistical Inference", "This course introduces you to the discipline of statistics as a science of understanding and analyzing data. You will learn how to effectively make use of data in the face of uncertainty: how to collect data, how to analyze data, and how to use data to make inferences and conclusions about real world phenomena.", user4.id, ca1.category_id, "courses.jpg")
course2 = courses("Programming Mobile Applications Android", "This course has been developed in two parts (Part 1 and Part 2), which will cover the fundamental programming principles, software architecture and user experience considerations underlying handheld software applications and their development environments, enabling course completers to build their own Android applications and experienced engineers to master a powerful set of development skills. Most students will need to have taken Part 1 before attempting Part 2. While Part 1 focuses on the basic Android Platform and components, Part 2 will focus on more advanced components and concepts provided by the Android platform:", user2.id, ca2.category_id, "courses2.jpg")
course3 = courses("Engineering Systems in Motion", "This course is an introduction to the study of bodies in motion as applied to engineering systems and structures. We will study the dynamics of particle motion and bodies in rigid planar (2D) motion. This will consist of both the kinematics and kinetics of motion. Kinematics deals with the geometrical aspects of motion describing position, velocity, and acceleration, all as a function of time. Kinetics is the study of forces acting on these bodies and how it affects their motion.", user1.id, ca3.category_id, "courses3.jpeg")
db.session.add(course1)
db.session.add(course2)
db.session.add(course3)
db.session.commit()

db.session.add(course_comments(course1.course_id, "Lorem ipsum dolor sit amet, ne mea integre mediocritatem, no quot molestie quo. Sit ea altera latine iuvaret, commodo erroribus patrioque has ei. Ne alii suas consulatu mea. Mel ut tota imperdiet. Ei pri inani cetero placerat.", user2.id))
db.session.add(course_comments(course1.course_id, "Graeco ancillae vis ut, ut mel porro corpora offendit. Nec dicat quando discere cu, quis quidam eos cu, te case solet pri. Ex est eros meis dicta, eu quando volutpat sit. Prima dolore comprehensam et eam, ne tale meis omnium sea.", user2.id))
db.session.add(course_comments(course1.course_id, "Vim in singulis reformidans. Ex timeam inciderint definitionem sed, ut nec porro facilisi antiopam. Duo habeo hendrerit ad, solet definitiones pri ut. Laudem option ea vix, pri id reque recteque. Vidit option constituto sit in. Ex rebum animal mea, vel ne tritani referrentur.", user2.id))
db.session.add(course_comments(course1.course_id, "Verterem scripserit eam ne. Recteque posidonium vis eu, tamquam scripserit vis ex, has posse nostro legimus ea. Partem deleniti percipit te quo. Vis ex nostro appellantur, eu quis odio constituam mel. Per an reque theophrastus, alia causae cu ius.", user2.id))
db.session.commit()

db.session.add(course_enrollments(course1.course_id, user4.id))
db.session.add(course_enrollments(course2.course_id, user4.id))
db.session.add(course_enrollments(course3.course_id, user4.id))
db.session.commit()

video1 = course_videos(course1.course_id, "https://youtu.be/OWsyrnOBsJs", "Computer Programming Intro", 1)
video2 = course_videos(course1.course_id, "https://youtu.be/k6U-i4gXkLM", " MIT Sting Introduction", 2)
video3 = course_videos(course1.course_id, "https://youtu.be/CDO28Esqmcg", "Computer Organization", 3)
video4 = course_videos(course1.course_id, "https://youtu.be/z-OxzIC6pic", "Hacking", 4)


db.session.add(video1)
db.session.add(video2)
db.session.add(video3)
db.session.add(video4)
db.session.commit()

question1 = course_video_quiz_questions(video1.course_video_id, 2, "first question", "A", "apple", "banana", "car", "goose")
question2 = course_video_quiz_questions(video1.course_video_id, 4, "next question", "A", "apple", "banana", "car", "goose")
db.session.add(question1)
db.session.add(question2)
db.session.commit()

# commit the changes
db.session.commit()
