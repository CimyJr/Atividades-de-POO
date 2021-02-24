class Ponto:
    def __init__(self, x, y):
        self._x = x
        self._y = y


    def getX(self):
        return self._x


    def getY(self):
        return self._y


    def setX(self, x):
        self._x = x


    def setY(self, y):
        self._y = y


    def qualQuadrante(self):
        if(self.getX() > 0 and self.getY() > 0):
            return 1

        elif(self.getX() < 0 and self.getY() > 0):
            return 2

        elif(self.getY() < 0 and self.getX > 0):
            return 4

        elif(self.getX() < 0 and self.getY() < 0):
            return 3

        elif(self.getX() == 0 and self.getY() == 0):
            return 'Origem do plano'  


class Quadrilatero():
    def __init__(self, P1, P2):
        self.P1 = P1 #x
        self.P2 = P2 #y


    def contidoEmQ(self, a):
        if(a.getY() <= self.P2 and a.getX() <= self.P1):
            return True
        else:
            return False
