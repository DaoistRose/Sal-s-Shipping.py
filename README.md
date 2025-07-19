# Sal-s-Shipping.py

# Sal’s Shipping Struggles   
### Expanding the User Experience — My Beginner's Journey

This is a beginner Python project built during my Codecademy Python course. The prompt was simple:  
> Ask the user for the weight of a package and determine the cheapest way to ship it using a set of pricing rules.

The concept started small—but as with every project so far, I saw an opportunity to make the experience more interactive, user-friendly, and polished.

---

## About the Project

Sal’s Shippers is the largest logistics company in the tri-county area. They offer three shipping options:

- **Ground Shipping**: Tiered cost per pound + $20 flat fee  
- **Premium Ground Shipping**: Flat fee of $125  
- **Drone Shipping**: Tiered cost per pound, no flat fee (but more expensive per pound)

My Python script:
- Prompts the user for package weight
- Calculates costs for each shipping method
- Returns the cheapest option
- Allows repeat entries for multiple packages
- Formats output in dollars and cents

---

## What I Learned

- How to validate user input using `try/except` and loops  
- The importance of formatting output with `.format("{:.2f}")` to properly show cents  
- How to use `while` loops to create reusable flows  
- The value of clear print statements and UX touches like `time.sleep()` for pacing

---

## Features

- Input validation (only positive numbers accepted)
- Handles multiple package entries in one session
- Friendly and informative output
- Prices always shown with two decimal places
- Interactive user prompts and graceful error handling

---

## What I’d Add Next

When I learn more Python, here are some features I’d love to implement:
- Let users **name their packages** and see a summary of all shipments
- Display **all shipping prices**, not just the cheapest one
- Refactor repetitive blocks into **functions** for cleaner, modular code

---
