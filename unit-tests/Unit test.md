# Pytest
We will use the Python library pytest. In general, pytest is [invoked](https://docs.pytest.org/en/stable/how-to/usage.html) with the command pytest. This will execute all tests in all files whose names follow the form test_*.py or \*_test.py in the current directory and its subdirectories. 

# Priority
We should first decide how we want to start testing. We can start, for example, testing the easiest pieces to test or focusing on the parts of the code that are responsible for the most breaks. 

In our example, the Order and LineItem classes are a main pieces of our code. 