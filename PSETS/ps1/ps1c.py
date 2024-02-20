def main():
    #Intialize the variables
    portion_down_payment = 0.25
    annual_return = 0.04
    total_cost = 1000000
    semi_annual_raise = 0.07
    epsilon = 100
    steps = 0
    low = 0
    high = 10000
    current_savings = 0
    #Get user input
    annual_salary = float(input("Enter the starting salary: "))
    
    
    portion_saved = (low + high) // 2
    
    # down payment required
    required = total_cost * portion_down_payment
    
    while ((abs(current_savings - required) >= epsilon)):
        current_savings = 0
        rate = portion_saved / 10000
        salary = annual_salary
        
        for month in range(36):
            if month%6 == 0 and month > 0:
                salary += salary * semi_annual_raise
        
            salary_saved = rate * (salary / 12)
        
            current_savings += (current_savings * annual_return/12) + salary_saved
        
        if current_savings <= required: 
            low = portion_saved
        else:
            high = portion_saved
        
        portion_saved = (low + high) // 2
        steps += 1 
        if steps > 13:
            break
        
    if steps > 13:
        print('It is not possible to pay the down payment in three years')
        return 0
    print(f"Best savings rate: {rate}")
    print(f"Steps in bisection search: {steps}")
    
if __name__=="__main__":
    main()