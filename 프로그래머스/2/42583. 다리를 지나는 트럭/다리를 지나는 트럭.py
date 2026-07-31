from collections import deque 

def solution(bridge_length, weight, truck_weights):
    sec = 1
    current_weight = 0 
    bridge = deque() 
    
    for truck in truck_weights:
        while bridge and bridge[0][1] <= sec:
            exited_weight, _ = bridge.popleft()
            current_weight -= exited_weight 
        
        while current_weight + truck > weight:
            sec = bridge[0][1]
    
            while bridge and bridge[0][1] <= sec:
                exited_weight, _ = bridge.popleft()
                current_weight -= exited_weight            
        
        bridge.append((truck, sec + bridge_length))
        current_weight += truck 
        sec += 1
    
    return bridge[-1][1]