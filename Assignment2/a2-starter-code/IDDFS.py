''' jichunli_IDDFS.py
by Jichun Li
Iterative-Deepening Depth-First Search of a problem space.
 Version 0.4, January 23, 2019.

 Usage:
 python3 jichunli_IDDFS.py TowersOfHanoi
'''

import sys

if sys.argv == [''] or len(sys.argv) < 2:
    #  import EightPuzzle as Problem
    import TowersOfHanoi as Problem
else:
    import importlib

    # Import User entered Problem as Problem
    Problem = importlib.import_module(sys.argv[1])

print("\nWelcome to jichunli_IDDFS")
COUNT = None
BACKLINKS = {}

'''
    Creating the initial state and running IDDFS
'''
def runIDDFS():
    initial_state = Problem.CREATE_INITIAL_STATE()
    print("Initial State:")
    print(initial_state)
    global COUNT, BACKLINKS, MAX_OPEN_LENGTH
    COUNT = 0
    BACKLINKS = {}
    MAX_OPEN_LENGTH = 0
    i = 0
    goal_state_reached = False
    while not goal_state_reached:
        goal_state_reached = IterativeDDFS(initial_state, i)
        i += 1
    print(str(COUNT) + " states expanded.")
    print('MAX_OPEN_LENGTH = ' + str(MAX_OPEN_LENGTH))


'''
    Implementing Iterative Breadth First Search
'''
def IterativeDDFS(initial_state, DEPTH):
    global COUNT, BACKLINKS, MAX_OPEN_LENGTH
    ITER_DEPTH = 0

    # STEP 1. Put the start state on a list OPEN
    OPEN = [(initial_state, ITER_DEPTH)]  # tuple of (state, depth of state)
    CLOSED = []
    BACKLINKS[initial_state] = None

    # STEP 2. If OPEN is empty, output “DONE” and stop.
    while OPEN != []:
        report(OPEN, CLOSED, COUNT)
        if len(OPEN) > MAX_OPEN_LENGTH: MAX_OPEN_LENGTH = len(OPEN)

        # STEP 3. Select the first state on OPEN and call it S.
        #         Delete S from OPEN.
        #         Put S on CLOSED.
        #         If S is a goal state, output its description
        List_Depth = OPEN.pop(0)
        S = List_Depth[0]
        CURRENT_DEPTH = List_Depth[1]
        CLOSED.append(S)

        if Problem.GOAL_TEST(S):
            print(Problem.GOAL_MESSAGE_FUNCTION(S))
            path = backtrace(S)
            print('Length of solution path found: ' + str(len(path) - 1) + ' edges')
            return True  # Return True to break while loop in runIDDFS

        # STEP 4. Generate the list L of successors of S and delete
        #         from L those states already appearing on CLOSED.

        if (CURRENT_DEPTH <= DEPTH):
            COUNT += 1  # Only increments states expanded when the current depth is <= max depth.
            L = []
            for op in Problem.OPERATORS:
                if op.precond(S):
                    new_state = op.state_transf(S)
                    if not (new_state in CLOSED):
                        L.append((new_state, CURRENT_DEPTH + 1))
                        if new_state not in BACKLINKS:  # makes sure it doesn't override existing backlinks
                            BACKLINKS[new_state] = S

            # STEP 5. Delete from OPEN any members of OPEN that occur on L.
            #         Insert all members of L at the front of OPEN.
            for s2 in L:
                for i in range(len(OPEN) - 1, -1, -1):  # Checks OPEN in reverse
                    if (OPEN[i][0] == s2[0]):
                        del OPEN[i];

            OPEN = L + OPEN
            print_state_list("OPEN", OPEN)

            # STEP 6. Go to Step 2.

'''
  Printing function for State Objects. 
'''
def print_state_list(name, lst):
    if (lst != []):
        print(name + " is now: ", end='')
        for s in lst[:-1]:
            print(str(s[0]), end=', ')
        print(str(lst[-1][0]))


'''
  Backtracing the state S by seeing which state S is a child of.
'''
def backtrace(S):
    global BACKLINKS
    path = []
    while S:
        path.append(S)
        S = BACKLINKS[S]
    path.reverse()
    print("Solution path: ")
    for s in path:
        print(s)
    return path


'''
 Reporting the length of OPEN, length of CLOSED, and the number of states expanded so far.
'''
def report(open, closed, count):
    print("len(OPEN)=" + str(len(open)), end='; ')
    print("len(CLOSED)=" + str(len(closed)), end='; ')
    print("COUNT = " + str(count))


if __name__ == '__main__':
    runIDDFS()

