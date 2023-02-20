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

EC = lambda tH,tCZ:f'''
{B_ALL}
{Y2M(Q_Anci+[Q1,Q6,Q8])}
{I(tH,[Q2,Q4,Q10,Q12,Q14,Q15])}
{B_ALL}
{CZ(pattern1)}
{I(tCZ,CZidle(pattern1))}
{B_ALL}
{Y2P([Q1,Q6,Q8])}
{Y2M([Q2,Q4,Q12,Q14])}
{I(tH,Q_Anci+[Q10,Q15])}
{B_ALL}
{CZ(pattern2)}
{I(tCZ,CZidle(pattern2))}
{B_ALL}
{I(tH,Q_ALL)}
{B_ALL}
{CZ(pattern3)}
{I(tCZ,CZidle(pattern3))}
{B_ALL}
{Y2P([Q2,Q4,Q12,Q14])}
{Y2M([Q8,Q10,Q15])}
{I(tH,Q_Anci+[Q1,Q6])}
{B_ALL}
{CZ(pattern4)}
{I(tCZ,CZidle(pattern4))}
{B_ALL}
{Y2P(Q_Anci+[Q8,Q10,Q15])}
{I(tH,[Q1,Q2,Q4,Q6,Q12,Q14])}
'''

ECM = lambda nD,tH,tCZ,tM,tR:EC(tH,tCZ) + f'''
{B_ALL}
{M_Anci}
{DD(nD,tH,tM+tR,Q_Data)}
'''