# Problem: 2751. Robot Collisions
# Difficulty: Hard
# Link: https://leetcode.com/problems/robot-collisions/description

# Time Complexity: O(N log N) - We sort the robots by position initially, and sort the survivors by their original index at the end. The stack operations (push/pop) take O(N) overall.
# Space Complexity: O(N) - We store the grouped robot data and the stack of survivors.

from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        
        # Package the data together: [position, health, direction, original_index]
        robots = []
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])
            
        # Sort robots strictly by their starting position (left-to-right)
        robots.sort(key=lambda x: x[0])
        
        stack = []
        
        # Simulate the collisions
        for robot in robots:
            # If moving Right, it just drives forward. Put it on the stack to wait.
            if robot[2] == 'R':
                stack.append(robot)
            else:
                # The robot is moving Left! It will smash into any Right-moving robots ahead of it.
                while stack and stack[-1][2] == 'R' and robot[1] > 0:
                    
                    if stack[-1][1] < robot[1]:
                        # The stack robot dies, our current robot loses 1 HP and keeps going
                        stack.pop()
                        robot[1] -= 1
                        
                    elif stack[-1][1] > robot[1]:
                        # Our current robot dies, the stack robot loses 1 HP
                        stack[-1][1] -= 1
                        robot[1] = 0
                        
                    else:
                        # Both robots have equal health and destroy each other
                        stack.pop()
                        robot[1] = 0
                        
                # If the current Left-moving robot survived the carnage, it safely joins the stack
                if robot[1] > 0:
                    stack.append(robot)
                    
        # Restore the original input order for the survivors
        stack.sort(key=lambda x: x[3])
        
        # Extract and return just the health values
        return [robot[1] for robot in stack]

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: L clears out smaller R's
    print(f"Test 1: {sol.survivedRobotsHealths([5,4,3,2,1], [2,17,9,15,10], 'RRRRR')}") 
    # Expected: [2, 17, 9, 15, 10] (No collisions, everyone moves Right)
    
    # Test 2: The massive collision
    print(f"Test 2: {sol.survivedRobotsHealths([3,5,2,6], [10,10,15,12], 'RLRL')}") 
    # Expected: [14]
    # (Robot 2 goes R, Robot 5 goes L. 10 vs 10 = Both die. 
    #  Robot 2 goes R(15), Robot 6 goes L(12). 15 vs 12 = Robot 2 wins with 14 HP. Original index 2 is the winner!)