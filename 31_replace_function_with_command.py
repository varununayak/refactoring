# Replace Function with Command

from typing import NamedTuple


class MedicalExam(NamedTuple):
    is_smoker: bool


class Candidate:

    def __init__(self, name: str, exercises: bool) -> None:
        self.name = name
        self.exercises = exercises


def score(medical_exam, candidate):
    result = 0
    health_level = 100
    high_medical_risk_flag = False

    if medical_exam.is_smoker:
        health_level -= 10
        high_medical_risk_flag = True

    if candidate.exercises:
        health_level -= 5

    result = (2 if high_medical_risk_flag else 1) / health_level
    # lots mode code like this
    # ...

    return result


"""
Functions are the building blocks of programming. There are times when it can be
useful to encapsulate functions into their own objects, which is referred to as 
a "command object". Such an object is usually built around a single execution
method. It offers greater flexibility for the control and expression of a function
and can provide methods to build up parameters to support a richer lifecycle.
We can also add customizations using inheritance and hooks.
"""


class Scorer:

    def __init__(self, candidate, medical_exam) -> None:
        self.candidate = candidate
        self.medical_exam = medical_exam
        self.health_level = 100
        self.high_medical_risk_flag = False

    def score(self):

        self._account_for_smoking()
        self._account_for_exercise()

        result = (2 if self.high_medical_risk_flag else 1) / self.health_level
        # lots mode code like this
        # ...

        return result

    def _account_for_exercise(self):
        if self.candidate.exercises:
            self.health_level -= 5

    def _account_for_smoking(self):
        if self.medical_exam.is_smoker:
            self.health_level -= 10
            self.high_medical_risk_flag = True


if __name__ == "__main__":
    candidate = Candidate("Varun", exercises=True)
    medical_exam = MedicalExam(is_smoker=False)
    print(f"Score: {score(medical_exam, candidate)}")
    scorer = Scorer(candidate, medical_exam)
    print(f"Score: {scorer.score()}")
