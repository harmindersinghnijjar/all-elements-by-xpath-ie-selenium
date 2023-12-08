import requests
import replicate
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.ie.options import Options
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# # Filter and print elements that have non-empty attributes
# print("Elements with non-empty attributes:")
# for elem in elems:
#     # Get attributes of the element
#     tag_name = elem.tag_name
#     elem_class = elem.get_attribute("class")
#     elem_role = elem.get_attribute("role")
#     elem_aria_label = elem.get_attribute("aria-label")
#     elem_id = elem.get_attribute("id")

#     # Check if attributes are not None or empty strings
#     if elem_class or elem_role or elem_aria_label or elem_id:
#         print(f"Tag Name: {tag_name}")
#         if elem_class:
#             print(f"Class: {elem_class}")
#         if elem_role:
#             print(f"Role: {elem_role}")
#         if elem_aria_label:
#             print(f"Aria-label: {elem_aria_label}")
#         if elem_id:
#             print(f"ID: {elem_id}")
#         print("----------")
