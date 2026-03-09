# calculator.py
def add(a, b):
    return a + b

print(__name__)

if __name__=="__main__":
    print("The result is:", add(3, 5))   # runs when imported too — unwanted!