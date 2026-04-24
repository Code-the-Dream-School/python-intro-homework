# python-intro-homework

This is your homework repository for the Python Intro course. Each week you'll add your assignment here alongside starter data files provided by the course.

## Repository Structure

```
python-intro-homework/
  week-1/
    data/               ← starter files provided for you
  week-2/
    data/
  ...
  week-7/
    data/
      expenses.csv
      notes.txt
      students.csv
    assignment-7/       ← your work goes here
      warmup1.py
      warmup2.py
      ...
```

Each week's `data/` folder contains any files your assignments need — CSVs, text files, and other resources. **Do not edit files in `data/`.** Your work lives in your `assignment-[#]` folder. Blank folders have a `.gitkeep` — don't worry about deleting this, it's just a placeholder.

## Your Workflow Each Week

1. Pull the latest from `main` so you have the week's data files:
   ```bash
   git checkout main
   git pull origin main
   ```
2. Create a new branch for the week's assignment:
   ```bash
   git checkout -b assignment-[#]
   ```
3. Create your working folder inside the week's folder:
   ```bash
   mkdir week-[#]/assignment-[#]
   cd week-[#]/assignment-[#]
   ```
4. Write your code there. Reference data files using a relative path — for example:
   ```python
   with open("../data/expenses.csv", "r") as file:
       ...
   ```
   The `..` moves up one level from your `assignment-[#]` folder to the `week-[#]` folder, then into `data/`. Each week's assignment instructions will show you the exact paths to use.

5. Commit and push your branch, then open a pull request from `assignment-[#]` into `main`. Submit the PR link (not the repo link) in the LMS.

## What to Submit

Your pull request should contain only your `.py` files and any output files your programs generate (like `food_report.txt`). It should not include changes to files in `data/`.

The PR URL should look like `github.com/your-username/python-intro-homework/pull/[number]`, *not the link to your repo homepage*.
