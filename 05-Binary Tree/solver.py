from binary_tree import BTree
from inspect import signature

def solve_tree(problems, func):
        
    for prob in problems:
        
        args, ans = prob
        
        args_tree = [BTree(arg).root if isinstance(arg, list) else arg for arg in args]
        ans = BTree(ans).root if "TreeNode" in str(signature(func).return_annotation) else ans
        
        print(f"SOLVING:\n{args} : {args_tree}\n")
        sol = func(*args_tree)
        print(f"CORRECT ANSWER:\n{ans}\n")
        print(f"SOLUTION:\n{sol}\n")
        res = f"SUCCESS: {sol==ans}"
        print(f"{'='*len(res)}")
        print(res)
        print(f"{'='*len(res)}\n\n")
