from enum import Enum


class InstructionType(Enum):
    A_INSTRUCTION = 1
    C_INSTRUCTION = 2
    L_INSTRUCTION = 3
    NO_TYPE = 4


class Parser(object):

    def __init__(self, input_file):
        self.lines = []
        self.cur = -1
        self.inputfile = input_file
        self.preprocessFile()

        self.curtype = InstructionType.NO_TYPE
        self.curdest = None
        self.cursymbol = None
        self.curcomp = None
        self.curjump = None

    def hasMoreLines(self):
        # Check whether another instruction exists
        return self.cur + 1 < len(self.lines)

    def advance(self):
        # Move to the next instruction
        if self.hasMoreLines():
            self.cur += 1
            self.interpretLine()

    def instructionType(self):
        return self.curtype

    def curLine(self):
        assert 0 <= self.cur < len(self.lines), \
            'No current line to report'
        return str(self.lines[self.cur])

    def symbol(self):
        # Return the symbol/value of A or L instruction
        assert self.curtype is InstructionType.A_INSTRUCTION or \
            self.curtype is InstructionType.L_INSTRUCTION, \
            f'symbol only for A or L type, not {self.lines[self.cur]}'

        return self.cursymbol

    def dest(self):
        # Return the destination of a C-instruction
        assert self.curtype is InstructionType.C_INSTRUCTION, \
            f'dest only for C-type, not {self.lines[self.cur]}'

        return self.curdest

    def comp(self):
        # Return the computation of a C-instruction
        assert self.curtype is InstructionType.C_INSTRUCTION, \
            f'comp only for C-type, not {self.lines[self.cur]}'

        return self.curcomp

    def jump(self):
        # Return the jump of a C-instruction
        assert self.curtype is InstructionType.C_INSTRUCTION, \
            f'jump only for C-type, not {self.lines[self.cur]}'

        return self.curjump

    def preprocessFile(self):
        # Remove comments, whitespace, and empty lines
        try:
            with open(self.inputfile, 'r') as file:
                all_lines = file.read().split('\n')
        except FileNotFoundError:
            print(f'Read Error: could not read {self.inputfile}.')
            raise
        except Exception as e:
            print(f'Unexpected Error: {e}')
            raise

        for line in all_lines:
            # Remove comments
            line = line.split("//")[0]

            # Remove whitespace
            line = "".join(line.split())

            # Save nonempty lines
            if line:
                self.lines.append(line)

    def interpretLine(self):
        # Interpret the current instruction
        line = str(self.lines[self.cur])

        # Reset previous instruction information
        self.cursymbol = None
        self.curdest = None
        self.curcomp = None
        self.curjump = None

        if line[0] == '@':
            # A-instruction
            self.curtype = InstructionType.A_INSTRUCTION
            self.cursymbol = line[1:]

        elif line[0] == '(':
            # L-instruction
            self.curtype = InstructionType.L_INSTRUCTION
            self.cursymbol = line[1:-1]

        else:
            # C-instruction
            self.curtype = InstructionType.C_INSTRUCTION

            # Separate destination if present
            if '=' in line:
                self.curdest, line = line.split('=', 1)

            # Separate computation and jump
            if ';' in line:
                self.curcomp, self.curjump = line.split(';', 1)
            else:
                self.curcomp = line
