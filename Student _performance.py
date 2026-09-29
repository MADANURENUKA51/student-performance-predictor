def predict_performance(study_hours, attendance, previous_marks):
    score = (study_hours * 5) + (attendance * 0.3) + (previous_marks * 0.4)

    if score >= 70:
        return "Good Performance"
    else:
        return "Needs Improvement"


study_hours = float(input("Enter study hours per day: "))
attendance = float(input("Enter attendance percentage: "))
previous_marks = float(input("Enter previous marks: "))

result = predict_performance(study_hours, attendance, previous_marks)

print("Predicted Result:", result)
