from app.server import db


if __name__ == "__main__":
	with open ("db.schema.txt", "r") as myfile:
		schema = myfile.read().replace('\n', '')
	result = db.engine.execute(schema)
	with open ("db.sample_data.sql", "r") as mydata:
		data = mydata.read().replace('\n', '')
	result = db.engine.execute(data)