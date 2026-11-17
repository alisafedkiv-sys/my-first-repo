class Streamer:
    def __init__(self, nick, subscribers):
        self.nick = nick
        self.donates = []
        self.subscribers = subscribers

    def add_donate(self, amount):
        self.donates.append(amount)

    def total_donates(self):
        total = 0
        for donate in self.donates:
            total += donate
        return total

    def average_donate(self):
        if len(self.donates) == 0:
            return 0
        return self.total_donates() / len(self.donates)


def print_stats(streamer):
    print("Стример:", streamer.nick)
    print("Донатов:", len(streamer.donates),
          "сумма:", streamer.total_donates(),
          "средний:", round(streamer.average_donate(), 1))
    print("Подписчиков:", streamer.subscribers)


def is_popular(streamer):
    return streamer.subscribers > 1000


s = Streamer("ShadowStorm", 1500)
s.add_donate(100)
s.add_donate(250)
s.add_donate(50)

print_stats(s)
print("Популярен:", is_popular(s))