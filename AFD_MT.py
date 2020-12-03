# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:50:22 2020

@author: llpulido
"""
def turingMachine():
        
    entry = open('input.txt').read()
    input = str(entry)
    program = open('program_MT.txt').read()
    state = 0
    trf = {}
    state = str(state)
    tape = ''.join(['_'] * 1000)
    head = 1000 // 2   
    tape = tape[:head] + input + tape[head:]
    for line in program.splitlines():
            s, a, r, d, s1 = line.split(' ')
            trf[s,a] = (r, d, s1)
    
    iter = 0
    while state != 'H' and iter < 9999:
        if state != 'H':
            a = tape[head]
            action = trf.get((state, a))
            if action:
                r, d, s1 = action
                tape = tape[:head] + r + tape[head+1:]
                if d != '*':
                    head = head + (1 if d == 'r' else -1)
                state = s1
                print(tape.replace('_', ''), state)
        iter += 1
    print(tape.replace('_', ''))

def finiteAutomata():
    d = {}
    efe = {''}
    
    def find(string, character):
        index = 0
        while (index < len(string)):
            if string[index] == character:
                return index
            index += 1
        return -1
    
    def AFD(d, q0, F, tape):
        q = q0
        for simbol in tape:
            q = d[q, simbol]
        return q in F

    program = open('program_AFD.txt')
    for line in program:
        a,b,c = line.split()
        ifFind = find(c, '-')
        if ifFind != -1:
            efe.add(c.rstrip('-accept'))
        d[a,b]=c.rstrip('-accept')
    program.close()   

    entry = open('input.txt')
    lines = entry.readlines()

    for i in lines:
        writeOutput = 'La entrada ' + i.rstrip('\n') + ' es '
        definition = {True:'aceptada', False:'rechazada'}
        writeOutput = writeOutput + definition[AFD(d, '0', efe, i.rstrip('\n'))]
        print(writeOutput + '\n')
    entry.close
    
def app():
    content = open('input.txt', 'r')
    sizeFile = len(content.readlines())
    if content=='':
        print("Error input file");
    if sizeFile > 2:
        finiteAutomata()
    if sizeFile <= 1:
        turingMachine()

if __name__ == '__main__':
    app()