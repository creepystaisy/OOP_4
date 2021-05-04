class generalList:
    def __init__(self):
        self.__list = []
    def clean(self):
        self.__list = []
    def findByCode(self, code):
        for link in self.__list:
            if link.getCode() == code:
                return link
        raise Exception('Объекта с кодом %s нет в списке' % code)

    def getCodes(self):
        return [s.getCode() for s in self.__list]
    def appendList(self, value):
        self.__list.append(value)
    def removeList(self, code):
        for s in self.__list:
            if s.getCode() == code:
                self.__list.remove(s)
    def getName(self, code):
        return self.findByCode(code).getName()
