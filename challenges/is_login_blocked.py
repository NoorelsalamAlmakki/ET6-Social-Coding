# -*- coding: utf-8 -*-
"""
Created on Tue Feb 04 15:30:30 2025

@author:
- Noorelsalam Almakki
- Amin
- Saeed Ali
- Geehan Ali
- Martha Nyekanga
"""
"""
Challenge 1: Detecting Suspicious Login Attempts
Objective:
The goal of this challenge is to practice Boolean algebra simplification. Students will write a Python program to simplify a
given Boolean expressions using Boolean Algebra’s law, helping them understand how to optimize logical expressions in 
programming.
Scenario:
A cybersecurity team is investigating an authentication system that occasionally flags legitimate login attempts as 
suspicious. The system checks multiple conditions to determine if a login attempt should be blocked.
One of the core checks involves the following rule:
¬(A∧(B∨¬B))
where:
A: The user has provided the correct login credentials.
B: The login attempt is from a trusted device.
The security team suspects that the system might be blocking users incorrectly due to redundant logic checks. Your task is
to simplify the logic to understand what the system is actually doing and determine if the rule is valid or needs 
modification.

Task:
Analyze the given Boolean expression.
Apply Boolean law to simplify it.
Interpret what the final expression means in the context of allowing or blocking a login attempt.

"""



def is_login_blocked(A, B):
    '''
    A: The user has provided the correct login credentials (True/False)
    B: The login attempt is from a trusted device (True/False).
    
    Returns
    True if the login attempt is blocked, False otherwise.
    '''
    original_expression = not (A and (B or not B)) 
    # (B or not B) -> 1, complement law
    # A and 1 -> A, identity law
    simplified_expression = not A 
    
    # The function as it is will block the login attempt if the user has provided an invalid login credentials. However, the "trusted device" criterion is not taken into account. 
    if simplified_expression:
        print("The login attempt is blocked.")   
    else:
        print("The login attempt is not blocked")
    return simplified_expression
