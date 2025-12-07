#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from department import Department
import ipdb

# Reset table
Department.drop_table()
Department.create_table()

# Create departments
payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)

hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)

# Update HR department
hr.name = "HR"
hr.location = "Building F, 10th Floor"
hr.update()
print(hr)

# Delete payroll
print("Deleting Payroll...")
payroll.delete()
print(payroll)

ipdb.set_trace()
