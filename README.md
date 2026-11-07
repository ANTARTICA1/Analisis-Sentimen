# Text Sentiment Analysis with Python & TextBlob

A natural language processing (NLP) application designed to perform textual sentiment classification and statistical distribution visualization using TextBlob and Matplotlib.

## Overview

Sentiment analysis (opinion mining) is a computational linguistic technique used to determine whether user opinions, reviews, or social media statements convey positive, negative, or neutral sentiment. This project processes a collection of textual evaluation statements, calculates continuous polarity indices, and renders statistical distributions into an analytical chart.

## Theoretical Foundation

### 1. Polarity Metric
The sentiment analysis engine employs TextBlob's lexicon-based sentiment analyzer. Each textual input is evaluated for **polarity**, a floating-point score in the range:

$$\text{Polarity} \in [-1.0, +1.0]$$

- Positive Sentiment: $\text{Polarity} > 0.0$ (indicates satisfaction, approval, or positive emotion)
- Negative Sentiment: $\text{Polarity} < 0.0$ (indicates criticism, dissatisfaction, or negative emotion)
- Neutral Sentiment: $\text{Polarity} = 0.0$ (indicates factual, objective, or balanced statements)

### 2. Statistical Aggregation and Distribution
The classification counts $N_{\text{pos}}$, $N_{\text{neg}}$, and $N_{\text{neu}}$ are aggregated across the corpus $C$:

$$\%_{\text{category}} = \frac{N_{\text{category}}}{|C|} \times 100\%$$

The resulting shares are visualized using a Matplotlib pie chart featuring standardized categorical color codings:
- Positive: Emerald Green (`#4CAF50`)
- Negative: Crimson Red (`#F44336`)
- Neutral: Amber Gold (`#FFC107`)

## Project Structure

```
Analisis-Sentimen/
├── analisis sentimen.py    # Main NLP classification and visualization script
└── README.md               # Technical documentation
```

## System Requirements

- Python 3.8 or higher
- TextBlob library
- Matplotlib library

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ANTARTICA1/Analisis-Sentimen.git
   cd Analisis-Sentimen
   ```

2. Install dependencies:
   ```bash
   pip install textblob matplotlib
   ```

3. Download required NLTK corpora (if running TextBlob for the first time):
   ```bash
   python -m textblob.download_corpora
   ```

## Execution

Execute the main script via terminal:
```bash
python "analisis sentimen.py"
```

### Output

The script outputs console summary statistics:
```text
ANALISIS SENTIMEN
===========================================

Hasil Analisis Sentimen: 
Positif: 26 (51.0%)
Negatif: 19 (37.3%)
Netral: 6 (11.8%)
```
A Matplotlib window will automatically display the generated graphical chart.

## Customization

To analyze custom datasets or external feedback streams:
1. Open `analisis sentimen.py`.
2. Replace or append elements in the `tweets` list, or read directly from a CSV/JSON file using `pandas`.
3. Re-run the script to observe updated statistical distribution metrics.

## Author

Anak Agung Ngurah Krisna Artha Wibawa ([ANTARTICA1](https://github.com/ANTARTICA1))

## License

This project is licensed under the MIT License.