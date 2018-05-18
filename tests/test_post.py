import pytest
import postToFirebase
import requests


def test_get_database():
    assert postToFirebase.get_database('https://hackernewsgraphs.firebaseio.com/') is not None


def test_invalid_get_database():
    with pytest.raises(SystemExit):
        postToFirebase.get_database('https://hackernewsgraphs123.firebaseio.com/')

#test that TRACELIST elements are in database

#test what get_FB_keys() is returning

#test if pass legit dataframe that maketrace() works

#test if you pass illegit dataframe that maketrace() crashes gracefully 