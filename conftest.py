# v) Time measurement fixture in conftest.py
# This fixture will measure the execution time of each test

import pytest
import time

@pytest.fixture(autouse=True)
def time_measure(request):
    start_time = time.time()
    yield
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Test '{request.node.name}' took {execution_time:.6f} seconds.")