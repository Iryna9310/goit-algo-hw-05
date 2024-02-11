def caching_fibonacci(n):
  cache = {}  #створення пустого словнику
  def fibonacci(n):  
    if n <= 0:   #перевірка умов
      return 0
    elif n == 1:
      return 1
    elif n in cache:
      return cache[n]
    else:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)  #формула для розрахунку
        return cache[n]
  return fibonacci(n)  #повернення внутрішньої фінкції

fib = caching_fibonacci
print(fib(10))