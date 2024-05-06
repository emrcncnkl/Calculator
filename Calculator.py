print('''
                         ___                                                ___                     
                        (   )                                              (   )                    
 ___  ___  ___   .--.    | |    .--.      .--.    ___ .-. .-.     .--.      | |_       .--.         
(   )(   )(   ) /    \   | |   /    \    /    \  (   )   '   \   /    \    (   __)    /    \        
 | |  | |  | | |  .-. ;  | |  |  .-. ;  |  .-. ;  |  .-.  .-. ; |  .-. ;    | |      |  .-. ;       
 | |  | |  | | |  | | |  | |  |  |(___) | |  | |  | |  | |  | | |  | | |    | | ___  | |  | |       
 | |  | |  | | |  |/  |  | |  |  |      | |  | |  | |  | |  | | |  |/  |    | |(   ) | |  | |       
 | |  | |  | | |  ' _.'  | |  |  | ___  | |  | |  | |  | |  | | |  ' _.'    | | | |  | |  | |       
 | |  ; '  | | |  .'.-.  | |  |  '(   ) | '  | |  | |  | |  | | |  .'.-.    | ' | |  | '  | |       
 ' `-'   `-' ' '  `-' /  | |  '  `-' |  '  `-' /  | |  | |  | | '  `-' /    ' `-' ;  '  `-' /       
  '.__.'.__.'   `.__.'  (___)  `.__,'    `.__.'  (___)(___)(___) `.__.'      `.__.    `.__.'        
                                                                                                    
                                                                                                    
                            ___                        ___            ___                           
                           (   )                      (   )          (   )                          
          .--.      .---.   | |    .--.     ___  ___   | |    .---.   | |_       .--.    ___ .-.    
         /    \    / .-, \  | |   /    \   (   )(   )  | |   / .-, \ (   __)    /    \  (   )   \   
        |  .-. ;  (__) ; |  | |  |  .-. ;   | |  | |   | |  (__) ; |  | |      |  .-. ;  | ' .-. ;  
        |  |(___)   .'`  |  | |  |  |(___)  | |  | |   | |    .'`  |  | | ___  | |  | |  |  / (___) 
        |  |       / .'| |  | |  |  |       | |  | |   | |   / .'| |  | |(   ) | |  | |  | |        
        |  | ___  | /  | |  | |  |  | ___   | |  | |   | |  | /  | |  | | | |  | |  | |  | |        
        |  '(   ) ; |  ; |  | |  |  '(   )  | |  ; '   | |  ; |  ; |  | ' | |  | '  | |  | |        
        '  `-' |  ' `-'  |  | |  '  `-' |   ' `-'  /   | |  ' `-'  |  ' `-' ;  '  `-' /  | |        
         `.__,'   `.__.'_. (___)  `.__,'     '.__.'   (___) `.__.'_.   `.__.    `.__.'  (___)       
                                                                                                    
                                                                                                    
''')


def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

continue_calculation = "y"

while continue_calculation == "y":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation you want to perform (+, -, *, /): ")

    if operation == '+':
        result = addition(num1, num2)
    elif operation == '-':
        result = subtraction(num1, num2)
    elif operation == '*':
        result = multiplication(num1, num2)
    elif operation == '/':
        result = division(num1, num2)

    print("Result: ", result)

    continue_calculation = input("Do you want to perform another calculation? (y/n): ")
    continue_calculation = continue_calculation.lower()
