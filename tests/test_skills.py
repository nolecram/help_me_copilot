#!/usr/bin/env python3
"""
Test module for skills.py
Tests the functionality of the skills manager application
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from skills import (
    SKILLS,
    PROFICIENCY_LEVELS,
    search_skills_by_keyword,
    filter_skills_by_category,
    filter_skills_by_proficiency,
    get_skill_by_number,
    list_categories
)


def test_skill_data_structure():
    """Test that all skills have required fields"""
    required_fields = ['name', 'category', 'proficiency', 'years_experience', 'description', 'use_cases', 'related_skills']

    assert len(SKILLS) > 0, "Should have at least one skill"

    for skill_key, skill in SKILLS.items():
        for field in required_fields:
            assert field in skill, f"Skill {skill_key} missing field {field}"

        assert isinstance(skill['name'], str), f"Skill {skill_key} name should be string"
        assert isinstance(skill['category'], str), f"Skill {skill_key} category should be string"
        assert isinstance(skill['proficiency'], str), f"Skill {skill_key} proficiency should be string"
        assert isinstance(skill['years_experience'], int), f"Skill {skill_key} years_experience should be int"
        assert isinstance(skill['description'], str), f"Skill {skill_key} description should be string"
        assert isinstance(skill['use_cases'], list), f"Skill {skill_key} use_cases should be list"
        assert isinstance(skill['related_skills'], list), f"Skill {skill_key} related_skills should be list"

        assert len(skill['use_cases']) > 0, f"Skill {skill_key} should have at least one use case"
        assert len(skill['related_skills']) > 0, f"Skill {skill_key} should have at least one related skill"


def test_skill_proficiency_values():
    """Test that all skills have valid proficiency levels"""
    for skill_key, skill in SKILLS.items():
        assert skill['proficiency'] in PROFICIENCY_LEVELS, (
            f"Skill {skill_key} proficiency '{skill['proficiency']}' not in {PROFICIENCY_LEVELS}"
        )


def test_skill_years_experience():
    """Test that years_experience values are reasonable"""
    for skill_key, skill in SKILLS.items():
        assert skill['years_experience'] >= 0, f"Skill {skill_key} years_experience should be non-negative"
        assert skill['years_experience'] <= 50, f"Skill {skill_key} years_experience seems unreasonably high"


def test_search_skills_by_keyword():
    """Test skill search functionality"""
    # Search by skill name
    results = search_skills_by_keyword("Python")
    assert len(results) > 0, "Should find Python skill"
    assert any("Python" in name for _, name in results), "Should find skill with 'Python' in name"

    # Search by category
    results = search_skills_by_keyword("DevOps")
    assert len(results) > 0, "Should find DevOps category skills"

    # Case-insensitive search
    results = search_skills_by_keyword("python")
    assert len(results) > 0, "Should find Python (case insensitive)"

    # Search in use cases
    results = search_skills_by_keyword("containerization")
    assert len(results) > 0, "Should find skill with 'containerization' in use cases"

    # Search with no results
    results = search_skills_by_keyword("nonexistent_xyz_skill")
    assert len(results) == 0, "Should return empty list for non-existent keyword"

    # Empty search
    results = search_skills_by_keyword("")
    assert len(results) == 0, "Should return empty list for empty keyword"

    # Whitespace-only search
    results = search_skills_by_keyword("   ")
    assert len(results) == 0, "Should return empty list for whitespace keyword"


def test_filter_skills_by_category():
    """Test filtering skills by category"""
    # Filter by a known category
    results = filter_skills_by_category("Programming Languages")
    assert len(results) > 0, "Should find Programming Languages skills"
    for key, _ in results:
        assert SKILLS[key]['category'] == "Programming Languages"

    # Case-insensitive filter
    results_upper = filter_skills_by_category("PROGRAMMING LANGUAGES")
    results_lower = filter_skills_by_category("programming languages")
    assert len(results_upper) == len(results_lower), "Category filter should be case-insensitive"

    # Unknown category
    results = filter_skills_by_category("Nonexistent Category")
    assert len(results) == 0, "Should return empty list for unknown category"

    # Empty category
    results = filter_skills_by_category("")
    assert len(results) == 0, "Should return empty list for empty category"


def test_filter_skills_by_proficiency():
    """Test filtering skills by proficiency level"""
    for level in PROFICIENCY_LEVELS:
        results = filter_skills_by_proficiency(level)
        # Each result should match the requested proficiency
        for key, _ in results:
            assert SKILLS[key]['proficiency'] == level

    # Case-insensitive filter
    results_upper = filter_skills_by_proficiency("ADVANCED")
    results_title = filter_skills_by_proficiency("Advanced")
    assert len(results_upper) == len(results_title), "Proficiency filter should be case-insensitive"

    # Invalid proficiency
    results = filter_skills_by_proficiency("Nonexistent Level")
    assert len(results) == 0, "Should return empty list for unknown proficiency"

    # Empty proficiency
    results = filter_skills_by_proficiency("")
    assert len(results) == 0, "Should return empty list for empty proficiency"


def test_get_skill_by_number():
    """Test getting a skill by its display number"""
    total_skills = len(SKILLS)

    skill_key = get_skill_by_number(1)
    assert skill_key is not None, "Should return a valid skill key for number 1"
    assert skill_key in SKILLS, "Returned key should exist in SKILLS"

    skill_key = get_skill_by_number(total_skills)
    assert skill_key is not None, f"Should return a valid skill key for number {total_skills}"

    assert get_skill_by_number(0) is None, "Should return None for skill number 0"
    assert get_skill_by_number(total_skills + 1) is None, "Should return None for number too high"
    assert get_skill_by_number(-1) is None, "Should return None for negative number"


def test_list_categories():
    """Test listing unique skill categories"""
    categories = list_categories()

    assert isinstance(categories, list), "list_categories should return a list"
    assert len(categories) > 0, "Should have at least one category"

    # All categories should be strings
    for cat in categories:
        assert isinstance(cat, str), "Each category should be a string"

    # Should contain only unique categories
    assert len(categories) == len(set(categories)), "Categories should be unique"

    # Should be sorted
    assert categories == sorted(categories), "Categories should be sorted"


def test_specific_skills_exist():
    """Test that expected skills are present in the database"""
    expected_skills = ["python", "javascript", "git", "docker", "sql"]

    for skill_key in expected_skills:
        assert skill_key in SKILLS, f"Expected skill '{skill_key}' not found"


def test_skill_content_quality():
    """Test that skill entries have meaningful content"""
    for skill_key, skill in SKILLS.items():
        assert len(skill['name']) > 1, f"Skill {skill_key} name is too short"
        assert len(skill['description']) > 20, f"Skill {skill_key} description is too short"

        for use_case in skill['use_cases']:
            assert len(use_case.strip()) > 5, f"Skill {skill_key} has a very short use case: '{use_case}'"

        for related in skill['related_skills']:
            assert len(related.strip()) > 0, f"Skill {skill_key} has an empty related skill"


if __name__ == "__main__":
    test_functions = [
        test_skill_data_structure,
        test_skill_proficiency_values,
        test_skill_years_experience,
        test_search_skills_by_keyword,
        test_filter_skills_by_category,
        test_filter_skills_by_proficiency,
        test_get_skill_by_number,
        test_list_categories,
        test_specific_skills_exist,
        test_skill_content_quality
    ]

    print("Running skills manager tests...")
    for test_func in test_functions:
        try:
            test_func()
            print(f"✓ {test_func.__name__}")
        except AssertionError as e:
            print(f"✗ {test_func.__name__}: {e}")
        except Exception as e:
            print(f"✗ {test_func.__name__}: Unexpected error - {e}")

    print("Tests completed!")
