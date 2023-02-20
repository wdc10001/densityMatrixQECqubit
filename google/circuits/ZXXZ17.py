import sys,os
sys.path.append(os.path.abspath(''))
from google.src.physicGate import *
from google.src.config import *
from numpy import random

pattern1 = [[Q3,Q1],[Q11,Q6],[Q13,Q8],[Q7,Q2],[Q9,Q4],[Q16,Q14]]
pattern2 = [[Q3,Q4],[Q11,Q12],[Q13,Q14],[Q7,Q6],[Q9,Q8],[Q16,Q15]]
pattern3 = [[Q3,Q2],[Q5,Q4],[Q13,Q12],[Q7,Q8],[Q9,Q10],[Q0,Q1]]
pattern4 = [[Q3,Q8],[Q5,Q10],[Q13,Q15],[Q7,Q12],[Q9,Q14],[Q0,Q2]]

CZidle = lambda pattern:[i for i in Q_ALL if i not in [j for k in pattern for j in k]]

EC = lambda tH,tCZ,pCT:f'''
{B_ALL}
{Y2M(Q_Anci)}
{I(tH,Q_Data)}
{B_ALL}
{CZ(pattern1)}
{I(tCZ,CZidle(pattern1))}
{B_ALL}
{Y2M(Q_Data)}
{I(tH,Q_Anci)}
{B_ALL}
{CZ(pattern2)}
{I(tCZ,CZidle(pattern2))}
{B_ALL}
{I(tH,Q_ALL)}
{B_ALL}
{CZ(pattern3)}
{I(tCZ,CZidle(pattern3))}
{B_ALL}
{Y2P(Q_Data)}
{I(tH,Q_Anci)}
{B_ALL}
{CZ(pattern4)}
{I(tCZ,CZidle(pattern4))}
{B_ALL}
{Y2P(Q_Anci)}
{I(tH,Q_Data)}
'''

ECM = lambda nD,tH,tCZ,tM,tR,pCT:EC(tH,tCZ,pCT) + f'''
{B_ALL}
{M_Anci}
{DD(nD,tH,tM+tR,Q_Data)}
'''