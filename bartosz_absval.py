# This file contributes to the implementation of the Bartosz Virtual Machine
# https://www.bartoszsypytkowski.com/simple-virtual-machine/

from homework.bartosz_vm import emulate

absval = ['LABEL', 'ffi',
          'CALL', 'abs', 1,
          'HALT',
          'LABEL', 'abs',
          # Student must complete this code so that when the function LABEL abs
          # is called with one argument (LDARG 0), then it returns with the
          # absolute value of the arg on the stack.
          # Note, we cannot represent 2**31 in signed 32-bit integers,
          # so it doesn't matter what you do in this case, as the
          # test case will never call abs(-2*31).
          # CHALLENGE: student must complete the implementation.
          # HINT: goal <= 18 lines
          'LDARG', 0,
          'CONST_I32', 0,
          'LT_I32',  # negative check
          'JMPF', 'x >= 0',  # value is actually greater than 0
          'LDARG', 0,
          'CONST_I32', -1,
          'MUL_I32',
          'RET',

          'LABEL', 'x >= 0',
          'LDARG', 0,
          'RET'
          ]

if __name__ == '__main__':
    from bartosz_vm import VM

    vm = VM(absval, trace=False, single_step=False)
    print(vm(0))
