from setuptools import setup

setup(
    # Required fields
    name="loan_py",
    version="0.1.0",
    packages=["/Volumes/Data Science/Data Science Projects/loan_predictions_py/loan_py"],
    description="This package predict loan status",
    author="Gouthaman Tharmathasan",
    author_email="gouthaman87@gmail.com",
    package_data={"loan_py": ["config.ini", "data/*.csv"]},
    install_requires=[
        "pandas >= 0.23.0",
        "matplotlib >= 3"
    ],
)