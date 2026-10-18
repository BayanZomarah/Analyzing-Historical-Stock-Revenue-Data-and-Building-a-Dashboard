import compliance_phases


def test_package_exports_version() -> None:
    assert compliance_phases.__version__ == "0.1.0"
