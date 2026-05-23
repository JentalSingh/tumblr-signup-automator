# Tumblr Signup Automator 

An enterprise-grade browser automation pipeline designed using Python and Playwright to completely automate the multi-step registration process on Tumblr. This script simulates human-like interactions to bypass complex layout changes, handles dynamic demographic selections, and generates high-entropy unique identifiers to guarantee clean execution.

---

## Key Features

* **Automated Demographic Selection:** Seamlessly handles and selects parameters from birth date dropdown menus (Month, Day, and Year) without UI layout breaks.
* **High-Entropy Username Generator:** Programmatically blends structural tech prefixes with email contexts and a 5-digit random anchor to entirely bypass "Invalid Username" or "Username Already Taken" system blocks.
* **Keystroke Interaction Simulation:** Utilizes advanced sequential typing layers (`press_sequentially`) mimicking actual hardware responses to bypass application-side validation overlays.
* **In-Lifecycle Token Verification:** Natively processes the in-terminal user input for official account verification URLs directly inside the active browser execution block to prevent premature session termination.

---

## Project Structure

```text
auto_2/
│
├── .env                  # Local environmental configuration layer
├── signup.py             # Core Playwright automation script engine
└── README.md             # Project documentation and architectural overview
