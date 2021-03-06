# как же не хватает структур из си
import numpy as np
from ctypes import *

class ZoomData:
    def __init__(self):
        self.x = None
        self.y = None
        self.colors = None

# рутина в отдельный класс
class IQData_arr:
    def __init__(self, _size=50):
        self.points = []
        self.size = _size
        self.offset = []



        self.updateLen()

    def __len__(self):
        return self.len

    def setOffset(self, arr):
        self.offset = arr

    # получаем номера доступных каналов
    def getChans(self):

        chans  = []

        chans = [val.chan for val in self.points]

        chans = np.unique(np.array(chans))

        return chans

    def countbyRAD(self, _chan):

        deg_arr = self.getArr('RAD', _chan, _np=True)

        x, y = np.unique(deg_arr, return_counts=True)

        return [x, y]

    #количество одинаковых точек по градусам
    def countbyDEG(self, _chan):

        deg_arr = self.getArr('DEG', _chan,_np=True)

        x, y = np.unique(deg_arr, return_counts=True)

        return [x, y]

    # получение класс с только уникальными точками
    # по градусам+амлитудам и каналам
    def getUniqDEGAMP(self):
        tmp = IQData_arr()


        return tmp



    # получение класс с только уникальными точками
    # по градусам и каналам
    def getUniqDEG(self ):
        tmp = IQData_arr()

        return tmp



    def getDeltaArr(self,type, chan0, chan1, flg=False):

        try:
            arr_chan0_x =  self.getArr(type, chan0, _np=True)
            arr_chan1_x =  self.getArr(type, chan1, _np=True)

            ret = arr_chan0_x - arr_chan1_x
        except:
            ret = []


        if type == 'DEG':

            for i in range(len(ret)):
                if ret[i] < 0:
                #if :
                 #   print('b ' + str(ret[i]))
                    ret[i] = max([abs(int(ret[i]  / 360)), 1]) * 360 + ret[i]
                   # print('a ' + str(ret[i]))
                    if ret[i] < 0:
                        ret[i] = ret[i] + 360

            #print(ret)

        return ret

    # получение массивов для графиков
    def getArr(self, type, _chan, _np=False):

        res = []

        if type == 'I':
            res = [val.I for val in self.points if val.chan == _chan]
        elif type == 'Q':
            res = [val.Q for val in self.points if val.chan == _chan]
        elif type == 'DEG':
            res = [val.DEG for val in self.points if val.chan == _chan]
        elif type == 'RAD':
            res = [val.RAD for val in self.points if val.chan == _chan]
        elif type == 'AMP':
            res = [val.AMP for val in self.points if val.chan == _chan]

        if _np:
            res = np.array(res)

        return res

    def updateLen(self):
        self.len = len(self.points)

    # --- размер очереди
    def setSize(self, _size):
        self.size = _size

    # --- удаление точек
    def clearPoints(self):
        self.points = []
        self.updateLen()


    #у нас тут вообще то очередь, молодой человек!
    def changeLen(self):
        while len(self.points) > self.size:
            for i in range(len(self.getChans())):
                self.points.pop(0)


    def addPoints(self, pts):
        self.points = self.points + pts

        self.changeLen()
        self.updateLen()

    # --- добавление точки с учетом очереди
    def addPoint(self, pt):

        self.points.append(pt)

        self.changeLen()
        self.updateLen()

# почему бы не считать все сразу, почти структура
class IQData:
    def __init__(self):
        self.I = None
        self.Q = None

        self.DEG = None
        self.RAD = None

        self.AMP = None

        self.chan = None

    def __str__(self):
        ret = ''

        ret = ret + 'I: ' +  str(self.I) + '\n'
        ret = ret + 'Q: ' +  str(self.Q) + '\n'

        ret = ret + 'DEG: ' + str(self.DEG) + '\n'
        ret = ret + 'RAD: ' + str(self.RAD) + '\n'

        ret = ret + 'AMP: ' + str(self.AMP) + '\n'

        ret = ret + 'chan: ' + str(self.chan)

        return ret



