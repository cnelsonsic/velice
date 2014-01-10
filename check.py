import re

def check(text):
    '''Check the given text for any issues like:
        * Contractions that can be expanded.
    '''
    contractions_regex = re.compile(r"(\b[a-zA-Z]+'[a-zA-Z]+\b)")
    results = []
    for match in contractions_regex.findall(text):
        if match.endswith("'s"):
            # Dont want possessives.
            continue
        else:
            results.append(('contraction', match))
    return results
