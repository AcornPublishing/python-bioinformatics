""" Tests for prot.py """

import os
import platform
from subprocess import getstatusoutput, getoutput

PRG = './prot.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
TEST1 = ('./tests/inputs/input1.txt', './tests/inputs/input1.txt.out')


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Usage """

    for arg in ['', '-h', '--help']:
        out = getoutput(f'{RUN} {arg}')
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def run(rna: str, expected: str) -> None:
    """ Runs test """

    rv, out = getstatusoutput(f'{RUN} {rna}')
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_input1() -> None:
    """ Runs on command-line input """

    run('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA',
        'MAMAPRTEINSTRING')


# --------------------------------------------------
def test_stop_codon() -> None:
    """ Stops at the stop codon """

    run('AUGCCGUAAUCU', 'MP')


# --------------------------------------------------
def test_input2() -> None:
    """ Runs on file input """

    file, expected = TEST1

    def cat(filename):
        return open(filename).read().rstrip()

    run(cat(file), cat(expected))
