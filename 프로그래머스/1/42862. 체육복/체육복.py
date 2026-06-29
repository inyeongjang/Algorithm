def solution(n, lost, reserve):
    
    _lost = [l for l in lost if not l in reserve]
    _reserve = [r for r in reserve if not r in lost]
    
    for student in sorted(_reserve):
        if student - 1 in _lost:
            _lost.remove(student - 1)
        elif student + 1 in _lost:
            _lost.remove(student + 1) 

    return n - len(_lost) 