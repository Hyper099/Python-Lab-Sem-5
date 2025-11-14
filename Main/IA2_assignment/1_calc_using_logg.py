import logging

LOG_FILE_PATH = './Main/IA2_assignment/calculator.log'

logging.basicConfig(level=logging.INFO, filename=LOG_FILE_PATH, format='%(asctime)s - %(levelname)s - %(message)s')

def add(a, b):
   result = a + b
   logging.info(f"Addition: {a} + {b} = {result}")
   return result

def subtract(a, b):
   result = a - b
   logging.info(f"Subtraction: {a} - {b} = {result}")
   return result

def multiply(a, b):
   result = a * b
   logging.info(f"Multiplication: {a} * {b} = {result}")
   return result

def divide(a, b):
   try:
      result = a / b
      logging.info(f"Division: {a} / {b} = {result}")
      return result
   except ZeroDivisionError:
      logging.error("Division by zero attempted")
      return None

def evaluate_expression(expression):
   logging.info(f"Evaluating expression: {expression}")
   try:
      result = eval(expression, {"__builtins__": None}, {
         "add": add,
         "subtract": subtract,
         "multiply": multiply,
         "divide": divide
      })
      logging.info(f"Result: {result}")
      return result
   except Exception as e:
      logging.error(f"Error evaluating expression: {e}")
      return None

if __name__ == "__main__":
   expr = input("Enter calculation (e.g., add(10, 5) or multiply(3, 4)): ")
   result = evaluate_expression(expr)
   if result is not None:
      print(f"Result: {result}")
   else:
      print("Error occurred. Check calculator.log for details.")