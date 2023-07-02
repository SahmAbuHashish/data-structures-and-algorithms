import re

def sort_by_title(movies):
    ignore_prefix = ['A', 'An', 'The']
    movies.sort(key=lambda x: (re.sub(r'^(A|An|The)\s+', '', x['title']).lower(), x['title']))
    return movies

def sort_by_year(movies):
    movies.sort(key=lambda x: x['year'], reverse=True)
    return movies
