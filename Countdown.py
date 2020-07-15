import sys

#Stores a state which can be expanded 
class State:

    #Constructor
    def __init__(self, eqn, usedNums):
        self.eqn = eqn

        #Records the numbers which have been used in the equation already
        #This is easier than processing the equation string for if the number is in the string
        self.usedNums = usedNums

    #Evaluates the value of the state
    def Evaluate():
        return eval(eqn)

    #Expands the current state into more states
    def Expand(nums, operators):
        #Holds the values of the new states
        newStates = []

        #For each of the possible numbers to use
        for num in nums:
            if not num in usedNums:
                #Creates a new list of the used numbers
                newUsedNums = usedNums.copy()
                #Adds the new number to this list
                newUsedNums.append(num)

                #Adds the new number with each operator
                for op in operators:
                    #Creates the new states
                    if not op == '+' and not op == '-':                    
                        newStates.append(State(self.eqn+op+'-'+str(num), newUsedNums))
                    newStates.append(State(self.eqn+op+str(num), newUsedNums))
                    
        return newStates


def main(arr):
    if(len(arr) == 0):
        ValidInput()

def ValidInput():
    print('Valid Input:\nMultiple numbers\nA Target Number\ne.g. python3 Countdown.py 2 3 4 5 100')

if __name__ == '__main__':
    main(sys.argv[1:])