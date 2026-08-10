def get_grades(marks):
    if marks >= 90:
        return "A grade"
    if marks >= 75:
        return "B grade"
    if marks >= 60:
        return "C grade"
    if marks >= 35:
        return "D grade"
    else:
        return "F grade"
