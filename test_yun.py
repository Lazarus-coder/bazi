#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lunar_python import Lunar, Solar

# Create a test birth date
solar = Solar.fromYmdHms(2001, 6, 16, 11, 0, 0)
lunar = solar.getLunar()
ba = lunar.getEightChar()

# Get the Yun object
yun = ba.getYun(True)  # True for male

# Print all attributes and methods
print("Yun object attributes and methods:")
print(dir(yun))

# Try to access common properties
print("\nTrying common properties:")
try:
    print(f"Start year: {yun.getStartYear()}")
except:
    print("No getStartYear method")

try:
    print(f"Start age: {yun.getStartAge()}")
except:
    print("No getStartAge method")

try:
    print(f"Start date: {yun.getStartSolar().toFullString()}")
except:
    print("No getStartSolar method")

try:
    print(f"Start year: {yun.getStartYear}")
except:
    print("No startYear property")
    
# Print all available methods with type hints if possible
print("\nDetailed information about the Yun object:")
print(f"Type: {type(yun)}")
print(f"String representation: {str(yun)}")
print(f"Dict representation: {yun.__dict__ if hasattr(yun, '__dict__') else 'No __dict__ attribute'}") 