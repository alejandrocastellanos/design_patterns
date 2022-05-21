class SingletonClass(object):

    db = 'Mongo db connection started'

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


singleton = SingletonClass()
new_singleton = SingletonClass()

print(singleton)
print(new_singleton)

print(new_singleton.db)
