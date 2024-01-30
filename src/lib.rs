mod covariates;
mod ascvd;

use pyo3::prelude::*;
use crate::ascvd::calculate_10_yr_ascvd;


/// A Python module implemented in Rust.
#[pymodule]
fn _pyascvd(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(calculate_10_yr_ascvd, m)?)?;
    Ok(())
}
