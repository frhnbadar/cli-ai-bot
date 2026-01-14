def confidence_score(response):
    length = len(response.split())
    if length < 5:
        return 0.3
    if length < 15:
        return 0.6
    return 0.85
