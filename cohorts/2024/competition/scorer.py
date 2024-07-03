import pandas as pd
import numpy as np


class ParticipantVisibleError(Exception):
    # If you want an error message to be shown to participants, you must raise the error as a ParticipantVisibleError
    # All other errors will only be shown to the competition host. This helps prevent unintentional leakage of solution data.
    pass


def score(solution: pd.DataFrame, submission: pd.DataFrame, row_id_column_name: str) -> float:
    '''
    Accuracy that works with multiple correct answers.
    '''
    solution = solution.set_index(row_id_column_name, drop=True)
    submission = submission.set_index(row_id_column_name, drop=True)
    submission = submission.loc[solution.index]
        
    target_column = 'answer'
    assert target_column in solution.columns
    assert target_column in submission.columns

    # This fix is needed because submission is loaded with default parameters
    # Pandas magically converts string column into float
    def fix_suffix(value):
        if value.endswith('.0'):
            return value[:-2]
        else:
            return value
        
    submission[target_column] = submission[target_column].astype(str)
    submission[target_column] = submission[target_column].apply(fix_suffix)
    
    
    def convert_to_list(value):
        values = [v.strip() for v in value.strip().lstrip('[').rstrip(']').split(',')]
        return values

    solution[target_column] = solution[target_column].astype(str).apply(convert_to_list)

    correct = [
        submit_answer in correct_answer
        for correct_answer, submit_answer in zip(
            solution[target_column].values, 
            submission[target_column].values
        )
    ]
            
    return np.mean(correct)