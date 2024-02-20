def main():
    #Intialize the variables
    portion_down_payment = 0.25
    current_savings = 0.0
    annual_return = 0.04
    
    #Get user input
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    

    required = total_cost * portion_down_payment
    portion_saved = portion_saved * (annual_salary/12)
    
    months = 0
    while (current_savings <= required):
        current_savings += (current_savings* annual_return/12) + portion_saved
        months += 1
    print(months)
    

if __name__=="__main__":
    main()