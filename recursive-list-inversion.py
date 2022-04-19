def invertList(List):
    if len(List) == 1:
        return List
    else:
        return invertList(List[1:]) + [List[0]]