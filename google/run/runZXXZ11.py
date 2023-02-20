import cirq,time
from qcisToCirq import qcisToCirq
from ZXXZ11 import EC,ECDD
from config import *
import multiprocessing
from functools import partial
import numpy as np
from qubitPara import *

nD = 3
M_Dire = MZ
fHL = fWest
qData = Q_Data

pDict = {'px':px,'py':py,'pz':pz,'pM':pM,'pReset01':pReset01,'pReset02':pReset02,'pLeak':pLeak,'pCZ':pCZ,'pCT':pCT}
tDict = {'T1_10':T1_10,'T1_21':T1_21,'Tp_10':Tp_10,'Tp_21':Tp_21,'Th12':Th12,'tH':tH,'tCZ':tCZ}

def runCirc(ncycle:int,shots:int):
    # start = time.time()
    qcis = f'{init_random}'+ncycle*f'{ECDD(nD,tH,tCZ,tM,tR,pCT)}'+f'{EC(tH,tCZ,pCT)}{M_Dire}{M_Data}'
    circuitList = qcisToCirq(qcis,qData,pDict,tDict,fHL,ten=True,eleven=True,circ=[]).matchline()
    circuit = cirq.Circuit(circuitList)
    sim = cirq.Simulator()
    result = sim.simulate(circuit)
    mDict = {i:result.measurements[i][0] for i in result.measurements}
    mList = [mDict[key] for i in Q_ALL for key in mDict if key[:3] == i]
    # print(time.time()-start)
    if shots%1000 == 0: print('ncycle',ncycle,'shots',shots)
    return mList

if __name__ == '__main__':
    # runCirc(25,0)
    shots = 40000
    pools = multiprocessing.Pool(8)
    for ncycle in range(3,25):
        result = pools.map(partial(runCirc,ncycle),range(shots))
        np.savetxt(f'google/result11/ncycle{ncycle+1}CT.txt',result,fmt='%d',delimiter='')
    pools.close()
    pools.join()

#测试结果：0.9秒一个周期