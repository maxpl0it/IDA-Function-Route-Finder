# Finds a path to a path in win32k to a callable function

def ntpath(from_name, visited=None, depth=0, max_depth=8):
    return_me = None;
    if visited is None:
        visited = list()
    if from_name[:5] == "_call":
        return_me = [[from_name] + visited]
    elif from_name not in visited and depth < max_depth:
        return_list = [i for i in [ntpath(idc.get_func_name(i.frm), visited=[from_name] + visited, depth=depth+1, max_depth=max_depth) for i in XrefsTo(idc.LocByName(from_name))] if i is not None and len(i) != 0]
        returnable = list()
        for i in return_list:
          if i not in returnable:
            returnable += i
        return_me = list(returnable)
    else:
        return None
    if depth == 0:
        return "\n".join(set([' -> '.join(i) for i in return_me]))
    else:
        return return_me
