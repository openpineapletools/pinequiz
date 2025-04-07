from setuptools import setup, find_packages
from pathlib import Path

# Baca file README.md
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8", errors="ignore")

setup(
    name="pinequiz",
    version="1.0.0",
    author="openpineaplehub",
    author_email="openpineaple@gmail.com",
    description="🍍 PineQuiz CLI - Jalankan kuis terenkripsi dari GitHub",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/openpineapletools/pinequiz",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pinequiz = pinequiz.pinequiz:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests"
    ],
)
