import re
from typing import Callable

def generator_numbers(text: str): 
  pattern =r"( [\d]+[.,\d]+ )"
  numbers=re.findall(pattern, text) # регулярний вираз для ідентифікації дійсних чисел у тексті
  for i in numbers:   #створення генератора
    yield float(i)  

def sum_profit(text: str, func: Callable):
  sum=0
  for i in generator_numbers(text): 
    sum +=i
  return sum  #загальна сума

text = "5.5 Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
generator_numbers(text)
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")