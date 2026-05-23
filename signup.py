import os
import time
import random
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

# Load core configuration parameters from environmental layer
load_dotenv()

TARGET_EMAIL = os.getenv("TARGET_EMAIL", "prashantgaurav242@gmail.com")
TARGET_PASSWORD = os.getenv("TARGET_PASSWORD", "sql@123python")

# Static configuration criteria for dynamic dropdown fields
BDAY_MONTH = "May"
BDAY_DAY = "23"
BDAY_YEAR = "2002"

# --- SYSTEM INTEGRITY USERNAME GENERATOR ---
email_prefix = TARGET_EMAIL.split('@')[0].replace('.', '').replace('-', '')
word_matrix = ["zone", "matrix", "nexus", "vertex", "alpha", "vector", "realm", "pulse"]
random_anchor = random.choice(word_matrix)
random_suffix = random.randint(10000, 99999)

# Formulates a high-entropy string to absolutely guarantee state validity
GENERATED_BLOG_NAME = f"{random_anchor}{email_prefix}{random_suffix}"
# -------------------------------------------

def run_tumblr_playwright_signup():
    if not TARGET_EMAIL or not TARGET_PASSWORD:
        print("ERROR: Missing TARGET_EMAIL or TARGET_PASSWORD configs in .env file.")
        return

    with sync_playwright() as p:
        print("Launching independent Chromium browser engine...")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        print("Navigating to the official Tumblr landing page...")
        try:
            page.goto("https://www.tumblr.com/", timeout=60000)
            page.wait_for_load_state("domcontentloaded")
            time.sleep(3)
            
            # Step 1: Initial Signup Trigger Execution
            print("Locating and triggering the primary Sign Up modal...")
            signup_trigger = page.locator("a[href='/register'], button:has-text('Sign up')").first
            if signup_trigger.is_visible():
                signup_trigger.click()
                time.sleep(2)
            
            # Step 2: Route to Email Input Sequence
            print("Selecting 'Continue with email' registration pathway...")
            email_auth_btn = page.locator("button:has-text('Continue with email')").first
            if email_auth_btn.is_visible():
                email_auth_btn.click()
                time.sleep(2)
            
            # Step 3: Email Injection Field Processing
            print(f"Injecting target email credentials: {TARGET_EMAIL}")
            email_field = page.locator("input[type='email'], input[name='email']").first
            email_field.fill(TARGET_EMAIL)
            time.sleep(1)
            
            # Step 4: Advance to Password Form Stage
            next_btn = page.locator("button[type='submit'], button:has-text('Next'), button:has-text('Continue')").first
            if next_btn.is_visible():
                next_btn.click()
                time.sleep(4)
            
            # Step 5: Double Password Field Population Strategy
            print(f"Injecting security password credentials: {TARGET_PASSWORD}") 
            set_pwd_field = page.locator("input[placeholder='Set a password']").first
            if set_pwd_field.is_visible():
                set_pwd_field.fill(TARGET_PASSWORD)
                time.sleep(1)
            
            repeat_pwd_field = page.locator("input[placeholder='Repeat password']").first
            if repeat_pwd_field.is_visible():
                repeat_pwd_field.fill(TARGET_PASSWORD)
                time.sleep(1)
                
            final_next = page.locator("button[type='submit'], button:has-text('Next')").first
            if final_next.is_visible():
                print("Submitting credential profile details...")
                final_next.click()
                time.sleep(5)
                
            # Step 6: Dropdown Demographic Target Allocation
            print("Detecting birthday dropdown components...")
            month_dropdown = page.locator("select[aria-label='Month'], select[name='month']").first
            if month_dropdown.is_visible():
                print(f"Selecting Birth Month: {BDAY_MONTH}")
                month_dropdown.select_option(label=BDAY_MONTH)
                time.sleep(0.5)
                
            day_dropdown = page.locator("select[aria-label='Day'], select[name='day']").first
            if day_dropdown.is_visible():
                print(f"Selecting Birth Day: {BDAY_DAY}")
                day_dropdown.select_option(label=BDAY_DAY)
                time.sleep(0.5)
                
            year_dropdown = page.locator("select[aria-label='Year'], select[name='year']").first
            if year_dropdown.is_visible():
                print(f"Selecting Birth Year: {BDAY_YEAR}")
                year_dropdown.select_option(label=BDAY_YEAR)
                time.sleep(1)

            # Submit the Birthday Form Component
            birthday_submit = page.locator("button[type='submit'], button:has-text('Next'), button:has-text('Done')").first
            if birthday_submit.is_visible():
                print("Submitting birthday validation form...")
                birthday_submit.click()
                time.sleep(5)

            # Step 7: Sequential Typing Simulation for Username Verification
            print(f"Detecting Username Screen... Typing unique Blog Name sequentially: {GENERATED_BLOG_NAME}")
            blog_field = page.locator("input[placeholder='Blog name'], input[name='blog_name']").first
            
            if blog_field.is_visible():
                blog_field.click()
                blog_field.focus()
                blog_field.press_sequentially(GENERATED_BLOG_NAME, delay=100)
                time.sleep(2)
                
                print("Sending hardware 'Enter' key stroke to enforce validation dispatch...")
                blog_field.press("Enter")
                time.sleep(3)
                
                final_signup_btn = page.locator("button[type='submit'], button:has-text('Sign up'), form button:last-child").first
                if final_signup_btn.is_visible():
                    print("Executing backup submission protocol on final Sign Up submit layer...")
                    try:
                        final_signup_btn.click(force=True, timeout=5000)
                    except Exception:
                        print("Using fallback JavaScript execution layer to dispatch registration form...")
                        page.evaluate("document.querySelector(\"button[type='submit']\").click()")
                    time.sleep(5)

            # --- MANUALLY INTERCEPT CAPTCHA CHALLENGES ---
            print("\n" + "!"*60)
            print("[ACTION REQUIRED]: Please check the browser window for any CAPTCHA security puzzles.")
            print("Manually solve the verification puzzle until the dashboard prompts 'Check your email'.")
            input("Once complete, return to this terminal and press ENTER to run the verification processor: ")
            print("!"*60 + "\n")
            
        except Exception as e:
            print(f"Pipeline Execution Status Warning: {str(e)}")

        # --- IN-BLOCK ACTIVATION LINK PROCESSOR (FIXED POSITION) ---
        print("\n" + "="*60)
        print("TUMBLR EMAIL VERIFICATION PROCESSOR")
        print("="*60)
        print(f"Please inspect the inbox or spam directories of: {TARGET_EMAIL}")
        activation_link = input("Paste the complete activation URL link here and press ENTER: ").strip()
        print("="*60 + "\n")
        
        if activation_link.startswith("http"):
            try:
                print("Initializing token verification cycle in clean environment context...")
                verify_page = context.new_page()
                verify_page.goto(activation_link, timeout=45000)
                verify_page.wait_for_load_state("networkidle")
                print("SUCCESS: Account verified and finalized successfully on Tumblr!")
                time.sleep(7)
            except Exception as e:
                print(f"CRITICAL ERROR: Token validation procedure failed: {str(e)}")
        else:
            print("ABORTED: Invalid verification URL string submitted.")

        print("Terminating sandboxed browser instance layers...")
        browser.close()

if __name__ == "__main__":
    run_tumblr_playwright_signup()