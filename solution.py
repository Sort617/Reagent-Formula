def isValid(formula):
    if (5 in formula and 6 not in formula) or (5 not in formula and 6 in formula): return False
    if 1 in formula and 2 in formula: return False
    if 3 in formula and 4 in formula: return False
    if 7 in formula or 8 in formula: return True
    if 7 or 8 not in formula: return False
    else: return True
