def solution(bridge_length, weight, truck_weights):
    sec = 1
    truck_stack = []
    truck_stack.append((sec, truck_weights.pop(0)))

    while truck_stack:
        sec += 1

        if sec - truck_stack[0][0] == bridge_length:
            truck_stack.pop(0)

        current_weight = sum(truck[1] for truck in truck_stack)

        if (
            truck_weights
            and len(truck_stack) < bridge_length
            and truck_weights[0] <= weight - current_weight
        ):
            truck_stack.append((sec, truck_weights.pop(0)))

    return sec

"""
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 함 
최대 bridge_legth대까지 올라갈 수 있음
다리는 weight 이하까지의 무게를 견딜 수 있음 
완전히 오르지 않은 건 무시 

1. stack <- pushleft()
2. while stack 
    1. sec ++ 
    2. if (len(stack) < bridge_length) and (truck_weights[i] <= weight - truck_weigths[0]) : stack <- pushleft() 
"""
