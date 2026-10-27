class Code(object):

    def __init__(self):
        self.destmap = {}
        self.compmap = {}
        self.jumpmap = {}
        self.symbmap = {}
        self.makeMaps()

    def dest(self, s):
        assert s in self.destmap, f'Error: no dest bits for {s}'
        return self.destmap[s]

    def comp(self, s):
        assert s in self.compmap, f'Error: no comp bits for {s}'
        return self.compmap[s]

    def jump(self, s):
        assert s in self.jumpmap, f'Error: no jump bits for {s}'
        return self.jumpmap[s]

    def makeMaps(self):

        # Destination bits
        self.destmap.update({
            None: '000',
            '000': '000',
            'M': '001',
            'D': '010',
            'MD': '011',
            'DM': '011',
            'A': '100',
            'AM': '101',
            'AD': '110',
            'AMD': '111',
            'ADM': '111'
        })

        # Jump bits
        self.jumpmap.update({
            None: '000',
            '000': '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111'
        })

        # Computation bits (a = 0)
        self.compmap.update({
            '0':   '0101010',
            '1':   '0111111',
            '-1':  '0111010',
            'D':   '0001100',
            'A':   '0110000',
            '!D':  '0001101',
            '!A':  '0110001',
            '-D':  '0001111',
            '-A':  '0110011',
            'D+1': '0011111',
            'A+1': '0110111',
            'D-1': '0001110',
            'A-1': '0110010',
            'D+A': '0000010',
            'D-A': '0010011',
            'A-D': '0000111',
            'D&A': '0000000',
            'D|A': '0010101'
        })

        # Automatically generate M versions (a = 1)
        keys = list(self.compmap.keys())

        for key in keys:
            if 'A' in key:
                self.compmap[key.replace('A', 'M')] = \
                    '1' + self.compmap[key][1:]
