##nodes = ['A', 'B', 'C', 'D']
##start_node = nodes[0]
##final_node = nodes[len(nodes)-1]
##
##for i in range(len(nodes)):
##    print(" The node at index number " , i , " is = " , nodes[i])
##
### Taking nodes as input from the user:
##
##total_nodes = int(input(" Enter how many nodes you want to give for DFA traversing:"))
##nodes_type = input(" Enter the type of nodes as well like numbers or alphabets:")
##nodes_list = []
##for i in range(total_nodes):
##    if(nodes_type == "number" or nodes_type =="Number"):
##       inputs = input(" Enter the nodes in numbers form: ")
##       nodes_list.append(inputs)
##       print(nodes_list)
##    elif(nodes_type == "alphabets" or nodes_type == "Alphabets"):
##        inputs = input(" Enter the nodes in alphabetic form: ")
##        nodes_list.append(inputs)
##        print(nodes_list)
##    else:
##        print(" You entered an in-valid nodes type.")
##        break;

# DFA Implementation in Python

# 5-tuple collection

states = []
alphabets = []
start_state = ""
accept_states = []
transition = {}

# Input which the DFA will accept/reject
input_string = ""
# The states and input alphabest will be represented as a list of strings
print("Enter the states of DFA separated by space: ", end="")
states = input().split()

print("Enter the numbers or weights which require b/w transition separated by space: ", end="")
alphabets = input().split()

# Start and accepted states
print("Enter the start state of the automata: ", end="")
start_state = input()

print("Enter the final states of the automaton separated by space: ", end="")
accept_states = input().split()

# Transition function is a dictionary where
#   key = (current_state, input)
#   value = next_state  (None for rejected states)

print("Enter the next states for the following")
for state in states:
    for alpha in alphabets:
        print(f"\t  {alpha}")
        print(f"{state}\t---->\t", end="")
        dest = input()
        
        # Rejected states are represented as None in the dictionary
        if dest == ".":
            transition[(state, alpha)] = None
        else:
            transition[(state, alpha)] = dest


print("Enter the input string to run the automata: ", end="")
input_string = input()

# Start parsing the input string with the current state as start state
current_state = start_state

for char in input_string:
    # Transition to the next state using the current state and input alphabet
    current_state = transition[(current_state, char)]
    
    # Check whether the DFA goes into a dead/rejected state
    if current_state is None:
        print("Not possible because the initial state is None or not defined.")
        break
else:
    
    
    # When entire string is parsed, check whether the final state is an accepted state
    if (current_state in accept_states):
         print(" The string which was given above is reaching to the final state and hence it is Accepted")
    else:
        print(" The string which was given above is not reaching to the final state and hence it is Rejected")

    
       
