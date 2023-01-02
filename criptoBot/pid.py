class Pid:
    'Tüm öğrenciler için temel sınıf'
    id = []
    
    def __init__(self, pid):
        self.pid = pid
        self.pidekle()

    def pidekle(self):
        self.id.append(self.pid)

    def id_goruntule(self):
        a = id(0)
        return a

