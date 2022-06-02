
from linked_list import LinkedList

def solve_list(problems, func):
    
    for prob in problems:
        
        args, ans = prob
        
        ans_ll = LinkedList.array_to_linked_list(ans)
        args_ll = [LinkedList.array_to_linked_list(arg) for arg in args]
        
        print(f"Solving Problem: {args}")
        print(f"Answer: {ans}: {ans_ll}")
        sol = func(*args_ll)
        sol_ll = LinkedList()
        sol_ll.head = sol
        print(f"Solution: {sol_ll.head}")
        print(f"Success: {sol_ll==LinkedList(ans)}")
        print()
        
def solve(problems, func):
    
    for prob in problems:
        
        args, ans = prob
        args_ll = [LinkedList.array_to_linked_list(arg) for arg in args]
        
        print(f"Solving Problem: {args}")
        print(f"Answer: {ans}: {ans}")
        sol = func(*args_ll)
        print(f"Solution: {sol}")
        print(f"Success: {sol==ans}")
        print()