import os
from time import sleep

class ASMSimple:
	
	commands = {'inc' : 1, 'dec' : 2, 'sac' : 4, 'jip' : 8}
	base = { '%' : 2, '#' : 10, '&' : 16}
	
	program_mem = [0 for _ in range(30000)]
	program_counter = 0
	mem = [0 for _ in range(30000)]
	i = 0
	
	def print_mem(self, quantity=10):
		os.system("cls||clear")
		print('\n'*5)
		print("-"*5)
		for j, cell in enumerate(self.mem[0:quantity]):
			if self.i == j:
				print('', cell, '<\n'+"-"*5)
			else:
				print('', cell, '\n'+"-"*5)
		
	
	def parse(self, code: str):
		command_list = []
		for command in code.split("\n"):
			command = [
			i for i in command.split(';')[0].replace('\t', '').split(' ') if i != ''
			]
			if len(command) != 0:
				if len(command) == 1:
					if self.commands[command[0]] <= 2:
						command.append('%1')
					else:
						command.append('%0')
				command_list.append(command)
			
		return command_list
			
	def record_program(self, code: str):
		program = self.parse(code)
		cell = 0
		for line, command in enumerate(program, start=1):
			try:
				self.program_mem[cell] = self.commands[command[0].lower()]
				cell += 1
			except KeyError:
				raise SyntaxError(f'the "{command[0]}" command in line {line} has not been identified')
				
			try:
				self.program_mem[cell] = int(command[1][1:], self.base[command[1][0]])
				cell += 1
			except KeyError:
				raise SyntaxError(f'failed to identify the prefix of the number "{command[1]}" in line {line}')
			except ValueError:
				raise SyntaxError(f'could not read the number "{command[1][1:]}" in line {line}')
				
	
	def execute(self, code: str, delay):
		self.record_program(code)
		
		def inc(num):
			if self.mem[self.i] + num > 255:
				self.mem[self.i] = self.mem[self.i] + num - 255
			else:
				self.mem[self.i] += num
			
		def dec(num):
			if self.mem[self.i] - num < 0:
				self.mem[self.i] = 256 + self.mem[self.i] - num
			else:
				self.mem[self.i] -= num
			
		def sac(num):
			self.i = num
				
		def jip(num):
			if self.mem[self.i]:
				self.program_counter = num*2 - 2
		
		command_fn = {
			1 : inc,
			2 : dec,
			4 : sac,
			8 : jip 
		}
		
		self.print_mem()
		print("PC =", self.program_counter)
			
		sleep(delay)
		
		while self.program_mem[self.program_counter] != 0:
			command_fn[self.program_mem[self.program_counter]]( self.program_mem[self.program_counter + 1])
			self.program_counter += 2
			
			self.print_mem()
			print("PC =", self.program_counter)
			
			sleep(delay)
		#	print(self.program_mem[0:12])
		#	input()

import sys

if __name__ == "__main__":
	if len(sys.argv) == 1:
		with open("code.asm", "r") as code:
			ASMSimple().execute(code.read(), 0)
	else:
		args = sys.argv[1:]
		delay = 0.7
		if len(args) > 1:
			delay = float(args[1])
		with open(args[0], "r") as code:
			ASMSimple().execute(code.read(), delay)

	input()
