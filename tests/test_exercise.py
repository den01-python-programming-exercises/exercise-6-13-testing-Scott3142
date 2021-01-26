import pytest
import src.exercise

def test_exercise():
    #implement tests here
    assert src.exercise.divide(3,4) == 0.75
    assert src.exercise.summation(3,4) == 7

    assert src.exercise.divide(3,-4) == -0.75
    assert src.exercise.summation(-3,4) == 1
