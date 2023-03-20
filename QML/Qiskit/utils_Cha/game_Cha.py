# https://qiskit.org/textbook/ch-ex/hello-qiskit.html
from qiskit_textbook.games import hello_quantum

def game_Cha(level, number, sandbox_number=None):
  match level:
    case 1:
      match number:
        case 1:
          initialize = []
          success_condition = {}
          allowed_gates = {'0': {'NOT': 3}, '1': {}, 'both': {}}
          vi = [[1], False, False]
          qubit_names = {'0':'the only bit', '1':None}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 2:
          initialize = []
          success_condition = {}
          allowed_gates = {'0': {}, '1': {'NOT': 0}, 'both': {}}
          vi = [[], False, False]
          qubit_names = {'0':'the bit on the left', '1':'the bit on the right'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 3:
          initialize = [['x', '0']]
          success_condition = {'IZ': -1.0}
          allowed_gates = {'0': {'CNOT': 0}, '1': {'CNOT': 0}, 'both': {}}
          vi = [[], False, False]
          qubit_names = {'0':'the bit on the left', '1':'the bit on the right'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 4:
          initialize = [['x', '0']]
          success_condition = {'ZI': 1.0, 'IZ': -1.0}
          allowed_gates = {'0': {'CNOT': 0}, '1': {'CNOT': 0}, 'both': {}}
          vi = [[], False, False]
          qubit_names = {'0':'the bit on the left', '1':'the bit on the right'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 5:
          initialize = [['h', '0']]
          success_condition = {'IZ': 0.0}
          allowed_gates = {'0': {'CNOT': 0}, '1': {'CNOT': 0}, 'both': {}}
          vi = [[], False, False]
          qubit_names = {'0':'the bit on the left', '1':'the bit on the right'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 6:
          initialize = [['h', '0']]
          success_condition = {'ZZ': -1.0}
          allowed_gates = {'0': {'NOT': 0, 'CNOT': 0}, '1': {'NOT': 0, 'CNOT': 0}, 'both': {}}
          vi = [[], False, True]
          qubit_names = {'0':'the bit on the left', '1':'the bit on the right'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 7:
          initialize = [['h', '1']]
          success_condition = {'IZ': -1.0}
          allowed_gates = {'0': {'NOT': 0, 'CNOT': 0}, '1': {'NOT': 0, 'CNOT': 0}, 'both': {}}
          vi = [[], False, True]
          qubit_names = {'0':'the bit on the left', '1':'the bit on the right'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
    case 2:
      match number:
        case 1:
          initialize = [ ["x","0"] ]
          success_condition = {"ZI":1.0}
          allowed_gates = { "0":{"x":3}, "1":{}, "both":{} }
          vi = [[1],True,True]
          qubit_names = {'0':'the only qubit', '1':None}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 2:
          initialize = [['x', '0']]
          success_condition = {'ZI': 1.0}
          allowed_gates = {'0': {'x': 0}, '1': {}, 'both': {}}
          vi = [[1], True, True]
          qubit_names = {'0':'the only qubit', '1':None}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 3:
          initialize = [['x', '1']]
          success_condition = {'IZ': 1.0}
          allowed_gates = {'0': {}, '1': {'x': 0}, 'both': {}}
          vi = [[0], True, True]
          qubit_names = {'0':None, '1':'the other qubit'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 4:
          initialize = []
          success_condition = {'ZI': 0.0}
          allowed_gates = {'0': {'h': 3}, '1': {}, 'both': {}}
          vi = [[1], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 5:
          initialize = [['h', '1']]
          success_condition = {'IZ': 1.0}
          allowed_gates = {'0': {}, '1': {'x': 3, 'h': 0}, 'both': {}}
          vi = [[0], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 6:
          initialize = [['h', '0'], ['z', '0']]
          success_condition = {'XI': 1.0}
          allowed_gates = {'0': {'z': 0, 'h': 0}, '1': {}, 'both': {}}
          vi = [[1], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 7:
          initialize = []
          success_condition = {'ZI': -1.0}
          allowed_gates = {'0': {'z': 0, 'h': 0}, '1': {}, 'both': {}}
          vi = [[1], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 8:
          initialize = [['h', '0']]
          success_condition = {'IX': 1.0}
          allowed_gates = {'0': {}, '1': {'z': 0, 'h': 0}, 'both': {}}
          vi = [[0], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 9:
          initialize = [['ry(pi/4)', '1']]
          success_condition = {'IZ': -0.7071, 'IX': -0.7071}
          allowed_gates = {'0': {}, '1': {'z': 0, 'h': 0}, 'both': {}}
          vi = [[0], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 10:
          initialize = [['x', '1']]
          success_condition = {'ZI': 0.0, 'IZ': 0.0}
          allowed_gates = {'0': {'x': 0, 'z': 0, 'h': 0}, '1': {'x': 0, 'z': 0, 'h': 0}, 'both': {}}
          vi = [[], True, False]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 11:
          initialize = [['h','0'],['h','1']]
          success_condition = {'ZZ': -1.0}
          allowed_gates = {'0': {'x': 0, 'z': 0, 'h': 0}, '1': {'x': 0, 'z': 0, 'h': 0}, 'both': {}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 12:
          initialize = [['x','0']]
          success_condition = {'XX': 1.0}
          allowed_gates = {'0': {'x': 0, 'z': 0, 'h': 0}, '1': {'x': 0, 'z': 0, 'h': 0}, 'both': {}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 13:
          initialize = []
          success_condition = {'XZ': -1.0}
          allowed_gates = {'0': {'x': 0, 'z': 0, 'h': 0}, '1': {'x': 0, 'z': 0, 'h': 0}, 'both': {}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 14:
          initialize = [['ry(-pi/4)', '1'], ['ry(-pi/4)','0']]
          success_condition = {'ZI': -0.7071, 'IZ': -0.7071}
          allowed_gates = {'0': {'x': 0}, '1': {'x': 0}, 'both': {}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 15:
          initialize = [['x', '1'], ['x','0']]
          success_condition = {'XI':1, 'IX':1}
          allowed_gates = {'0': {'z': 0, 'h': 0}, '1': {'z': 0, 'h': 0}, 'both': {}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
    case 3:
      match number:
        case 1:
          initialize = [['x', '0']]
          success_condition = {'ZI': 1.0, 'IZ': -1.0}
          allowed_gates = {'0': {'cx': 0}, '1': {'cx': 0}, 'both': {}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 2:
          initialize = [['h', '0'],['x', '1']]
          success_condition = {'XI': -1.0}
          allowed_gates = {'0': {'cz': 0}, '1': {}, 'both': {}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case "2b":
          initialize = [['h', '1'],['x', '0']]
          success_condition = {'IX': -1.0}
          allowed_gates = {'0': {'cz': 0}, '1': {}, 'both': {}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 3:
          initialize = [['h', '0'],['x', '1'],['h', '1']]
          success_condition = { }
          allowed_gates = {'0':{'cz': 2}, '1':{'cz': 2}, 'both': {}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case "3b":
          initialize = [['h', '0'],['x', '1'],['h', '1']]
          success_condition = { }
          allowed_gates = {'0': {}, '1': {}, 'both': {'cz': 2}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names, mode='y')
        case 4:
          initialize = [['x', '0']]
          success_condition = {'IZ': -1.0}
          allowed_gates = {'0': {'h':0}, '1': {'h':0}, 'both': {'cz': 0}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 5:
          initialize = [['h', '0'],['h', '1']]
          success_condition = {'XI': -1.0, 'IX': -1.0}
          allowed_gates = {'0': {}, '1': {'z':0,'cx': 0}, 'both': {}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 6:
          initialize = [('x','0'),('x','1')]
          success_condition = {'ZI': 1.0,'IZ': -1.0}
          allowed_gates = {'0': {'h':0}, '1': {'h':0,'cx':0}, 'both': {}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 7:
          initialize = [['ry(-pi/4)','0'],['ry(-pi/4)','0'],['ry(-pi/4)','0'],['x','0'],['x','1']]
          success_condition = {'ZI': -1.0,'XI':0,'IZ':0.7071,'IX':-0.7071}
          allowed_gates = {'0': {'h':0}, '1': {'h':0}, 'both': {'cz': 0}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case 8:
          initialize = [['x','0'],['h','1']]
          success_condition = {'XI':1,'IZ':-1}
          allowed_gates = {'0': {'h':0}, '1': {'h':0}, 'both': {'cz':3}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names,shots=2000)
        case 9:
          initialize = [['x','1']]
          success_condition = {'IZ':1.0,'ZI':-1.0}
          allowed_gates = {'0': {'h':0}, '1': {'h':0}, 'both': {'cz':0}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names,shots=2000)
    case 4:
      match number:
        case "1a":
          initialize = []
          success_condition = {}
          allowed_gates = {'0': {'ry(pi/4)': 4}, '1': {}, 'both': {}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)
        case "1b":
          initialize = [['x','0']]
          success_condition = {'XX': 1.0}
          allowed_gates = {'0': {'x': 0, 'z': 0, 'h': 0}, '1': {'x': 0, 'z': 0, 'h': 0}, 'both': {}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names, mode='line')
        case "1c":
          initialize = []
          success_condition = {'ZI': -1.0}
          allowed_gates = {'0': {'bloch':1, 'ry(pi/4)': 0}, '1':{}, 'both': {'unbloch':0}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names, mode='line')
        case 2:
          initialize = [['h','0'],['h','1']]
          success_condition = {'ZI': -1.0,'IZ': -1.0}
          allowed_gates = {'0': {'bloch':0, 'ry(pi/4)': 0, 'ry(-pi/4)': 0}, '1': {'bloch':0, 'ry(pi/4)': 0, 'ry(-pi/4)': 0}, 'both': {'unbloch':0}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names, mode='line')
        case 3:
          initialize = [['h','0']]
          success_condition = {'ZZ': 1.0}
          allowed_gates = {'0': {}, '1': {'bloch':0, 'ry(pi/4)': 0, 'ry(-pi/4)': 0}, 'both': {'unbloch':0,'cz':0}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names, mode='line')
        case 4:
          initialize = [['ry(pi/4)','0'],['ry(pi/4)','1']]
          success_condition = {'ZI': 1.0,'IZ': 1.0}
          allowed_gates = {'0': {'bloch':0, 'z':0, 'ry(pi/4)': 1}, '1': {'bloch':0, 'x':0, 'ry(pi/4)': 1}, 'both': {'unbloch':0}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names, mode='line')
        case 5:
          initialize = [['x','0'],['h','1']]
          success_condition = {'IZ': 1.0}
          allowed_gates = {'0': {}, '1': {'bloch':0, 'cx':0, 'ry(pi/4)': 1, 'ry(-pi/4)': 1}, 'both': {'unbloch':0}}
          vi = [[], True, True]
          qubit_names = {'0':'q[0]', '1':'q[1]'}
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names, mode='line')
    case 'bonus':
      match number:
        case "Sandbox":
          match sandbox_number:
            case 1:
              initialize = []
              success_condition = {'IZ': 1.0,'IX': 1.0}
              allowed_gates = {'0': {'bloch':0, 'x':0, 'z':0, 'h':0, 'cx':0, 'ry(pi/4)': 0, 'ry(-pi/4)': 0}, '1': {'bloch':0, 'x':0, 'z':0, 'h':0, 'cx':0, 'ry(pi/4)': 0, 'ry(-pi/4)': 0}, 'both': {'cz':0, 'unbloch':0}}
              vi = [[], True, True]
              qubit_names = {'0':'q[0]', '1':'q[1]'}
              puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names, mode='line')
            case 2:
              initialize = []
              success_condition = {'IZ': 1.0,'IX': 1.0}
              allowed_gates = {'0': {'x':0, 'z':0, 'h':0, 'cx':0, 'ry(pi/4)': 0, 'rx(pi/4)': 0, 'ry(-pi/4)': 0, 'rx(-pi/4)': 0}, '1': {'x':0, 'z':0, 'h':0, 'cx':0, 'ry(pi/4)': 0, 'rx(pi/4)': 0, 'ry(-pi/4)': 0, 'rx(-pi/4)': 0}, 'both': {'cz':0}}
              vi = [[], True, True]
              qubit_names = {'0':'q[0]', '1':'q[1]'}
              puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names, mode='y')
        case "Make your own puzzles":
          initialize = [['x', '0'],['cx', '1']]
          success_condition = {'IZ': 1.0}
          allowed_gates = {'0': {'h':0}, '1': {'h':0}, 'both': {'cz': 1}}
          vi = [[], True, True]
          qubit_names = {'0':'qubit 0', '1':'qubit 1'}
          mode = None
          puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names, mode=mode)
  return puzzle