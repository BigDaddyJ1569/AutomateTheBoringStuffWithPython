import sqlite3
from Employee import Employee
conn = sqlite3.connect('employee.db')

c = conn.cursor()

#c.execute("""CREATE TABLE employees (
#            First text,
#            last text,
#            pay integer
#         )""")

emp_1 = Employee('George', 'Feorge', 69000)
emp_2 = Employee('Mark', 'Stark', 80500)

print(emp_1.first)
print(emp_2.last)
print(emp_1.pay)

print
#c.execute("INSERT INTO employees VALUES ('David', 'Smith', 75000)")
conn.commit()

#c.execute("SELECT * FROM employees WHERE last='Smith'")
print(c.fetchall())

conn.commit()

conn.close()