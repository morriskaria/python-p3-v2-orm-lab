#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from department import Department
from employee import Employee
from review import Review

import ipdb

def reset_database():
    Department.drop_table()
    Employee.drop_table()
    Review.drop_table()
    
    Department.create_table()
    Employee.create_table()
    Review.create_table()

    # Create seed data
    engineering = Department.create("Engineering", "Building A")
    hr = Department.create("Human Resources", "Building B")
    
    alice = Employee.create("Alice", "Software Engineer", engineering.id)
    bob = Employee.create("Bob", "HR Manager", hr.id)
    
    Review.create(2023, "Excellent performance", alice.id)
    Review.create(2022, "Good progress", alice.id)
    Review.create(2023, "Outstanding leadership", bob.id)

if __name__ == '__main__':
    reset_database()
    ipdb.set_trace()