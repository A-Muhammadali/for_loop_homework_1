def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    x=[]
    for i in(list1):
        a=i.title()
        x.append(a)
    return x
print(main(['rustam', 'diyor', 'alisher', 'bektosh']))