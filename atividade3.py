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


    def qualQuadrante(self, x, y):
        if(x > 0 and y > 0):
            return 1

        elif(x < 0 and y > 0):
            return 2

        elif(y < 0 and x > 0):
            return 3

        elif(y < 0 and x > 0):
            return 4

        elif(y == 0 and x == 0):
            return 'Origem do plano'  


class Quadrilatero():
    def __init__(self, P1, P2):
        self.P1 = P1
        self.P2 = P2


    def contidoEmQ(self, a = Ponto, Quadrilatero):
        if(a.getX() <= P2.getX and a.getX() >= P1.getX() and a.getY() <= P1.getY() and a.getY() >= P2.getY()):
            return True
        else:
            return False 
                
