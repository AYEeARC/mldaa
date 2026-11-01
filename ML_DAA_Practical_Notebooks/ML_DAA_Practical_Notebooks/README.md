# ML and DAA Practical Notebooks

This repository pack contains 11 separate Jupyter notebooks:
- `DAA/`: 5 Design and Analysis of Algorithms practicals.
- `ML/`: 6 Machine Learning practicals.
- `datasets/`: place your CSV datasets here.

## Setup (Windows)
```bash
py -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

In VS Code, install the Python and Jupyter extensions, open a notebook, and select the `.venv` kernel.

## Dataset files expected
Put the following files in `datasets/` (names can be changed in the notebook):
- `uber.csv`
- `email.csv`
- `Churn_Modelling.csv`
- `diabetes.csv`
- `sales_data_sample.csv`

The notebooks state their expected columns. Your actual lab datasets may use different names; update the `DATA_PATH`, target, or column variables accordingly. Dataset files are not included in this pack.

## Run
Open any `.ipynb` file and choose **Run All**.

## Git
From the repository root:
```bash
git add .
git commit -m "Add ML and DAA practical notebooks"
git push origin main
```

## Important
These are clean, runnable practical implementations based on the practical topics discussed. They are not claimed to be byte-for-byte copies of your original uploaded scripts or your institution's exact lab code. Verify dataset column names and experiment-specific requirements against your lab manual.
