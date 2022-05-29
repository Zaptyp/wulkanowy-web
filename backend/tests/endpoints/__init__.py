import pytest
#pytest.register_assert_rewrite("tests.endpoints.login")
pytest.register_assert_rewrite("tests.endpoints.login_incorrect")
pytest.register_assert_rewrite("tests.endpoints.symbol_incorrect")
pytest.register_assert_rewrite("tests.endpoints.grades_test")
pytest.register_assert_rewrite("tests.endpoints.school_info_test")