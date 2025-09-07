from setuptools import setup, find_packages

setup(
    name="signal_ict_devansh_92510133006",
    version="0.0.3",  # Change from 0.0.1 to 0.0.2
    author="Devansh",
    author_email="devansh@example.com",
    description="Custom signal processing package demonstrating Signals and Systems concepts",
    long_description="A comprehensive package for signal generation and operations including unitary signals, trigonometric signals, and signal operations.",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.19.0",
        "matplotlib>=3.3.0"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)