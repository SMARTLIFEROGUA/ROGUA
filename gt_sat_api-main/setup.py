"""Setup tools"""
import os

from setuptools import find_packages, setup

if os.environ.get("CI_COMMIT_TAG"):
    VERSION = os.environ["CI_COMMIT_TAG"]
elif os.environ.get("CI_JOB_ID"):
    VERSION = os.environ["CI_JOB_ID"]
else:
    VERSION = "1.0.3"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="gt_sat_api",
    version=VERSION,
    description="GT SAT API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="HomebrewSoft",
    author_email="moises@homebrewsoft.dev",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    url="https://gitlab.com/HomebrewSoft/l10n_gt/gt_sat_api",
    setup_requires=["setuptools_scm"],
    include_package_data=True,
)
