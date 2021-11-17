#MyAsm

Writing documentation was done by Zikilo_Pmd & Zhenya Kozlov

All the commands and stuff are described here

##1) Commands:
Inc X - Increment the value of this cell on the X number. if X is not specified then one is added
   
Dec X - Decrement the value of this cell on the X number. if X is not specified then one is added
   
Sac X - Select A X Cell
   
Jip X - Jump to X command(address of command in the memory) If value in selected cell Positive 

Prefixes:
   
		% : binary
		# : decimal
		& : hexadecimal

		Example:
            Inc #10 - 10
            Dec %101 - 5
            Sac %FF - 255

##2) A little bit about numbers in cell:
Max value in cell  is 255 if you write a number > 255 in the cell, then this number will be truncated example:
   
        Inc #257

   The value in the cell = 2

##Examples:
1. Writing 1 in cell 1 and 2 
   
    Code:
   
        Inc 
        Sac 
        Inc 
   
2. Infinite loop with addition of 1 to the cell

    Code:
        
        Inc #1 
        Jip #0

3. Adder

    Code:

        Dec 
        Sac 
        Inc
        Sac
        Jip #1 
