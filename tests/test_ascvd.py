import pyascvd
import slash


def test_white_female() -> None:
    test_patient = {
        "age": 55,
        "sex": "female",
        "race": "white",
        "systolic_blood_pressure": 120,
        "total_cholesterol": 213,
        "hdl_cholesterol": 50,
        "diabetes": False,
        "smoker": False,
        "on_hypertension_treatment": False,
    }
    r = pyascvd.ascvd(**test_patient)
    slash.assert_almost_equal(r, 2.1, delta=0.1)


def test_white_male() -> None:
    test_patient = {
        "age": 55,
        "sex": "male",
        "race": "white",
        "systolic_blood_pressure": 120,
        "total_cholesterol": 213,
        "hdl_cholesterol": 50,
        "diabetes": False,
        "smoker": False,
        "on_hypertension_treatment": False,
    }
    r = pyascvd.ascvd(**test_patient)
    slash.assert_almost_equal(r, 5.4, delta=0.1)


def test_african_american_male() -> None:
    test_patient = {
        "age": 55,
        "sex": "male",
        "race": "aa",
        "systolic_blood_pressure": 120,
        "total_cholesterol": 213,
        "hdl_cholesterol": 50,
        "diabetes": False,
        "smoker": False,
        "on_hypertension_treatment": False,
    }
    r = pyascvd.ascvd(**test_patient)
    slash.assert_almost_equal(r, 6.1, delta=0.1)


def test_african_american_female() -> None:
    test_patient = {
        "age": 55,
        "sex": "female",
        "race": "aa",
        "systolic_blood_pressure": 120,
        "total_cholesterol": 213,
        "hdl_cholesterol": 50,
        "diabetes": False,
        "smoker": False,
        "on_hypertension_treatment": False,
    }
    r = pyascvd.ascvd(**test_patient)
    slash.assert_almost_equal(r, 3.0, delta=0.1)
