import pytest
from equation_quiz_generator import check_user_score
    
def test_check_user_score():
    """ testing the check_user_score function to ensure that the score and streak are correct"""
    #correct user answer case
    user_score, user_streak = check_user_score(10,10,0,0)
    assert user_score == 1
    assert user_streak == 1
    #incorrect user answer case
    user_score, user_streak = check_user_score(7,3,1,1)
    assert user_score == 1
    assert user_streak == 0
    


    

