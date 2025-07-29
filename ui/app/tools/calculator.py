def get_calculator_tool():
   return {
       "name": "Calculator",
       "func": lambda x: str(eval(x)),
       "description": "Performs basic arithmetic operations from natural language input."
   }