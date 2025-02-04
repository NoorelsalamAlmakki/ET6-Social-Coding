# -*- coding: utf-8 -*-
"""
Created on Tue Feb 04 15:30:30 2025

@author:
- Noorelsalam Almakki
- Amin
- Saeed Ali
- Geehan Ali
- Martha Nyekanga

Challenge 2: Digital Access Control
Objective
Use set operations to analyze and improve a company's digital access control system while identifying potential security risks in data access.
Scenario
A secure company vault stores sensitive data, where employees are granted access based on their roles:
Finance Team (F): Needs access to financial records.
Tech Team (T): Needs access to technical documents.
Some employees belong to both teams due to cross-departmental responsibilities.
Access Data (Given)
The security system tracks employee IDs (formatted as "E####").
finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}
Additionally, two special cases exist:
E0001 (Admin): Has access to all data but is not listed in specific access groups.
E9999 (New Employee): Has no assigned access yet.
Your Task
Analyze the current access structure and identify potential security risks by answering the following:
Who has access to at least one type of data?
Who has access to both financial and technical data?
Who has exclusive access to only one type of data?
Which employees currently lack access (but exist in the system)?
Are there unnecessary overlaps in access that could pose a security risk?
What changes would you recommend to enhance security and minimize excessive access?
# -*- coding: utf-8 -*-

"""
# finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
# tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}
# admin_access = {"E0001"}
# no_access = {"E9999"}

def access_control(finance_access, tech_access, admin_access, no_access):
    # All Employees
    all_employees = (finance_access | tech_access | admin_access | no_access)
    
    # Employees with access to at least one type of data
    F_or_T = finance_access | tech_access | admin_access
    
    # Employees with access to both financial and technical data
    F_and_T = finance_access & tech_access & admin_access
    
    # Employees with exclusive access to only one type of data
    either_F_or_T = F_or_T - F_and_T - admin_access
    
    # Employees who lack access
    no_access = all_employees - (F_or_T)
    
    # Unnecessary overlaps in access that could pose a security risk
    overlaps = finance_access & tech_access 
    
    return F_or_T, F_and_T, either_F_or_T, no_access, overlaps
