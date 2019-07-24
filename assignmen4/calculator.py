
print('*********Calculator********')
x = int(input('input num1 : '))
y = int(input('input num2 : '))
mark = input('input Operator is [ + - * / ] : ')

class Calculator:  

  def __init__(self, x, y ,mark):
    self.x = x
    self.y = y
    self.mark = mark


  def process(self):
    print(x,mark,y)
    if mark=='+' :
      result = self.x + self.y
      print('result plus : ', result)
    elif mark=='-' :
      result = self.x - self.y
      print('result minus : ', result)
    elif mark=='*' :
      result = self.x * self.y
      print('result multiply : ', result)
    elif mark=='/' :
      if y==0:
        print("Error")
      else:
        result = self.x / self.y
        print('result divide : ', result)
    else :
      print('Error !!')
 

test = Calculator(x,y,mark)

print('--------RESULT-------')
test.process()
print('---------End---------')
