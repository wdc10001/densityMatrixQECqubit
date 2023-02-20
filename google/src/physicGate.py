I = lambda ti,QList:''.join([f'''
I {Qi} {ti}
''' for Qi in QList])

Y2M = lambda QList:''.join([f'''
Y2M {Qi}
''' for Qi in QList])

Y2P = lambda QList:''.join([f'''
Y2P {Qi}
''' for Qi in QList])

X2M = lambda QList:''.join([f'''
X2M {Qi}
''' for Qi in QList])

X2P = lambda QList:''.join([f'''
X2P {Qi}
''' for Qi in QList])

Z2M = lambda QList:''.join([f'''
Z2M {Qi}
''' for Qi in QList])

CZ = lambda QList:''.join([f'''
GCZ G{Qi[0][1:]}{Qi[1][1:]} 0
''' if int(Qi[0][1:]) > int(Qi[1][1:]) else f'''
GCZ G{Qi[1][1:]}{Qi[0][1:]} 0
''' for Qi in QList])

DD = lambda nD,tH,tMR,QList:''.join([f'''
I {Qi} {tMR}
''' for Qi in QList]) if nD == 0 else ''.join([nD*2*f'''
I {Qi} {int(tMR/nD/2/8)*2-tH}
X2P {Qi}
X2P {Qi}
I {Qi} {int(tMR/nD/2/8)*2-tH}
I {Qi} {int(tMR/nD/2/8)*2-tH}
Y2P {Qi}
Y2P {Qi}
I {Qi} {int(tMR/nD/2/8)*2-tH}
''' for Qi in QList])
    
MEASURE = lambda QList:''.join([f'''
MEASURE {Qi[0]} {Qi[1]}
''' for Qi in QList])