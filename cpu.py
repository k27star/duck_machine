"""
Duck Machine model DM2018S CPU
"""

from instr_format import Instruction, OpCode, CondFlag, decode
from register import Register, ZeroRegister
from alu import ALU
from mvc import MVCEvent, MVCListenable

import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class CPUStep(MVCEvent):
    """CPU is beginning step with PC at a given address"""

    def __init__(self, subject: "CPU", pc_addr: int,
                 instr_word: int, instr: Instruction) -> None:
        self.subject = subject
        self.pc_addr = pc_addr
        self.instr_word = instr_word
        self.instr = instr

# Create a class CPU, subclassing MVCListenable.
# It should have 16 registers (a list of Register objects),
# and the first of them should be the special ZeroRegister
# object that is always zero regardless of what is stored.
# It should have a CondFlag with the current condition.
# It should have a boolean "Halted" flag, and execution of
# the "run" method should halt with the Halted flag is True
# (set by the HALT instruction). The CPU does not contain
# the memory, but has a connection to a Memory object
# (specifically a MemoryMappedIO object).
# See the project web page for more guidance.

