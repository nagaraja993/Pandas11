import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    examinations['attend'] = 1
    df = students.merge(subjects, how = 'cross').merge(examinations, on = ['student_id', 'subject_name'], how = 'left')
    df = df.groupby(['student_id', 'student_name', 'subject_name'], dropna=False).agg(attended_exams = ('attend', 'sum'))
    return df.reset_index().sort_values(by = ['student_id', 'subject_name'], ascending = [True, True])