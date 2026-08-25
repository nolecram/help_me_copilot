# Project Structure Reference

## Root Directory

```
HelpMeCopilot/
├── README.md                      # Main project documentation
├── CHANGELOG.md                   # Version history and updates
├── CONTRIBUTING.md                # Contribution guidelines
├── requirements.txt               # Python package dependencies
├── .gitignore                     # Git ignore rules
├── .github/                       # GitHub configuration
├── docs/                          # Documentation directory
├── src/                           # Source code and examples
├── modules/                       # Reusable Terraform modules
├── tests/                         # Test suite
└── assets/                        # Static assets and images
```

## Source Code Structure (`/src`)

### Applications (`src/`)
- **chocolate_cake_recipes.py** - Recipe management and display
- **temperature_converter.py** - Unit conversion utilities
- **ExcuseGenerator/** - Flask web application

### Examples (`src/examples/DiffFrame/HelloWorld/`)
- Hello World in 25+ programming languages
- **pom.xml** - Java build example

### Infrastructure
- **src/ICA_Azure_AWS/** - Azure/AWS Terraform examples and a LAMP stack (`lamp_stack_azure/`)
- **modules/lamp_stack/** - Reusable Terraform LAMP stack module

### Machine Learning (`src/ML_Experiments/`)
- Jupyter notebooks for ML experiments
- Sample ML functions

### Legacy & Language Examples
- **src/Legacy/** - Assembly, C, and COBOL examples
- **src/SybaseDB/** - Sybase C++ database examples
- **src/Ruby_Examples/** - Ruby examples
- **src/Chat/** - Copilot chat experiments

## Test Structure (`/tests`)
- test_chocolate_cake_recipes.py
- test_TestA.py
- TestB.py
- TestC.py
- Test.js (JavaScript tests)

## Configuration Files

### .gitignore
Comprehensive git ignore rules for:
- Python cache files
- Jupyter notebooks
- Node.js modules
- Terraform state files
- macOS files
- Environment variables
- IDE files

### requirements.txt
- pytest>=7.0.0

### CHANGELOG.md
Version history in Keep a Changelog format

### CONTRIBUTING.md
Contribution guidelines and workflow

---

**Last Updated:** August 25, 2026
