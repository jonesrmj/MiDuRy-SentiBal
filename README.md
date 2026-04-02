# MiDuRy-SentiBal

Sentiment analysis on generative AI tweets.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jonesrmj/MiDuRy-SentiBal/blob/main/MiDuRy-SentiBal.ipynb)

## Dataset
[Generative AI Tweets — Kaggle](https://www.kaggle.com/datasets/arinjaypathak/generative-ai-tweets)

---

## Setup (run once)

**1. Clone the repo**
```bash
git clone https://github.com/jonesrmj/MiDuRy-SentiBal.git
cd MiDuRy-SentiBal
```

**2. Create a virtual environment and install dependencies**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**3. Open the notebook in VS Code**
- Open `MiDuRy-SentiBal.ipynb`
- Top right → **Select Kernel** → **Python Environments** → select `venv`
- Run all cells

---

## Daily workflow
```bash
git pull                  # get latest changes
source venv/bin/activate  # activate venv
```
Then open the notebook in VS Code and run.

## Google Colab Notes

> **Use Colab for training only, not editing.**
> Make edits locally → push to GitHub → pull in Colab to run.
> If you edit on Colab, save back to GitHub immediately before anyone else pushes.

> **Colab does not auto-save your trained model.** The runtime is wiped on disconnect.
> Save the model to Google Drive after training:
> ```python
> from google.colab import drive
> drive.mount('/content/drive')
> model.save_pretrained('/content/drive/MyDrive/MiDuRy-SentiBal/model')
> ```
> Note: RoBERTa is ~500MB — too large for GitHub, use Drive instead.

---

## Repo Structure
```
data/
  tweets.csv              # dataset (included in repo)
MiDuRy-SentiBal.ipynb    # main notebook
requirements.txt          # dependencies
```
