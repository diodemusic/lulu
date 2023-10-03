import setuptools

readme = open("README.md", "r").read()
url = "https://github.com/diodemusic/lulu"

setuptools.setup(
    name="lulu",
    version="0.0.1",
    license="MIT",
    author="saves",
    description="A League of Legends API wrapper for the Riot API.",
    url=url,
    project_urls={
        "Source Code": url,
        "Pull Requests": url + "/pulls",
        "Issue Tracker": url + "/issues",
        # "Documentation": "https://lulu.readthedocs.io/",
    },
    long_description=readme,
    long_description_content_type="text/markdown",
    python_requires=">=3.8.0",
    zip_safe=False,
    packages=["lulu"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
