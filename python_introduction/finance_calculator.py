monthly_income =int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
# Calculating monthly savings
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are: ${monthly_savings}.")
# Projecting annual savings
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: ${int(projected_annual_savings)}.")