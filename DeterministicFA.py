import sys
import re

dfa = True
fa = []
ss = 0
stn = None
terms = []
symbs = None
eps = False
eps_symb = '@'

def ReadFiniteAutomata(textform):
    textline = textform.split("\n")
    line = textline[0]
    r1 = re.compile(R"\s*(\d+).*")
    m1 = r1.search(line)
    global stn
    stn = int(m1.group(1))
    global symbs
    symbs = textline[1]
    stp = textline[2]
    ssn = 0
    tn  = 0
    for i in range(0,stn):
        fa.append((int(stp[i]), []))
        if stp[i] == '1' or stp[i] == '3':
            global ss
            ss = i
            ssn = ssn + 1
        if stp[i] == '2' or stp[i] == '3':
            terms.append(i)
            tn = tn + 1
    if ssn != 1:
        sys.stdout.write("ERR, != 1 start st")
    if tn < 1:
        sys.stdout.write("ERR, 0 term states")
    r2 = re.compile(R"\s*(\d+)\s+(\S)\s+(\d+)")
    for line in textline[3:]:
        m2 = r2.search(line)
        st1 = int(m2.group(1))
        st2 = int(m2.group(3))
        sym = m2.group(2)
        if sym == eps_symb:
            global eps
            eps = True
        fa[st1][1].append( (sym, st2) )
    global dfa
    dfa = CheckDeterministicFA()

def CheckDeterministicFA():
    for i in range(0,stn):
        for ch in symbs:
            t = LookupFunction(i, ch)
            if t != None and len(t) >= 2:
                return False
    return True
                  
def LookupFunction(state, symb):
    ret = []
    if state < 0 or state >= len(fa):
        return None
    elif len(fa[state][1]) == 0:
        return None
    else:
        t = len(fa[state][1])
        for i in range(0,t):
            if fa[state][1][i][0] == symb:
                ret.append(fa[state][1][i][1])
        return ret

def GetStartState():
    return ss

def GetTerminals():
    return terms

def CheckIfTerminal(state):
    if fa[state][0] == 2 or fa[state][0] == 3:
        return True
    return False

def CheckIfDeterministicFA():
    return dfa
    
def ObtainFiniteAutomata():
    FunctionOutput = "<pre>"
    if eps:
        FunctionOutput = FunctionOutput + "<b>NFA with epsilon</b>" + "\n"
    elif dfa:
        FunctionOutput = FunctionOutput + "<b>DFA</b>" + "\n"
    else:
        FunctionOutput = FunctionOutput + "<b>NFA</b>" + "\n"
    FunctionOutput = FunctionOutput + "<b>States: </b>" + str(stn) + "\n" + "<b>Symbols: </b>" + str(symbs) + "\n\n"
    for i in range(0,stn):
        if i < 10:
            FunctionOutput = FunctionOutput + " " + str(i)
        else:
            FunctionOutput = FunctionOutput + str(i)
        if i == ss:
            FunctionOutput = FunctionOutput + "s"
        else:
            FunctionOutput = FunctionOutput + " "
        if CheckIfTerminal(i):
            FunctionOutput = FunctionOutput + "t:"
        else:
            FunctionOutput = FunctionOutput + " : "
        FunctionOutput = FunctionOutput + str(fa[i]) + "\n"
    FunctionOutput = FunctionOutput + "</pre>"
    return FunctionOutput