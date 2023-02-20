import cirq
import random

def SingleQubitNoiseChannel(px:float,py:float,pz:float,Qubit:cirq.Qid)->cirq.Gate:
    errorRate = random.random()
    if errorRate < px:
        return cirq.X(Qubit)
    elif errorRate < px+py:
        return cirq.Y(Qubit)
    elif errorRate < px+py+pz:
        return cirq.Z(Qubit)
    else:
        return cirq.I(Qubit)

def DoubleQubitNoiseChannel(pCZ:float,QubitH:cirq.Qid,QubitL:cirq.Qid)->list:
    errorRate = random.random()
    channelList1 = [cirq.I(QubitH),cirq.X(QubitH),cirq.Y(QubitH),cirq.Z(QubitH)]
    channelList2 = [cirq.I(QubitL),cirq.X(QubitL),cirq.Y(QubitL),cirq.Z(QubitL)]
    if errorRate < pCZ:
        channelList = [random.choice(channelList1),random.choice(channelList2)]
        if channelList1[0] in channelList and channelList2[0] in channelList:
            return DoubleQubitNoiseChannel(1,QubitH,QubitL)
        else:
            return channelList
    else:
        return [channelList1[0],channelList2[0]]

if __name__ == '__main__':
    from math import pi
    q0, q1 = cirq.LineQubit.range(2)
    circuit = cirq.Circuit([
        cirq.I(q0),
        # cirq.measure([q0])
    ])
    sim = cirq.Simulator()
    result = sim.simulate(circuit)
    print(circuit)
    print(result.final_state_vector)
    # print({i:result.measurements[i] for i in result.measurements})