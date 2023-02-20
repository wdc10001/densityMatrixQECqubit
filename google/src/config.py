from google.src.physicGate import *
from numpy import random

# Q0,Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15,Q16 = 'Q26', 'Q32', 'Q33', 'Q34', 'Q38', 'Q39', 'Q40', 'Q44', 'Q45', 'Q46', 'Q49', 'Q50', 'Q51', 'Q56','Q57', 'Q58', 'Q63'
Q0,Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15,Q16 = 'Q00','Q01','Q02','Q03','Q04','Q05','Q06','Q07','Q08','Q09','Q10','Q11','Q12','Q13','Q14','Q15','Q16'
RQ0,RQ1,RQ2,RQ3,RQ4,RQ5,RQ6,RQ7,RQ8,RQ9,RQ10,RQ11,RQ12,RQ13,RQ14,RQ15,RQ16 = 'R05','R06','R06','R06','R07','R07','R07','R08','R08','R08','R09','R09','R09','R10','R10','R10','R11'
Q_ALL = [Q0,Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15,Q16]
R_ALL = [RQ0,RQ1,RQ2,RQ3,RQ4,RQ5,RQ6,RQ7,RQ8,RQ9,RQ10,RQ11,RQ12,RQ13,RQ14,RQ15,RQ16]
QR_Dict = {i:j for i,j in zip(Q_ALL,R_ALL)}
Q_Data = [Q1,Q2,Q6,Q4,Q8,Q12,Q10,Q14,Q15]
Q_Anci = [i for i in Q_ALL if i not in Q_Data]
B_ALL = 'B ' + ''.join([f'{i} ' for i in Q_ALL]) + ''.join([f'{i} ' for i in set(R_ALL)])
M_ALL = ''.join([f'MEASURE {QR_Dict[i]} {i}\n' for i in Q_ALL])
M_Anci = ''.join([f'MEASURE {QR_Dict[i]} {i}\n' for i in Q_Anci])
M_Data = ''.join([f'MEASURE {QR_Dict[i]} {i}\n' for i in Q_Data])

fWest = [[Q0,Q1],[Q2,Q0],[Q5,Q4],[Q5,Q10],[Q11,Q6],[Q11,Q12],[Q14,Q16],[Q15,Q16],[Q3,Q1],[Q2,Q3],[Q4,Q3],[Q3,Q8],[Q2,Q7],[Q7,Q6],[Q7,Q8],[Q7,Q12],[Q9,Q4],[Q9,Q8],[Q9,Q10],[Q14,Q9],[Q13,Q8],[Q13,Q12],[Q14,Q13],[Q15,Q13]]

tail = f'''
{B_ALL}
{M_ALL}
'''

psT = f'''
{M_ALL}
{B_ALL}
{I(10000,Q_ALL)}
{B_ALL}
'''

initp = f'''
{Y2P([Q1,Q6,Q8,Q10,Q15])}
'''

initm = f'''
{Y2M([Q1,Q6,Q8,Q10,Q15])}
{X2P([Q2,Q4,Q12,Q14])}
{X2P([Q2,Q4,Q12,Q14])}
'''

init0 = f'''
{Y2P([Q2,Q4,Q12,Q14])}
'''

init1 = f'''
{Y2M([Q2,Q4,Q12,Q14])}
{X2P([Q1,Q6,Q8,Q10,Q15])}
{X2P([Q1,Q6,Q8,Q10,Q15])}
'''

randomQubits = random.choice(Q_Data,random.choice(range(10),1),replace=False)
init_random = f'''
{X2P(randomQubits)}
{X2P(randomQubits)}
'''

MX = f'''
{Y2M([Q1,Q6,Q8,Q10,Q15])}
'''

MZ = f'''
{Y2M([Q2,Q4,Q12,Q14])}
'''