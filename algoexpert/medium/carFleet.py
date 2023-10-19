# if a car starting at a later position is going to reach the target
# earlier than the car that started from a position closer to the target
# then the fast car and slow car are going to form a fleet and they are going to
# move together at the speed of the slower car, hence we pop the time of the fast car
# and keep the time of the slower car on the stack, the stack represents the
# number of fleets and the time at which each fleet is going to reach the target

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for p,s in zip(position,speed):
            pairs.append((p,s))
        
        pairs.sort(reverse=True)
        fleets = []

        for p,s in pairs:

            t = (abs(target-p)/s)
            fleets.append(t)
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
            
        return len(fleets)

