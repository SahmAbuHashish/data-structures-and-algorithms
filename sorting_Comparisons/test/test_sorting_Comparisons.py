import pytest
from sorting_Comparisons.sorting_comparisons import sort_by_year,sort_by_title

def test_sort_by_year():
    movies = [
        {'title': 'Movie A', 'year': 2015, 'genres': ['Drama', 'Romance']},
        {'title': 'Movie B', 'year': 2010, 'genres': ['Action', 'Thriller']},
        {'title': 'Movie C', 'year': 2020, 'genres': ['Comedy', 'Romance']}
    ]
    sorted_by_year = sort_by_year(movies)
    assert sorted_by_year == [
        {'title': 'Movie C', 'year': 2020, 'genres': ['Comedy', 'Romance']},
        {'title': 'Movie A', 'year': 2015, 'genres': ['Drama', 'Romance']},
        {'title': 'Movie B', 'year': 2010, 'genres': ['Action', 'Thriller']}
    ]



def test_sort_by_title():
    movies = [
        {'title': 'The Movie', 'year': 2010, 'genres': ['Drama', 'Romance']},
        {'title': 'An Action Movie', 'year': 2020, 'genres': ['Action', 'Thriller']},
        {'title': 'A Comedy Movie', 'year': 2015, 'genres': ['Comedy', 'Romance']}
    ]
    sorted_by_title = sort_by_title(movies)
    assert sorted_by_title == [
        {'title': 'An Action Movie', 'year': 2020, 'genres': ['Action', 'Thriller']},
        {'title': 'A Comedy Movie', 'year': 2015, 'genres': ['Comedy', 'Romance']},
    ]
