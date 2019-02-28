from setuptools import find_packages, setup

setup(
    name="pymongo-migrate",
    version="1.0.0",
    description="MongoDB data migration tool in Python",
    url="https://github.com/rooterkyberian/pymongo-migrate",
    license="Apache",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    platforms="any",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "pymongo>=3.7.2",
        "Click>=7",
        "dataclasses>=0.6; python_version<'3.7'",
    ],
    entry_points={"console_scripts": ["pymongo-migrate=pymongo_migrate.cli:cli"]},
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database",
    ],
)