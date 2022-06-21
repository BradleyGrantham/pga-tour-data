import os
import subprocess

from setuptools import Command, find_packages, setup

REQS = ["atomicwrites==1.2.1",
        "attrs==18.2.0",
        "chardet==3.0.4",
        "cycler==0.10.0",
        "idna==2.7",
        "kiwisolver==1.0.1",
        "matplotlib==2.2.3",
        "more-itertools==4.3.0",
        "numpy==1.22.0",
        "pandas==0.23.4",
        "pluggy==0.7.1",
        "psycopg2==2.7.6.1",
        "py==1.6.0",
        "pymongo==3.7.1",
        "pyparsing==2.2.0",
        "pytest==3.8.0",
        "python-dateutil==2.7.3",
        "python-slugify==1.2.6",
        "pytz==2018.5",
        "requests==2.21.0",
        "scipy==1.1.0",
        "seaborn==0.9.0",
        "six==1.11.0",
        "SQLAlchemy==1.2.15",
        "Unidecode==1.0.22",
        "urllib3==1.23"
        ]


class Clean(Command):
    """Clean python setup build files."""

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    @staticmethod
    def run():
        """List of temporary objects"""

        path = os.path.dirname(os.path.abspath(__file__))

        subprocess.call(["rm", "-rf", os.path.join(path, "dist")])
        subprocess.call(["rm", "-rf", os.path.join(path, ".cache")])
        subprocess.call(["rm", "-rf", os.path.join(path, ".eggs")])
        subprocess.call(["rm", "-rf", os.path.join(path, "pga_tour_data.egg-info")])
        subprocess.call(["rm", "-rf", os.path.join(path, "pga_tour_data.egg-info")])
        subprocess.call(["rm", "-rf", os.path.join(path, "__pycache__")])
        subprocess.call(["rm", "-rf", os.path.join(path, "tests", "__pycache__")])
        subprocess.call(["rm", "-rf", os.path.join(path, "tests", ".cache")])
        subprocess.call(["find", path, "-name", "*.pyc", "-type", "f", "-delete"])
        subprocess.call(["find", path, "-name", "*.log", "-type", "f", "-delete"])


setup(
    name="pga-tour-data",
    maintainer="Bradley Grantham",
    version="0.0.1",
    author="Bradley Grantham",
    author_email="bradley.grantham@bath.edu",
    description="A package to scrape PGA Tour data and store in a PostgreSQL db",
    url="https://github.com/BradleyGrantham/pga-tour-data",
    packages=find_packages(),
    cmdclass={"clean": Clean},
    install_requires=REQS,
    tests_require=["pytest"]
)
