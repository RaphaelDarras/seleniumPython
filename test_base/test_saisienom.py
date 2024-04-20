import pytest

def custom_assert(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            print("Test réussi : {}".format(func.__name__))
        except AssertionError as e:
            print("Test échoué : {}".format(func.__name__))
            raise e
    return wrapper

def verif_nom(n):
    if n == "John":
        return "ok"
    else:
        return "ko"

def pytest_report_teststatus(report, config):
    if report.passed:
        print(f"Test {report.nodeid} a réussi !")
    elif report.failed:
        print(f"Test {report.nodeid} a échoué !")

@custom_assert
def test_verif_nom():
    nom = "John"
    assert verif_nom("John") == "ok"
    

#print(test_verif_nom(nom))