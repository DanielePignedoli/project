#! /usr/bin/env python3

def generate_state():
    return "                   \u25b2                   "


def evolve(stato,lenght):
    rule30 = {"\u25b2\u25b2\u25b2": ' ',"\u25b2\u25b2 ": ' ',"\u25b2 \u25b2": ' ',"   ": ' ',
          "\u25b2  ": '\u25b2'," \u25b2\u25b2": '\u25b2'," \u25b2 ": '\u25b2',"  \u25b2": '\u25b2',}
    new_state=''
    for i in range(lenght):
    	if i ==0:
    		new_state= new_state+rule30[' '+stato[i:i+2]]
    	elif i == lenght-1:
    		new_state = new_state+rule30[stato[i-1:i+1]+' ']
    	else:
    		new_state = new_state + rule30[stato[i-1:i+2]]
    return new_state
	
def simulation(nsteps):
    initial_state = generate_state()
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state,len(initial_state))
        states_seq.append(new_state)
    return states_seq

########################################################

def test_generation_valid_state():
    state = generate_state()
    assert set(state) == {' ', '\u25b2'}
    

def test_generation_single_alive():
    state = generate_state()
    num_of_0 = sum(1 for i in state if i=='\u25b2')
    assert num_of_0 == 1


list = simulation(20)
for j in range(20):
	print(list[j])
