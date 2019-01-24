'''
jichunli_FarmerFox.py
by Jichun Li

Assignment 2, in CSE 415, Winter 2019.

This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''

# <METADATA>
SOLUZION_VERSION = "1.0"
PROBLEM_NAME = "Farmer, Fox, Chicken, and Grain"
PROBLEM_VERSION = "1.0"
PROBLEM_AUTHORS = ['J. Li']
PROBLEM_CREATION_DATE = "20-JAN-2019"
PROBLEM_DESC = \
    '''
A farmer needs to take a fox, chicken and sack of grain across a river using
a small boat. He can only take one of the three items in the boat with him at
one time. The fox must never be left alone with the chicken, and the chicken
must never be left alone with the grain. The Goal is to move the farmer, fox,
chicken and grain from left bank of the river to the right bank of the river.
'''
# </METADATA>


# <COMMON_DATA>
# </COMMON_DATA>


# <COMMON_CODE>
FARMER = 0  # array index of farmer
FOX = 1  # array index of fox
CHICKEN = 2  # array index of chicken
GRAIN = 3  # array index of grain

LEFT = 0  # array index of left bank
RIGHT = 1  # array index of left bank


class State:
    def __init__(self, d=None):
        # Initializing the state
        if d is None:
            d = {'item': [[0, 0], [0, 0], [0, 0], [0, 0]],
                 'boat': LEFT}
        self.d = d

    def __eq__(self, s2):
        # Testing if two states are equal
        for prop in ['item', 'boat']:
            if self.d[prop] != s2.d[prop]:
                return False
        return True

    def __str__(self):
        # Producing a textual description of a state
        p = self.d['item']
        txt = "\n Farmer on left:" + str(p[FARMER][LEFT]) + "\n"
        txt += "   Fox on left:" + str(p[FOX][LEFT]) + "\n"
        txt += "   Chicken on left:" + str(p[CHICKEN][LEFT]) + "\n"
        txt += "   Grain on left:" + str(p[GRAIN][LEFT]) + "\n"
        txt += " Farmer on right:" + str(p[FARMER][RIGHT]) + "\n"
        txt += "   Fox on right:" + str(p[FOX][RIGHT]) + "\n"
        txt += "   Chicken on right:" + str(p[CHICKEN][RIGHT]) + "\n"
        txt += "   Grain on right:" + str(p[GRAIN][RIGHT]) + "\n"
        side = 'left'
        if self.d['boat'] == RIGHT:
            side = 'right'
            txt += " boat is on the " + side + ".\n"
        return txt

    def __hash__(self):
        # Hashing the state
        return (self.__str__()).__hash__()

    def copy(self):
        # Performs an appropriately deep copy of a state,
        # for use by operators in creating new states.
        news = State({})
        news.d['item'] = [self.d['item'][F_f_c_g][:] for F_f_c_g in [FARMER,
                                                                     FOX,
                                                                     CHICKEN,
                                                                     GRAIN]]
        news.d['boat'] = self.d['boat']
        return news

    def can_move(self, farmer, fox, chicken, grain):
        """
        Tests whether it's legal to move the boat and take F farmer, f fox,
        c chickens, and g grain."""
        side = self.d['boat']  # Where the boat is.
        p = self.d['item']
        if p[FARMER][side] == 0:
            # The farmer and boat are not on the same side
            return False

        fox_available = p[FOX][side]
        if fox_available < fox:
            # Can't take more foxes than available
            return False

        chicken_available = p[CHICKEN][side]
        if chicken_available < chicken:
            # Can't take more chicken than available
            return False

        grain_available = p[GRAIN][side]
        if grain_available < grain:
            # Can't take more grain than available
            return False

        if fox == 1:
            # Moving fox
            if (p[FOX][1 - LEFT] == p[CHICKEN][LEFT]
                # fox with chicken
                    and p[FOX][1 - LEFT] != p[GRAIN][LEFT]
                    and p[FARMER][LEFT] == p[FOX][1 - LEFT]):
                return False
            if (p[CHICKEN][LEFT] == p[GRAIN][LEFT]
                # chicken with grain
                    and p[CHICKEN][LEFT] != p[FOX][1 - LEFT]
                    and p[FARMER][LEFT] == p[CHICKEN][LEFT]):
                return False
        elif chicken == 1:
            # Moving chicken
            if (p[FOX][LEFT] == p[CHICKEN][1 - LEFT]
                # chicken with fox
                    and p[FOX][LEFT] != p[GRAIN][LEFT]
                    and p[FOX][LEFT] == p[FARMER][LEFT]):
                return False
            if (p[CHICKEN][1 - LEFT] == p[GRAIN][LEFT]
                # chicken with grain
                    and p[CHICKEN][1 - LEFT] != p[FOX][LEFT]
                    and p[CHICKEN][1 - LEFT] == p[FARMER][LEFT]):
                return False
        elif grain == 1:
            # Moving grain
            if (p[CHICKEN][LEFT] == p[GRAIN][1 - LEFT]
                # grain with chicken
                    and p[CHICKEN][LEFT] != p[FOX][LEFT]
                    and p[CHICKEN][LEFT] == p[FARMER][LEFT]):
                return False
            if (p[FOX][LEFT] == p[CHICKEN][LEFT]
                # fox with chicken
                    and p[FOX][LEFT] != p[GRAIN][1 - LEFT]
                    and p[FOX][LEFT] == p[FARMER][LEFT]):
                return False

        return True

    def move(self, farmer, fox, chicken, grain):
        """Assuming it's legal to make the move, this computes
         the new state resulting from moving the boat carrying
         the farmer and f foxes, c chickens, and g grains"""
        news = self.copy()  # start with a deep copy.
        side = self.d['boat']  # where is the boat?
        p = news.d['item']  # get the array of arrays of item.
        p[FARMER][side] = p[FARMER][side] - farmer  # Remove farmer from the current side.
        p[FOX][side] = p[FOX][side] - fox  # Remove fox from the current side.
        p[CHICKEN][side] = p[CHICKEN][side] - chicken  # Remove chicken from the current side.
        p[GRAIN][side] = p[GRAIN][side] - grain  # Remove grain from the current side.
        p[FARMER][1 - side] = p[FARMER][1 - side] + farmer  # Add farmer at the other side.
        p[FOX][1 - side] = p[FOX][1 - side] + fox  # Add Fox to other side
        p[CHICKEN][1 - side] = p[CHICKEN][1 - side] + chicken  # Add Chicken to the other side.
        p[GRAIN][1 - side] = p[GRAIN][1 - side] + grain  # Add Grain to other side
        news.d['boat'] = 1 - side  # Move the boat itself.
        return news


def goal_test(s):
    """If all items are on the right, then s is a goal state."""
    p = s.d['item']
    return p[FOX][RIGHT] == 1 and p[CHICKEN][RIGHT] == 1 and p[GRAIN][RIGHT] == 1 and p[FARMER][RIGHT] == 1


def goal_message(s):
    return "Congratulations on successfully guiding the farmer and fox, chicken, and grain across the river!"


class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)


# </COMMON_CODE>


# <INITIAL_STATE>
CREATE_INITIAL_STATE = lambda: State(d={'item': [[1, 0], [1, 0], [1, 0], [1, 0]], 'boat': LEFT})
# </INITIAL_STATE>


# <OPERATORS>
Ffcg_combinations = [(1, 0, 0, 0),
                   (1, 1, 0, 0),
                   (1, 0, 1, 0),
                   (1, 0, 0, 1)]

OPERATORS = [Operator(
    "Cross the river with " + str(farmer) + " Farmers, " + str(fox) + " fox, " + str(chicken) + " chicken, and " + str(
        grain) + " grain",
    lambda s, farmer1=farmer, fox1=fox, chicken1=chicken, grain1=grain: s.can_move(farmer1, fox1, chicken1, grain1),
    lambda s, farmer1=farmer, fox1=fox, chicken1=chicken, grain1=grain: s.move(farmer1, fox1, chicken1, grain1))
    for (farmer, fox, chicken, grain) in Ffcg_combinations]
# </OPERATORS>


# <GOAL_TEST>
GOAL_TEST = lambda s: goal_test(s)
# </GOAL_TEST>

# </GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
# </GOAL_MESSAGE_FUNCTION>

