def total_salary(path:str):
    try:
        with open (path, "r", encoding="utf-8") as f:
            all_data = f.read().splitlines()
        salary_numbers = []
        error_counter = 0
        for record in all_data:
            try:
                salary_numbers.append(int(record.split(",")[1]))
            except Exception as error:
                error_counter +=1
        if error_counter > 0:
            print(f'Salary records are processed with {error_counter} error(s) that are excluded from calculation. Please,check the soucre file')
        else:
            print('Salary records are processed successfully')
        total = sum(salary_numbers);
        avgerage = round(total / len(salary_numbers),2)

        return (total, avgerage)

    except FileNotFoundError:
        print(f"Can't find file for mentioned path -> {path}")
        return (0, 0)
    except Exception as error:
        print(f"Error: {error}")
        return (0, 0)

# checking time
total, average = total_salary('./source_data/salaries.txt')
print(f"Total sum of salaries is: {total}, average salary is: {average}")

qaTotal, qaAverage = total_salary('./salaries_QA.txt')
print(f"Total sum of salaries is: {qaTotal}, average salary is: {qaAverage}")

madeUpTotal, madeUpAverage = total_salary('./madeUp/salaries_QA.txt')
print(f"Total sum of salaries is: {madeUpTotal}, average salary is: {madeUpAverage}")
