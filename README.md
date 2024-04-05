# CS399 Module 7: Exploring Neural Word Embeddings with Python

![Python](https://img.shields.io/badge/python-3.9-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**Author**: Wonjoon Jun  
**Forked From**: Prof. Paulus at ERAU

Welcome to CS399 Module 7, where we dive into the fascinating world of Neural Word Embeddings using Python. This project, forked from the esteemed Prof. Paulus, aims to explore the intricacies of linguistic models through practical, hands-on experience.

## Table of Contents
- [Introduction](#introduction)
- [Compatibility Notice](#compatibility-notice)
- [Installation](#installation)
- [Usage](#usage)
- [Insights and Data Processing](#insights-and-data-processing)
- [Acknowledgments](#acknowledgments)

## Introduction

In this module, we explore the power of Neural Word Embeddings, leveraging the GloVe dataset for its remarkable accuracy in capturing linguistic nuances. This journey will illuminate the mechanisms by which models understand and process human language.

## Compatibility Notice

This version introduces `typing_extensions` for enhanced compatibility with Python versions prior to 3.10, diverging from the traditional `typing` module to ensure a smoother experience across different Python environments.

**Important**: If you've directly downloaded the files from GitHub, ensure that `short_glove.txt` is present and contains approximately 300MB of data to avoid any runtime issues.

## Installation

To get started, ensure you have Python 3.9 or later installed. Then, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
3. Run using streamlit
    ```bash
    streamlit run main.py

## Insights and Data Processing
The `gloVe model` was chosen because it was opensource, and it yielded the best results.

## Acknowledgements
1. https://blog.esciencecenter.nl/king-man-woman-king-9a7fd2935a85
2. https://www.geeksforgeeks.org/detect-and-remove-the-outliers-using-python/
3. https://www.assemblyai.com/blog/6-best-ai-playgrounds/
4. https://fasttext.cc/docs/en/english-vectors.html
