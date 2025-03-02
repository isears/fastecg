import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fastecg",
    version="0.0.1",
    author="Isaac Sears",
    author_email="isaac.j.sears@gmail.com",
    description="GPU Enabled ECG Signal Preprocessing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["fastecg"],
    url="https://github.com/isears/fastecg",
    project_urls={
        "Bug Tracker": "https://github.com/isears/fastecg/issues",
    },
)
