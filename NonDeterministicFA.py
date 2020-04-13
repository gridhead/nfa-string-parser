import DeterministicFA
import sys

def CheckIfTerminal(s):
    if not s:
        return False
    else:
        for x in s:
            if DeterministicFA.CheckIfTerminal(x):
                return True
        return False

def EpsillonClosure(s):
    t = list(s)
    b = set(t)
    while len(t) != 0:
        u = t.pop()
        r = DeterministicFA.LookupFunction(u,DeterministicFA.eps_symb)
        if r != None:
            for v in r:
                if not (v in b):
                    b.add(v)
                    t.append(v)
    return b

def MainFunction(NFAString, TestString):
    DeterministicFA.ReadFiniteAutomata(NFAString)
    FiniteAutoOutput = DeterministicFA.ObtainFiniteAutomata()
    FunctionOutput = FiniteAutoOutput + "<br/>" + "<pre>"
    instr = TestString
    ss = DeterministicFA.GetStartState()
    x = []
    x.append(DeterministicFA.GetStartState())
    s1 = set(x)
    s1 = EpsillonClosure(s1)
    FunctionOutput = FunctionOutput + "Start:\n   " + str(list(s1)) + "\n"
    i = 0
    while instr[i] != '$':
        s2 = set()
        for y in s1:
            s = DeterministicFA.LookupFunction(y, instr[i])
            if not s:
                s = set()
            else:
                s = set(s)
            s2 = s2 | s
        s2 = EpsillonClosure(s2)
        FunctionOutput = FunctionOutput + str(instr[i]) + ": " + str(list(s2))
        if CheckIfTerminal(s2):
            FunctionOutput = FunctionOutput + " term "
        FunctionOutput = FunctionOutput + "\n"
        s1 = s2
        i = i + 1
    FunctionOutput = FunctionOutput + "</pre>"
    return FunctionOutput