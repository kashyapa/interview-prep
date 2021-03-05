def find_salary_cap(target_payroll, current_salaries):
    current_salaries.sort()
    n = len(current_salaries)
    unadjusted_salary = 0

    for i, salary in enumerate(current_salaries):
        adjusted_salaries = salary * (n - i)
        total_salary = adjusted_salaries + unadjusted_salary
        if total_salary >= target_payroll:
            return (target_payroll - unadjusted_salary)// (n-i)
        unadjusted_salary += salary
    return -1.0
