from parser_noL import Parser, InstructionType
from code_noL import Code
import os
import sys


def assembleNoL(filename):
    parse = Parser(filename)
    code = Code()

    print(f'{filename} has {len(parse.lines)} code lines.\n')

    outlines = []

    while parse.hasMoreLines():

        # Move to the next instruction
        parse.advance()

        # Determine the instruction type
        instruction_type = parse.instructionType()

        # Translate A-instructions
        if instruction_type == InstructionType.A_INSTRUCTION:

            value = int(parse.symbol())

            binary = format(value, '016b')

            outlines.append(binary)

        # Translate C-instructions
        elif instruction_type == InstructionType.C_INSTRUCTION:

            comp_bits = code.comp(parse.comp())
            dest_bits = code.dest(parse.dest())
            jump_bits = code.jump(parse.jump())

            binary = '111' + comp_bits + dest_bits + jump_bits

            outlines.append(binary)

        # Labels require symbol handling (added later)
        elif instruction_type == InstructionType.L_INSTRUCTION:
            raise ValueError(
                "Label encountered. Use the full assembler "
                "when symbol handling is implemented."
            )

    # Create output filename
    basename, ext = os.path.splitext(filename)
    outfilename = basename + '.hack'

    # Write binary instructions to output file
    with open(outfilename, 'w') as outfile:
        for line in outlines:
            outfile.write(line + '\n')

    print(f'Wrote {len(outlines)} lines to {outfilename}.\n')


if __name__ == '__main__':
    assembleNoL(sys.argv[1])
