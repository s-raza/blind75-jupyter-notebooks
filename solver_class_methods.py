from typing import Tuple, List, Union

def solve_one(cls, cmds: List[Tuple[str, Union[int, List]]], **kwargs):
    
    q = cls(kwargs.get("init_kwargs"))
    res = []
    
    for cmd in cmds:
        
        cmd_name, args = cmd
        func = getattr(q, cmd_name)
        output = func(*args)
        res.append(output)
        
    return res

def solve(problems):
    
    for prob in problems:
        
        args, ans = prob
        
        
        print(f"{args=}")
        
        print(f"Solving: {args}")
        print(f"Ans: {ans}")
        sol = solve_one(*args[1:], **args[0])
        print(f"Solution: {sol}")
        print(f"Success: {sol==ans}")
        print()