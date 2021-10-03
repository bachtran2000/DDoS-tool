class RW:
    def saveBot(listip):
        f = open("botlist.txt", "w")
        for ip in listip:
            f.write(ip+"$bach$2349567\n")
        f.close()
