def fb(n):
        
        patternFizz = ["Fizz","",""]
        patternBuzz = ["Buzz","","","",""]
        result = patternFizz[ n % 3 ]
        result = result + patternBuzz[ n % 5 ]
        return result
i = 1

while i<=20:
	print i, fb(i)
	i= i + 1
