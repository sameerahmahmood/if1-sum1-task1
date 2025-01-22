import pytest
from equation_quiz_generator import check_user_score
    
def test_check_user_score():
    #correct user case
    user_score, user_streak = check_user_score(10,10,0,0)
    assert user_score == 1
    assert user_streak == 1
    
    user_score, user_streak = check_user_score(7,3,1,1)
    assert user_score == 1
    assert user_streak == 0
    

