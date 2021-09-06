def find_salary_threshold(salaries, target):
    n = len(salaries)
    unadjusted_salaries = 0
    adjusted_salary = 0
    for i in range(n):
        total_salary = unadjusted_salaries + salaries[i] * (n-i)
        if total_salary > target:
            adjusted_salary = (target - unadjusted_salaries) // (n - i)
            break
        unadjusted_salaries += salaries[i]
    return adjusted_salary

