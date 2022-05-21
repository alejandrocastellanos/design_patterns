class Subscriber:

    def __init__(self, name):
        self.name = name

    def send_message(self, message):
        print(f'Sending Message = {message}')


class Publisher:

    def __init__(self):
        self.subscriber = set()

    def register(self, who: Subscriber):
        print('register', who.name)
        self.subscriber.add(who)

    def unregister(self, who: Subscriber):
        self.subscriber.discard(who)

    def dispatch(self, message: str):
        for subscriber in self.subscriber:
            subscriber.send_message(message)


publisher = Publisher()

rolan = Subscriber('Rolan')
alejo = Subscriber('Alejo')

publisher.register(rolan)
publisher.register(alejo)

publisher.dispatch("Enviando un nuevo mensaje")

publisher.unregister(alejo)

print('------')
publisher.dispatch("Enviando un nuevo mensaje")

