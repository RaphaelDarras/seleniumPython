
from mesfonctions import *
import pytest

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