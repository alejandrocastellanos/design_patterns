
class Connection:
    db = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Connection, cls).__new__(cls)
        return cls.instance

    def connect_to_db(self):
        if not self.db:
            self.db = 'Mongo DB connection started'

    def get_data(self):
        print(self.db)
        print('Get data from DB')


if __name__ == "__main__":
    # create object of Singleton Class
    instance_connection = Connection()
    instance_connection.connect_to_db()
    print(instance_connection)
    print(instance_connection.get_data())

    instance_connection_2 = Connection()
    instance_connection_2.connect_to_db()
    print(instance_connection_2)
    print(instance_connection_2.get_data())

