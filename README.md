# SmartCater Prototype
A simple prototype for SmartCater, a catering ingredient-ordering service.
The prototype allows the users to browse available meals, view ingredients and recipes, and see meal prices in different currencies.


## Features
- Browse meals with name, price and short description
- View ingredients and recipe by expanding each meal
- Display meal prices in multiple currencies (EUR, USD, GBP)
- Update the meal list dynamically
- Intuitive interface designed for ease of use


## Requirements
- Python 3.10+
- Tkinter (usually included with standard Python installations)


## Installation
1. Clone the repository
   ```bash
   git clone <repository_url>
   cd <repository_folder> 
   ```
2. (Optional) Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate     # Unix / Mac
   source venv\Scripts\activate # Windows
   ```
3. Install dependencies  
   (For this prototype, there are no additional dependencies to install.)


## Running the Demo
To run the demo, navigate to the repository folder and execute one of the following commands to start the demo
```bash
python3 smart_cater.py  # Unix / Mac
python smart_cater.py   # Windows
```

If neither command works, ensure that Python 3.10 or newer is installed and added to your system PATH.

Inside the demo you then can do the following things:
- Browse the sample meals in the main window.
- Click on a meal to expand ingredients and recipe details.
- Change the currency using the dropdown menu to see prices updated.
- Click the 'Refresh Meals' button to refresh available meals.  
  You can add or remove meals at any time (even at runtime) in the sample data `.json` files.


## Project structure
```
project/
├── requirements/             # Documentation of the requirements analysis
├── source/
│   ├── core/                 # Core classes (Meal, Ingredient, Currency)
│   └── data/                 # Sample data and update functions
├── sample_data/              # JSON files with some sample meals and ingredients
├── smart_cater.py            # Implementation and main entry point for the demo
└── README.md
```
