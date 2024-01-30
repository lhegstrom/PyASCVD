from pyascvd import _pyascvd


def ascvd(
    age: float,
    sex: str,
    race: str,
    systolic_blood_pressure: float,
    total_cholesterol: float,
    hdl_cholesterol: float,
    diabetes: bool,
    smoker: bool,
    on_hypertension_treatment: bool,
) -> float:
    return _pyascvd.calculate_10_yr_ascvd(
        age,
        sex,
        race,
        systolic_blood_pressure,
        total_cholesterol,
        hdl_cholesterol,
        diabetes,
        smoker,
        on_hypertension_treatment,
    )
