from physicGate import *
from config import *
from numpy import random

Q_ALL = [Q0,Q1,Q2,Q3,Q4]
Q_Anci = [Q0,Q3]
Q_Data = [Q1,Q2,Q4]
M_Anci = ''.join([f'MEASURE {QR_Dict[i]} {i}\n' for i in Q_Anci])

pattern1 = [[Q0,Q1],[Q3,Q4]]
pattern2 = [[Q0,Q2],[Q3,Q1]]

CZidle = lambda pattern:[i for i in Q_ALL if i not in [j for k in pattern for j in k]]

EC = lambda tH,tCZ,pCT:f'''
{B_ALL}
{Y2M(Q_ALL)}
{B_ALL}
{CZ(pattern1)}
{I(tCZ,CZidle(pattern1))}
{B_ALL}
{I(tH,Q_ALL)}
{B_ALL}
{CZ(pattern2)}
{I(tCZ,CZidle(pattern2))}
{B_ALL}
{Y2P(Q_ALL)}
'''

ECM = lambda nD,tH,tCZ,tM,tR,pCT:EC(tH,tCZ,pCT) + f'''
{B_ALL}
{M_Anci}
{DD(nD,tH,tM+tR,Q_Data)}
'''