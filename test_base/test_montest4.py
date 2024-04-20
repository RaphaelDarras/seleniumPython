# test_functions.py

from mesfonctions import *
import pytest

CestQuandMes60 = lambda age : 60 - age

def pytest_report_teststatus(report, config):
    if report.passed:
        print(f"Test {report.nodeid} a réussi !")
    elif report.failed:
        print(f"Test {report.nodeid} a échoué !")



def test_CestQuandMes60():
    age = 40
    assert CestQuandMes60(age) == 20

def test_verifier_age():
    prenom = "John"
    nom = "Doe"
    
    # Test pour age > 35
    age = 40
    assert verifierAge(prenom, nom, age) == [prenom, nom, 20]

    # Test pour age == 35
    age = 35
    assert verifierAge(prenom, nom, age) == [prenom, nom, 25]

    # Test pour age < 35
    age = 30
    assert verifierAge(prenom, nom, age) == [prenom, nom, 30]

def test_CestQuandMes60v2():
    age = 40
    assert CestQuandMes60(age) == 20