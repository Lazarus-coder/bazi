#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Test script for bazi.py

import os
import subprocess

def test_bazi_module():
    """Test the bazi.py module with a sample birth date and time."""
    print("Testing bazi.py module...")
    
    # Test with public calendar (公历)
    cmd_public = ["python", "bazi.py", "-g", "1990", "8", "23", "12"]
    print(f"Running command: {' '.join(cmd_public)}")
    
    result = subprocess.run(cmd_public, capture_output=True, text=True)
    
    # Print first 20 lines of output
    lines = result.stdout.split('\n')
    print("\nOutput (first 20 lines):")
    for i, line in enumerate(lines[:20]):
        print(line)
    
    print("\n...")
    
    # Check if the program ran successfully
    if result.returncode == 0:
        print("\nTest passed: bazi.py ran successfully with public calendar.")
    else:
        print("\nTest failed: bazi.py returned an error.")
        print(f"Error: {result.stderr}")
    
    # Test with lunar calendar (农历)
    cmd_lunar = ["python", "bazi.py", "1990", "7", "3", "12"]
    print(f"\nRunning command: {' '.join(cmd_lunar)}")
    
    result = subprocess.run(cmd_lunar, capture_output=True, text=True)
    
    # Print first 10 lines of output
    lines = result.stdout.split('\n')
    print("\nOutput (first 10 lines):")
    for i, line in enumerate(lines[:10]):
        print(line)
    
    print("\n...")
    
    # Check if the program ran successfully
    if result.returncode == 0:
        print("\nTest passed: bazi.py ran successfully with lunar calendar.")
    else:
        print("\nTest failed: bazi.py returned an error.")
        print(f"Error: {result.stderr}")

if __name__ == "__main__":
    test_bazi_module() 