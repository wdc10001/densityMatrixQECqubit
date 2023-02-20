import re
import cirq
import google.src.NoiseChannel as NC
import numpy as np
from math import pi

class qcisToCirq():
    def __init__(self,qcis:str,qData:list,pDict:dict,tDict:dict,fHL:list,ten:bool,eleven:bool,circ:list) -> None:
        self.qcis,self.qData,self.pDict,self.tDict,self.fHL,self.circ,self.ten,self.eleven = qcis,qData,pDict,tDict,fHL,circ,ten,eleven

    def matchSQ(self,line_:re.Match,gate:cirq.Gate):
        nStr = line_.group(2)[1:]
        Qn = 'Q'+nStr
        if self.ten and Qn not in self.qData: nStr = '00'
        if self.eleven and Qn == 'Q05': nStr = '05'
        Qubit = cirq.LineQubit(int(nStr))
        self.circ.append(gate(Qubit))
        self.circ.append(NC.SingleQubitNoiseChannel(self.pDict['px'][Qn],self.pDict['py'][Qn],self.pDict['pz'][Qn],Qubit))

    def matchline(self)->list:
        count = 0
        for line in self.qcis.split('\n'):
            line_ = re.match(r'([a-zA-Z0-9]*) ([a-zA-Z0-9]*) ?(.*)', line)
            if line_:
                if line_.group(1) == 'I':
                    nStr = line_.group(2)[1:]
                    Qn = 'Q'+nStr
                    if self.ten and Qn not in self.qData: nStr = '00'
                    if self.eleven and Qn == 'Q05': nStr = '05'
                    Qubit = cirq.LineQubit(int(nStr))
                    tg = int(line_.group(3))
                    decay10 = 1-np.exp(-tg/self.tDict['T1_10'][Qn])
                    dephase10 = 1-np.exp(-tg/self.tDict['Tp_10'][Qn])
                    self.circ.append(cirq.amplitude_damp(decay10).on(Qubit))
                    self.circ.append(cirq.phase_damp(dephase10).on(Qubit))
                if line_.group(1) == 'X2P':
                    self.matchSQ(line_,cirq.rx(pi/2))
                if line_.group(1) == 'X2M':
                    self.matchSQ(line_,cirq.rx(-pi/2))
                if line_.group(1) == 'Y2P':
                    self.matchSQ(line_,cirq.ry(pi/2))
                if line_.group(1) == 'Y2M':
                    self.matchSQ(line_,cirq.ry(-pi/2))
                if line_.group(1) == 'MEASURE':
                    nStr = line_.group(3)[1:]
                    Qn = 'Q'+nStr
                    if self.ten and Qn not in self.qData: nStr = '00'
                    if self.eleven and Qn == 'Q05': nStr = '05'
                    Qubit = cirq.LineQubit(int(nStr))
                    self.circ.append(cirq.bit_flip(self.pDict['pM'][Qn]).on(Qubit))
                    self.circ.append(cirq.measure(Qubit,key=Qn+'m'+f'{count}'))
                    if Qn not in self.qData:
                        self.circ.append(cirq.reset(Qubit))
                        self.circ.append(cirq.bit_flip(self.pDict['pReset01'][Qn]).on(Qubit))
                    count += 1
                if line_.group(1) == 'GCZ':
                    n1 = line_.group(2)[1:3]
                    n2 = line_.group(2)[3:5]
                    if self.ten:
                        if ['Q'+n1,'Q'+n2] in self.fHL:
                            QnH,QnL = 'Q'+n1,'Q'+n2
                            if 'Q'+n1 in self.qData: 
                                QubitH,QubitL = cirq.LineQubit(int(n1)),cirq.LineQubit(0)
                                if self.eleven and n2 == '05':
                                    QubitH,QubitL = cirq.LineQubit(int(n1)),cirq.LineQubit(5)
                            else: 
                                QubitH,QubitL = cirq.LineQubit(0),cirq.LineQubit(int(n2))
                                if self.eleven and n1 == '05':
                                    QubitH,QubitL = cirq.LineQubit(5),cirq.LineQubit(int(n2))
                        else:
                            QnH,QnL = 'Q'+n2,'Q'+n1
                            if 'Q'+n1 in self.qData: 
                                QubitH,QubitL = cirq.LineQubit(0),cirq.LineQubit(int(n1))
                                if self.eleven and n2 == '05':
                                    QubitH,QubitL = cirq.LineQubit(5),cirq.LineQubit(int(n1))
                            else: 
                                QubitH,QubitL = cirq.LineQubit(int(n2)),cirq.LineQubit(0)
                                if self.eleven and n1 == '05':
                                    QubitH,QubitL = cirq.LineQubit(int(n2)),cirq.LineQubit(5)
                    else:
                        if ['Q'+n1,'Q'+n2] in self.fHL:
                            QnH,QnL = 'Q'+n1,'Q'+n2
                            QubitH,QubitL = cirq.LineQubit(int(n1)),cirq.LineQubit(int(n2))
                        else:
                            QnH,QnL = 'Q'+n2,'Q'+n1
                            QubitH,QubitL = cirq.LineQubit(int(n2)),cirq.LineQubit(int(n1))
                    self.circ.append(cirq.CZ(QubitH,QubitL))
                    self.circ.append(NC.DoubleQubitNoiseChannel(self.pDict['pCZ'][(QnH,QnL)],QubitH,QubitL))
                if line_.group(1) == 'GCT':
                    n1 = line_.group(2)[1:3]
                    n2 = line_.group(2)[3:5]
                    n3 = line_.group(2)[5:7]
                    n4 = line_.group(2)[7:9]
                    Qubit1 = cirq.LineQubit(int(n1))
                    Qubit2 = cirq.LineQubit(int(n2))
                    Qubit3 = cirq.LineQubit(int(n3))
                    Qubit4 = cirq.LineQubit(int(n4))
                    self.circ.append(NC.DoubleQubitNoiseChannel(1,Qubit1,Qubit2))
                    self.circ.append(NC.DoubleQubitNoiseChannel(1,Qubit3,Qubit4))
        return self.circ
