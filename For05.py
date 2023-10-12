def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    x=[]
    for i in range(B,A-1,-1):
        x.append(i)
    return x
print(main(2,7))