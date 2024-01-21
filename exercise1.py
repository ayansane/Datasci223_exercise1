from typing import List


# Question 1
# Define `round_scores(list_of_floats)`
def round_scores(list_of_floats: List[float]) -> List[int]:
    return [round(score) for score in list_of_floats]


# Question 2
def count_failed_students(student_scores: List[int]) -> int:
    count = [score for score in student_scores if score <= 40]
    return len(count)


# Question 3
def above_threshold(student_scores: List[int], threshold: int) -> List[int]:
    return [score for score in student_scores if score >= threshold]


# Question 4
def letter_grades(highest: int) -> List[int]:
    interval = round((highest - 40) / 4)
    next_highest = highest - interval + 1
    groups: List[int] = []
    while next_highest > 40:
        groups.insert(0, next_highest)
        next_highest = next_highest - interval
    return groups


# Question 5
def student_ranking(student_scores: List[int], student_names: List[str]) -> List[str]:
    return [
        f"{count + 1}. {student_names[count]}: {scores}"
        for count, scores in enumerate(student_scores)
    ]


# Question 6
def perfect_score(student_info: List[list]) -> List[list]:
    return [student for student in student_info if student[1] == 100]


if __name__ == "__main__":
    # Define `student_scores`
    student_scores = [90.33, 40.5, 55.44, 70.05,
                      30.55, 25.45, 80.45, 95.3, 38.7, 40.3]

    # Question 1
    print(round_scores(student_scores))

    # Question 2
    print(
        count_failed_students(
            student_scores=[90, 40, 55, 70, 30, 25, 80, 95, 38, 40])
    )

    # Question 3
    print(
        above_threshold(
            student_scores=[90, 40, 55, 70, 30, 68, 70, 75, 83, 96], threshold=75
        )
    )

    # Question 4
    print(letter_grades(highest=100))
    print(letter_grades(highest=88))

    # Question 5
    student_scores = [100, 99, 90, 84, 66, 53, 47]
    student_names = ["Joci", "Sara", "Kora", "Jan", "John", "Bern", "Fred"]

    print(student_ranking(student_scores, student_names))

    # Question 6
    print(perfect_score(student_info=[
          ["Charles", 90], ["Tony", 80], ["Alex", 100]]))
    print(perfect_score(student_info=[["Charles", 90], ["Tony", 80]]))
