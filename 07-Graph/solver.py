from graph import Graph
from inspect import signature

def solve_graph(problems, func):
        
    for prob in problems:
        
        args, ans = prob
        
        args_graph = [Graph(arg).root if isinstance(arg, list) else arg for arg in args]
        ans = Graph(ans).root if "Node" in str(signature(func).return_annotation) else ans
        
        print(f"SOLVING:\n{args} : {args_graph}\n")
        sol = func(*args_graph)
        print(f"CORRECT ANSWER:\n{ans}\n")
        print(f"SOLUTION:\n{sol}\n")
        res = f"SUCCESS: {sol==ans}"
        print(f"{'='*len(res)}")
        print(res)
        print(f"{'='*len(res)}\n\n")
