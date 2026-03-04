#!/usr/bin/env python3
"""
Skills Manager Application
Manage and explore a collection of professional and technical skills
"""

# Skills database organized by category
SKILLS = {
    "python": {
        "name": "Python",
        "category": "Programming Languages",
        "proficiency": "Advanced",
        "years_experience": 5,
        "description": "High-level, general-purpose programming language known for readability and versatility.",
        "use_cases": [
            "Web development with Django and Flask",
            "Data science and machine learning",
            "Scripting and automation",
            "API development",
            "Testing and quality assurance"
        ],
        "related_skills": ["Django", "Flask", "NumPy", "Pandas", "pytest"]
    },
    "javascript": {
        "name": "JavaScript",
        "category": "Programming Languages",
        "proficiency": "Intermediate",
        "years_experience": 3,
        "description": "Lightweight, interpreted language primarily used for web development.",
        "use_cases": [
            "Frontend web development",
            "Backend development with Node.js",
            "Building interactive user interfaces",
            "REST API development",
            "Mobile development with React Native"
        ],
        "related_skills": ["Node.js", "React", "TypeScript", "Express", "npm"]
    },
    "git": {
        "name": "Git",
        "category": "Tools",
        "proficiency": "Advanced",
        "years_experience": 6,
        "description": "Distributed version control system for tracking changes in source code.",
        "use_cases": [
            "Source code version control",
            "Collaborative software development",
            "Branch management and code reviews",
            "CI/CD pipeline integration",
            "Open source contribution"
        ],
        "related_skills": ["GitHub", "GitLab", "Bitbucket", "GitHub Actions"]
    },
    "docker": {
        "name": "Docker",
        "category": "DevOps",
        "proficiency": "Intermediate",
        "years_experience": 2,
        "description": "Platform for developing, shipping, and running applications in containers.",
        "use_cases": [
            "Application containerization",
            "Consistent development environments",
            "Microservices deployment",
            "CI/CD pipeline integration",
            "Multi-container orchestration"
        ],
        "related_skills": ["Kubernetes", "Docker Compose", "container registries"]
    },
    "sql": {
        "name": "SQL",
        "category": "Databases",
        "proficiency": "Advanced",
        "years_experience": 4,
        "description": "Structured Query Language for managing and querying relational databases.",
        "use_cases": [
            "Database querying and manipulation",
            "Schema design and management",
            "Data analysis and reporting",
            "Stored procedures and functions",
            "Performance tuning and indexing"
        ],
        "related_skills": ["PostgreSQL", "MySQL", "SQLite", "data modeling"]
    },
    "machine_learning": {
        "name": "Machine Learning",
        "category": "Data Science",
        "proficiency": "Beginner",
        "years_experience": 1,
        "description": "Subset of AI enabling systems to learn from data and improve without explicit programming.",
        "use_cases": [
            "Predictive modeling",
            "Image and speech recognition",
            "Natural language processing",
            "Recommendation systems",
            "Anomaly detection"
        ],
        "related_skills": ["scikit-learn", "TensorFlow", "PyTorch", "NumPy", "Pandas"]
    },
    "terraform": {
        "name": "Terraform",
        "category": "DevOps",
        "proficiency": "Intermediate",
        "years_experience": 2,
        "description": "Infrastructure as Code tool for provisioning and managing cloud resources.",
        "use_cases": [
            "Cloud infrastructure provisioning",
            "Multi-cloud deployments",
            "Infrastructure versioning",
            "Automated environment management",
            "Compliance and governance"
        ],
        "related_skills": ["AWS", "Azure", "GCP", "HCL", "Ansible"]
    }
}

PROFICIENCY_LEVELS = ["Beginner", "Intermediate", "Advanced", "Expert"]


def display_skill(skill_key):
    """Display a complete skill profile with formatting"""
    if skill_key not in SKILLS:
        print("Skill not found!")
        return

    skill = SKILLS[skill_key]

    print(f"\n{'='*60}")
    print(f"🛠️  {skill['name']}")
    print(f"{'='*60}")
    print(f"Category:    {skill['category']}")
    print(f"Proficiency: {skill['proficiency']}")
    print(f"Experience:  {skill['years_experience']} year(s)")
    print(f"\n📖 DESCRIPTION:")
    print(f"   {skill['description']}")

    print(f"\n💡 USE CASES:")
    print("-" * 30)
    for use_case in skill['use_cases']:
        print(f"  • {use_case}")

    print(f"\n🔗 RELATED SKILLS:")
    print("-" * 30)
    print(f"  {', '.join(skill['related_skills'])}")
    print("=" * 60)


def search_skills_by_keyword(keyword):
    """Search skills by keyword in name, category, description, or use cases"""
    if not keyword or not keyword.strip():
        return []

    matching_skills = []
    keyword_lower = keyword.lower()

    for key, skill in SKILLS.items():
        if keyword_lower in skill['name'].lower():
            matching_skills.append((key, skill['name']))
            continue

        if keyword_lower in skill['category'].lower():
            matching_skills.append((key, skill['name']))
            continue

        if keyword_lower in skill['description'].lower():
            matching_skills.append((key, skill['name']))
            continue

        for use_case in skill['use_cases']:
            if keyword_lower in use_case.lower():
                matching_skills.append((key, skill['name']))
                break

    return matching_skills


def filter_skills_by_category(category):
    """Return all skills matching a given category (case-insensitive)"""
    if not category or not category.strip():
        return []

    return [
        (key, skill['name'])
        for key, skill in SKILLS.items()
        if skill['category'].lower() == category.strip().lower()
    ]


def filter_skills_by_proficiency(proficiency):
    """Return all skills at a given proficiency level (case-insensitive)"""
    if not proficiency or not proficiency.strip():
        return []

    return [
        (key, skill['name'])
        for key, skill in SKILLS.items()
        if skill['proficiency'].lower() == proficiency.strip().lower()
    ]


def get_skill_by_number(skill_number):
    """Get skill key by its display number"""
    skill_keys = list(SKILLS.keys())
    if 1 <= skill_number <= len(skill_keys):
        return skill_keys[skill_number - 1]
    return None


def list_all_skills():
    """Display a summary list of all available skills"""
    print("\n🛠️  Available Skills:")
    print("=" * 60)
    for i, (key, skill) in enumerate(SKILLS.items(), 1):
        print(f"{i}. {skill['name']}")
        print(f"   Category: {skill['category']} | Proficiency: {skill['proficiency']} | "
              f"{skill['years_experience']} yr(s)")
    print("=" * 60)


def list_categories():
    """Return a sorted list of unique skill categories"""
    return sorted({skill['category'] for skill in SKILLS.values()})


def main():
    """Main function to run the skills manager application"""
    print("🛠️  Skills Manager")
    print("=" * 45)

    skills_viewed = 0

    while True:
        print("\nSelect an option:")
        print("1. View all skills")
        print("2. Display a specific skill")
        print("3. Search skills by keyword")
        print("4. Filter by category")
        print("5. Filter by proficiency level")
        print("6. View skills viewed count")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice (1-7): "))

            if choice == 1:
                list_all_skills()

            elif choice == 2:
                list_all_skills()
                try:
                    skill_num = int(input(f"\nEnter skill number (1-{len(SKILLS)}): "))
                    skill_key = get_skill_by_number(skill_num)
                    if skill_key:
                        display_skill(skill_key)
                        skills_viewed += 1
                    else:
                        print("Invalid skill number!")
                except ValueError:
                    print("Please enter a valid number.")

            elif choice == 3:
                keyword = input("Enter search keyword: ").strip()
                if keyword:
                    matches = search_skills_by_keyword(keyword)
                    if matches:
                        print(f"\n🔍 Found {len(matches)} skill(s) matching '{keyword}':")
                        print("-" * 40)
                        for i, (key, name) in enumerate(matches, 1):
                            print(f"{i}. {name}")

                        try:
                            choice_num = int(input(f"\nSelect skill to view (1-{len(matches)}): "))
                            if 1 <= choice_num <= len(matches):
                                selected_key = matches[choice_num - 1][0]
                                display_skill(selected_key)
                                skills_viewed += 1
                            else:
                                print("Invalid selection!")
                        except ValueError:
                            print("Please enter a valid number.")
                    else:
                        print(f"No skills found matching '{keyword}'.")
                else:
                    print("Please enter a search keyword.")

            elif choice == 4:
                categories = list_categories()
                print("\n📂 Available Categories:")
                for i, cat in enumerate(categories, 1):
                    print(f"  {i}. {cat}")
                category = input("Enter category name: ").strip()
                if category:
                    matches = filter_skills_by_category(category)
                    if matches:
                        print(f"\n📂 Skills in '{category}':")
                        for _, name in matches:
                            print(f"  • {name}")
                    else:
                        print(f"No skills found in category '{category}'.")
                else:
                    print("Please enter a category name.")

            elif choice == 5:
                print(f"\n📊 Proficiency Levels: {', '.join(PROFICIENCY_LEVELS)}")
                proficiency = input("Enter proficiency level: ").strip()
                if proficiency:
                    matches = filter_skills_by_proficiency(proficiency)
                    if matches:
                        print(f"\n📊 Skills at '{proficiency}' level:")
                        for _, name in matches:
                            print(f"  • {name}")
                    else:
                        print(f"No skills found at proficiency level '{proficiency}'.")
                else:
                    print("Please enter a proficiency level.")

            elif choice == 6:
                print(f"Number of skills viewed: {skills_viewed}")

            elif choice == 7:
                print(f"Total skills viewed: {skills_viewed}")
                print("Thank you for using the Skills Manager! 🛠️")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
