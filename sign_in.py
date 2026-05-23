#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#sign_in_code
import os
import time
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

TARGET_EMAIL = os.getenv("TARGET_EMAIL", "jentaltest0633@mailinator.com")
# Static test password or can be fetched from environment
PASSWORD = "Pass@123" 

def run_signin_automation():
    with sync_playwright() as p:
        print("Launching browser for Login process...")
        
        # Launching browser (Headless=False lets you see the execution live)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Extracting username prefix from the target email for login input
        username_input = TARGET_EMAIL.split("@")[0]
        
        print(f"Attempting to login with Username: {username_input}")
        print("Navigating to login page...")
        
        try:
            # Open the target sign-in URL
            page.goto("https://www.inube.com/login", timeout=60000)
            
            print("Filling login credentials...")
            # Selectors based on standard text fields for username and password
            page.locator('input[name="username"], input[type="text"]').first.fill(username_input)
            page.locator('input[name="password"], input[type="password"]').first.fill(PASSWORD)
            
            print("Clicking login button...")
            # Locating the submit/login action button
            login_button = page.locator('input[type="submit"], button:has-text("Login"), button:has-text("Sign In")').first
            login_button.click()
            
            # Wait for background activities to settle post-login
            page.wait_for_load_state("networkidle", timeout=15000)
            print("SUCCESS: Login action completed.")
            
        except Exception as e:
            print(f"An error occurred during login process: {str(e)}")
            
        # Keeping browser open for 5 seconds to confirm visually, then closing session
        time.sleep(5)
        print("Closing browser session...")
        browser.close()

if __name__ == "__main__":
    run_signin_automation()
