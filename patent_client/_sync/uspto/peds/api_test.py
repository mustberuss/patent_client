# ********************************************************************************
# *         WARNING: This file is automatically generated by unasync.py.         *
# *                             DO NOT MANUALLY EDIT                             *
# *           Source File: patent_client/_async/uspto/peds/api_test.py           *
# ********************************************************************************


from .api import PatentExaminationDataSystemApi


def test_can_get_app():
    result = PatentExaminationDataSystemApi().create_query("applId:(16123456)")
    assert result.num_found == 1
    assert result.applications[0].appl_id == "16123456"


def test_can_search_by_customer_number():
    result = PatentExaminationDataSystemApi().create_query("appCustNumber:(70155)")
    assert result.num_found > 10


def test_can_limit_by_rows():
    result = PatentExaminationDataSystemApi().create_query(
        "appCustNumber:(70155)", rows=5
    )
    assert len(result.applications) == 5
