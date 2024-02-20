def main():
    #Intialize the variables
    portion_down_payment = 0.25
    current_savings = 0.0
    annual_return = 0.04
    
    #Get user input
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
    

    required = total_cost * portion_down_payment
    salary_saved = portion_saved * (annual_salary/12)
    
    months = 0
    while (current_savings <= required):
        if months%6 == 0 and months > 0:
            annual_salary += annual_salary * semi_annual_raise
            salary_saved = portion_saved * (annual_salary/12)
            
        current_savings += (current_savings* annual_return/12) + salary_saved
        months += 1
    print(months)
    

if __name__=="__main__":
    main()