class Coin:
    name = 'coin'
    point = 1
    cp = 1
    sp = 10
    ep = 50
    gp = 100
    pp = 1000
    cost = ''

    # def __init__(self, name, point, cp=1, sp=10, ep=10, gp=100, pp=100):
    #     self.name = name
    #     self.point = point
    #     self.cp = cp
    #     self.sp = sp
    #     self.ep = ep
    #     self.gp = gp
    #     self.pp = pp

    def __str__(self):
        cp = '{:>10}'.format('cp')
        sp = '{:>10}'.format('sp')
        ep = '{:>10}'.format('ep')
        gp = '{:>10}'.format('gp')
        pp = '{:>10}'.format('pp')
        cp2 = '\n{:>10}'.format(self.cp)
        sp2 = '{:>10}'.format(self.sp)
        ep2 = '{:>10}'.format(self.ep)
        gp2 = '{:>10}'.format(self.gp)
        pp2 = '{:>10}'.format(self.pp)
        return f'{cp}{sp}{ep}{gp}{pp}{cp2}{sp2}{ep2}{gp2}{pp2}'


class Copper(Coin):
    name = 'copper'

    def __init__(self, point):
        self.point = point
        self.cp = point
        self.sp = point * 10
        self.ep = point * 50
        self.gp = point * 100
        self.pp = point * 1000
        self.cost = f'{self.point} {self.name}'


class Silver(Coin):
    name = 'silver'

    def __init__(self, point):
        self.point = point
        self.cp = point * 0.1
        self.sp = point
        self.ep = point * 5
        self.gp = point * 10
        self.pp = point * 100
        self.cost = f'{self.point} {self.name}'


class Electrum(Coin):
    name = 'electrum'

    def __init__(self, point):
        self.point = point
        self.cp = point * 0.02
        self.sp = point * 0.2
        self.ep = point
        self.gp = point * 2
        self.pp = point * 20
        self.cost = f'{self.point} {self.name}'


class Gold(Coin):
    name = 'gold'

    def __init__(self, point):
        self.point = point
        self.cp = point * 0.01
        self.sp = point * 0.1
        self.ep = point * 0.5
        self.gp = point
        self.pp = point * 10
        self.cost = f'{self.point} {self.name}'


class Platinum(Coin):
    name = 'platinum'

    def __init__(self, point):
        self.point = point
        self.cp = point * 0.001
        self.sp = point * 0.01
        self.ep = point * 0.05
        self.gp = point * 0.1
        self.pp = point
        self.cost = f'{self.point} {self.name}'


a = Platinum(10)

print(a.cost)
