n = int(raw_input("Please input the level of tower:\n"))

# function for hanoi tower
def hanoi(n):
    hanoiHelper(n, 'TowerA', 'TowerB', 'TowerC')

def hanoiHelper(n, origin, helper, destination):
    if n == 1: # base case
            print 'Move disk', n, 'from', origin, 'to', destination
    else: # recursive case
            hanoiHelper(n-1, origin, destination, helper)
            print 'Move disk', n, 'from', origin, 'to', destination
            hanoiHelper(n-1, helper, origin, destination)
            
#test function
hanoi(n)


n = int(raw_input("Please input the level of the tower:\n"))

# function for the hanoi tower
