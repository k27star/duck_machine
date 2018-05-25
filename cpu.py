"""
Duck Machine model DM2018S CPU
By: Kristine Stecker
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


class CPU(MVCListenable):
    '''
    Contains 16 registers (register 0 will always be of type
    ZeroRegister), an ALU object, an interface to memory,
    and sequential logic for executing programs that may
    have loops and conditional branches.
    '''

    def __init__(self, memory):
        super().__init__()

        self.memory = memory
        self.registers = [ZeroRegister(), Register(), Register(), Register(), Register(),
                          Register(), Register(), Register(), Register(), Register(),
                          Register(), Register(), Register(), Register(), Register(), Register()]
        self.cond_flag = CondFlag.ALWAYS
        self.halted = False
        self.program_pointer = self.registers[15]
        self.alu = ALU()

    def step(self) -> None:
        '''Fetches instructions in memory. Decodes instruction word. Determines if
        instruction should be executed or skipped. Executes if applicable.
        '''
        #fetch
        address = self.program_pointer.get()
        instruction_word = self.memory.get(address)

        #decode
        decoded_word = decode(instruction_word)

        self.notify_all(CPUStep(self, address, instruction_word, decoded_word))

        #execute
        predicate = self.cond_flag & decoded_word.cond

        if predicate:
            # get values for source registers
            val1 = self.registers[decoded_word.reg_src1].get()
            val2 = self.registers[decoded_word.reg_src2].get()

            # add offset to register
            val2 =  val2 + decoded_word.offset

            #increment program counter
            self.program_pointer.put(self.program_pointer.get() + 1)

            #sending op code to ALU to execute with 2 values
            result, self.cond_flag = self.alu.exec(decoded_word.op, val1, val2)

            if decoded_word.op == OpCode.HALT:
                self.halted = True

            #load
            elif decoded_word.op == OpCode.LOAD:
                self.registers[decoded_word.reg_target].put(self.memory.get(result))

            #store
            elif decoded_word.op == OpCode.STORE:
                self.memory.put(result, self.registers[decoded_word.reg_target].get())

            else:
                self.registers[decoded_word.reg_target].put(result)
        else:
            self.program_pointer.put(self.program_pointer.get() + 1)

    def run(self, from_addr=0, single_step=False) -> None:
        ''' Calls step method until it executes the HALT instruction.
        Allows the option of a single-step mode for debugging.
        '''
        self.program_pointer.put(from_addr)

        step_count = 0

        while not self.halted:
            if single_step:
                input("Step {}; press enter".format(step_count))
            self.step()
            step_count += 1

