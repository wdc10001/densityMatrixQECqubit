from physicGate import *
from config import *
from numpy import random

crosstalk1 = lambda pCT:f'''
GCT G03020504
''' if random.random() < pCT else ''

crosstalk2 = lambda pCT:f'''
GCT G03080510
''' if random.random() < pCT else ''

EC = lambda tH,tCZ,pCT:f'''
{Y2M([Q16])}
{I(tH,[Q14])}
{CZ([[Q16,Q14]])}
{I(tH,[Q16])}
{Y2M([Q14])}
{I(tH,[Q15])}
{I(tCZ,[Q15])}
{Y2M([Q15])}
{CZ([[Q16,Q15]])}
{I(tH,[Q16,Q15])}
{I(tCZ,[Q16,Q15])}
{Y2P([Q15])}
{I(tH,[Q16])}
{I(tCZ,[Q16])}
{Y2P([Q16])}
{MEASURE([[RQ16,Q16]])}
{Y2M([Q11])}
{I(tH,[Q6])}
{CZ([[Q11,Q6]])}
{I(tH,[Q11])}
{Y2M([Q6])}
{I(tH,[Q12])}
{I(tCZ,[Q12])}
{Y2M([Q12])}
{CZ([[Q11,Q12]])}
{I(tH,[Q11,Q12])}
{I(tCZ,[Q11])}
{I(tH,[Q11])}
{I(tCZ,[Q11])}
{Y2P([Q11])}
{MEASURE([[RQ11,Q11]])}
{Y2M([Q13])}
{I(tH,[Q8])}
{CZ([[Q13,Q8]])}
{I(tH,[Q13])}
{Y2M([Q8])}
{CZ([[Q13,Q14]])}
{I(tH,[Q13,Q14])}
{CZ([[Q13,Q12]])}
{I(tCZ,[Q14])}
{I(tH,[Q13])}
{Y2P([Q12,Q14])}
{CZ([[Q13,Q15]])}
{Y2P([Q13])}
{I(tH,[Q15])}
{MEASURE([[RQ13,Q13]])}
{Y2M([Q9])}
{I(tH,[Q4])}
{CZ([[Q9,Q4]])}
{I(tH,[Q9])}
{Y2M([Q4])}
{CZ([[Q9,Q8]])}
{I(tH,[Q9,Q8])}
{I(tH,[Q10])}
{I(tCZ,[Q10])}
{Y2M([Q10])}
{I(tCZ,[Q10])}
{I(tH,[Q10])}
{CZ([[Q9,Q10]])}
{I(tH,[Q9])}
{Y2P([Q10])}
{CZ([[Q9,Q14]])}
{Y2P([Q9])}
{I(tH,[Q14])}
{MEASURE([[RQ9,Q9]])}
{Y2M([Q7])}
{I(tH,[Q2])}
{CZ([[Q7,Q2]])}
{I(tH,[Q7])}
{Y2M([Q2])}
{CZ([[Q7,Q6]])}
{I(tCZ,[Q2])}
{I(tH,[Q2,Q6,Q7])}
{CZ([[Q7,Q8]])}
{I(tCZ,[Q6])}
{I(tH,[Q7])}
{Y2P([Q6,Q8])}
{CZ([[Q7,Q12]])}
{I(tCZ,[Q6])}
{Y2P([Q7])}
{I(tH,[Q6,Q12])}
{MEASURE([[RQ7,Q7]])}
{Y2M([Q3])}
{I(tH,[Q1])}
{CZ([[Q3,Q1]])}
{I(tH,[Q3])}
{Y2M([Q1])}
{CZ([[Q3,Q4]])}
{I(tCZ,[Q1])}
{I(tH,[Q1,Q3,Q4])}
{Y2M([Q5])}
{I(tCZ,[Q5])}
{I(tH,[Q5])}
{I(tCZ,[Q5])}
{I(tH,[Q5])}
{CZ([[Q5,Q4]])}
{CZ([[Q3,Q2]])}
{crosstalk1(pCT)}
{I(tH,[Q3])}
{Y2P([Q2])}
{I(tH,[Q5])}
{Y2P([Q4])}
{CZ([[Q5,Q10]])}
{CZ([[Q3,Q8]])}
{crosstalk2(pCT)}
{Y2P([Q3])}
{I(tH,[Q8])}
{MEASURE([[RQ3,Q3]])}
{I(tCZ,[Q4])}
{Y2P([Q5])}
{I(tH,[Q4,Q10])}
{MEASURE([[RQ5,Q5]])}
{Y2M([Q0])}
{I(tCZ,[Q0])}
{I(tH,[Q0])}
{I(tCZ,[Q0])}
{I(tH,[Q0])}
{CZ([[Q0,Q1]])}
{I(tH,[Q0])}
{Y2P([Q1])}
{CZ([[Q0,Q2]])}
{I(tCZ,[Q1])}
{Y2P([Q0])}
{I(tH,[Q1,Q2])}
{MEASURE([[RQ0,Q0]])}
'''

ECDD = lambda nD,tH,tCZ,tM,tR,pCT:EC(tH,tCZ,pCT) + f'''
{DD(nD,tH,tM+tR,Q_Data)}
'''