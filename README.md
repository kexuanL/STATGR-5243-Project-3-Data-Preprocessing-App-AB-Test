# STATGR 5243 Project 3: A/B Test for a Data Preprocessing App

This repository contains two versions of the same interactive data preprocessing web application. The project is designed for an A/B test that compares whether an onboarding guide improves or distracts from the user experience.

The app is built with Shiny for Python and provides a no-code workflow for uploading data, cleaning it, creating new features, exploring it visually, and exporting the processed dataset.

## A/B Test Design

The two versions are intentionally kept almost identical. The main experimental difference is the presence or absence of the User Guide tab.

| Version | Folder | Main Difference |
| --- | --- | --- |
| Version A | `Version A Code/Version A Code` | Includes a `User Guide` tab that introduces the workflow before users start processing data. |
| Version B | `Version B Code/Version B Code` | Removes the `User Guide` tab so users start directly from the `Data Upload` tab. |

The goal is to test whether the guided onboarding experience helps users understand the app faster, or whether removing it allows users to begin the preprocessing task more efficiently.

## App Features

- Upload datasets in CSV, Excel, JSON, or Parquet format.
- Load built-in sample datasets for quick testing.
- Preview dataset shape, column count, missing values, and duplicate rows.
- Handle missing values by dropping rows or columns, or using mean, median, mode, or constant imputation.
- Remove duplicate rows.
- Filter outliers using IQR or Z-score methods.
- Scale numeric columns with standardization or min-max scaling.
- Encode categorical columns with one-hot or label encoding.
- Convert column data types.
- Create new features through arithmetic operations, mathematical transformations, binning, and datetime extraction.
- View operation history and use undo/redo for preprocessing steps.
- Generate exploratory visualizations and summary statistics.
- Export the final processed dataset as a CSV file.

## Project Structure

```text
STATGR 5243 Project3/
|-- README.md
|-- Version A Code/
|   `-- Version A Code/
|       |-- app.py
|       |-- requirements.txt
|       |-- data/
|       |-- report/
|       `-- src/
`-- Version B Code/
    `-- Version B Code/
        |-- app.py
        |-- requirements.txt
        |-- data/
        |-- report/
        `-- src/
```

Each version has the same basic structure:

- `app.py`: main Shiny application file.
- `requirements.txt`: Python dependencies.
- `data/`: sample datasets used by the app.
- `src/`: helper modules for loading data, preprocessing, feature engineering, EDA, UI helpers, and utilities.
- `report/`: project report files.

## Installation

Use Python 3.10 or newer.

First, clone the repository:

```bash
git clone <your-github-repository-url>
cd "STATGR 5243 Project3"
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On macOS or Linux:

```bash
source venv/bin/activate
```

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies from either version folder. The dependency files are currently the same:

```bash
pip install -r "Version A Code/Version A Code/requirements.txt"
```

## Running Version A

Version A includes the User Guide tab.

```bash
cd "Version A Code/Version A Code"
shiny run app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8000
```

## Running Version B

Version B removes the User Guide tab and starts users directly with data upload.

From the repository root:

```bash
cd "Version B Code/Version B Code"
shiny run app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8000
```
