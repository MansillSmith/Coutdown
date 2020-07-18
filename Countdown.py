import sys

operators = ['+','-','*','/']

#Stores a state which can be expanded 
class State:

    #Constructor
    def __init__(self, eqn, usedNums):
        self.eqn = eqn

        #Records the numbers which have been used in the equation already
        #This is easier than processing the equation string for if the number is in the string
        self.usedNums = usedNums
    
    def __str__(self):
        return self.eqn

    #Evaluates the value of the state
    def Evaluate(self):
        return eval(self.eqn)

    #Expands the current state into more states
    def Expand(self, nums, operators):
        #Holds the values of the new states
        newStates = []

        #For each of the possible numbers to use
        for num in nums:
            if not num in self.usedNums:
                #Creates a new list of the used numbers
                newUsedNums = self.usedNums.copy()
                #Adds the new number to this list
                newUsedNums.append(num)

                #Adds the new number with each operator
                for op in operators:
                    #Creates the new states
                    newStates.append(State(self.eqn+op+str(num), newUsedNums))
                    if not op == '+' and not op == '-':                    
                        newStates.append(State(self.eqn+op+'-'+str(num), newUsedNums))
                    
        return newStates

#Initialises the queue
def InitialiseQueue(arr):
    queue = []
    for i in arr:
        queue.append(State(str(i), [i]))
        queue.append(State('-' + str(i), [i]))
    return queue

#Converts the input list of strings into ints
def convertToIntList(arr):
    nums = []
    try:
        for i in arr:
            nums.append(int(i))
        return nums
    except:
        return None

def main(arr):
    #If the correct number of inputs were used
    if(len(arr) == 0):
        ValidInput()
    else:
        nums = convertToIntList(arr)
        if nums is None:
            ValidInput()
        else:
            #The input was valid
            target = nums[-1]
            nums = nums[:-1]
            queue = InitialiseQueue(nums)

            #Records the best state
            bestState = None
            bestValue = 0

            #While the queue is not empty
            while(queue):
                #Removes the first item in the queue
                state = queue.pop(0)
                value = state.Evaluate()

                #If the value is closer to the target than the current one
                if abs(target - value) < abs(target - bestValue):
                    bestState = state
                    bestValue = value                    
                #If the value is the target value
                if value == target:
                    break

                #Expand the current state
                queue.extend(state.Expand(nums, operators))

            print(bestState)
            print(bestValue)


def printQueue(queue):
    for i in queue:
        print(i)


def ValidInput():
    print('Valid Input:\nMultiple numbers\nA Target Number\ne.g. python3 Countdown.py 2 3 4 5 100')

if __name__ == '__main__':
    main(sys.argv[1:])