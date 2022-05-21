
class MongoDb:
    connection = 'Mongo db connection started'

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MongoDb, cls).__new__(cls)
        return cls.instance

    def get_data(self, data):
        return data


db_1 = MongoDb()
db_2 = MongoDb()
db_3 = MongoDb()
db_4 = MongoDb()

print(db_1)
print(db_1.get_data(data='db_1'))
print(db_2)
print(db_2.get_data(data='db_2'))
print(db_3)
print(db_3.get_data(data='db_3'))
print(db_4)
print(db_4.get_data(data='db_4'))

db_1.connection = 'Postgresql'
print(db_1)
print(db_1.connection)
