class RW:
    def __init__(self, ip, username, password):
        self.__ip = ip
        self.__username = username
        self.__password = password

    def getip(self):
        return self.__ip

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def saveBot(listip):
        f = open("botlist.txt", "w")
        for ip in listip:
            f.write(ip+"$kali$kali\n")
        f.close()

    def readBot():
        f = open("botlist.txt", "r")
        bot = []
        for i in f.readlines():
            result = i.split("$")
            t = RW(result[0], result[1], result[2])
            bot.append(t)
        return bot
