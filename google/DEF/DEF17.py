import sys,os
sys.path.append(os.path.abspath(''))
import plotly.graph_objects as go
import numpy as np

title = 'qubit_ncycle8shots10000tH400pM0.03pCZ0.02pxyz0.01'
path = f'google/result/result10/{title}.txt'
CycleNum = 8
ExperimentNum = 10000

qnum = 17
d_2_qubit = [0,5,11,16]
d_4_qubit = [3,7,9,13]
meas_qubit = d_2_qubit + d_4_qubit
data_qubit = [ii for ii in range(qnum) if ii not in meas_qubit]

data_def = [[0 for i2 in range(CycleNum)] for i1 in range(qnum)]
with open(path,'r') as f:
    data_raw = [[ [] for i2 in range(qnum) ] for i1 in range(ExperimentNum)]
    for expi in range(ExperimentNum):
        data_line = f.readline()
        shift = 0
        for ii in range(qnum):
            data_num = CycleNum if ii in meas_qubit else 1
            data_raw[expi][ii] = [int(data_line[e]) if int(data_line[e])<2 else 1 for e in range(shift,shift+data_num)]
            shift += data_num
DEF_std={}
fig = go.Figure()
for ii in meas_qubit:
    for cycle_num in range(1,CycleNum):
        data_def[ii][cycle_num] = sum([int(data_raw[expi][ii][cycle_num] != data_raw[expi][ii][cycle_num-1]) for expi in range(ExperimentNum)])/ExperimentNum
    data_def[ii][0] =  sum([int(data_raw[expi][ii][0] != 0) for expi in range(ExperimentNum)])/ExperimentNum
    DEF_std.update({ii:np.std(data_def[ii][1:],ddof=1)})

data_def[0].append(sum([(int(data_raw[expi][1][0]) ^ int(data_raw[expi][2][0])) != data_raw[expi][0][CycleNum-1] for expi in range(ExperimentNum)])/ExperimentNum)
data_def[3].append(sum([(int(data_raw[expi][1][0]) ^ int(data_raw[expi][2][0]) ^ int(data_raw[expi][4][0]) ^ int(data_raw[expi][8][0])) != data_raw[expi][3][CycleNum-1] for expi in range(ExperimentNum)])/ExperimentNum)
data_def[5].append(sum([(int(data_raw[expi][4][0]) ^ int(data_raw[expi][10][0])) != data_raw[expi][5][CycleNum-1] for expi in range(ExperimentNum)])/ExperimentNum)
data_def[7].append(sum([(int(data_raw[expi][2][0]) ^ int(data_raw[expi][6][0]) ^ int(data_raw[expi][8][0]) ^ int(data_raw[expi][12][0])) != data_raw[expi][7][CycleNum-1] for expi in range(ExperimentNum)])/ExperimentNum)
data_def[9].append(sum([(int(data_raw[expi][4][0]) ^ int(data_raw[expi][8][0]) ^ int(data_raw[expi][10][0]) ^ int(data_raw[expi][14][0])) != data_raw[expi][9][CycleNum-1] for expi in range(ExperimentNum)])/ExperimentNum)
data_def[11].append(sum([(int(data_raw[expi][6][0]) ^ int(data_raw[expi][12][0])) != data_raw[expi][11][CycleNum-1] for expi in range(ExperimentNum)])/ExperimentNum)
data_def[13].append(sum([(int(data_raw[expi][8][0]) ^ int(data_raw[expi][12][0]) ^ int(data_raw[expi][14][0]) ^ int(data_raw[expi][15][0])) != data_raw[expi][13][CycleNum-1] for expi in range(ExperimentNum)])/ExperimentNum)
data_def[16].append(sum([(int(data_raw[expi][14][0]) ^ int(data_raw[expi][15][0])) != data_raw[expi][16][CycleNum-1] for expi in range(ExperimentNum)])/ExperimentNum)

for ii in meas_qubit:
    fig.add_trace(go.Scatter(x=list(range(CycleNum+1)),y=data_def[ii],mode='lines+markers',name=f'qubit{ii}_std{round(DEF_std[ii],4)}'))

# d2_def = [0 for cycle_num in range(CycleNum+1)]
# for cycle_num in range(CycleNum+1):
#     for ii in d_2_qubit:
#         d2_def[cycle_num] += data_def[ii][cycle_num]
#     d2_def[cycle_num] /= len(d_2_qubit)
# d4_def = [0 for cycle_num in range(CycleNum+1)]
# for cycle_num in range(CycleNum+1):
#     for ii in d_4_qubit:
#         d4_def[cycle_num] += data_def[ii][cycle_num]
#     d4_def[cycle_num] /= len(d_4_qubit)

# fig.add_trace(go.Scatter(x=list(range(CycleNum+1)),y=d2_def,mode='lines+markers',name=f'd2_qubit'))
# fig.add_trace(go.Scatter(x=list(range(CycleNum+1)),y=d4_def,mode='lines+markers',name=f'd4_qubit'))

fig.update_layout(xaxis=dict(tickmode='linear',dtick=1),xaxis_title='cycle',yaxis_title='DEF',title=title)
fig.show()