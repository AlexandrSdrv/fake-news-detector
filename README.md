# Fake news detector

Binary text classifier fine-tuned on DistilBERT to detect fake news articles.

Live working model:   
    Try here - https://huggingface.co/spaces/AlexandrSdrv/fake-news-detector

Dataset
-
- **Source:** [ISOT Fake News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- **Real news:** ~21,000 articles from Reuters
- **Fake news:** ~23,000 articles from flagged sources
- **Split:** 80% train / 10% validation / 10% test

Notes:
-
- The "True" articles in the dataset mostly contain date and location mentions, so for the model to correctly analyze the content, instead of relying on composition hints, all of the additional information from real articles was removed before training the model.

Limitations:
-
- The model was trained on the Reuters database of real articles, so it is biased to recognize their writing style as real information.
- Does not generalize well to social media text, satire, or non-English content.
- Publisher names in articles can still bias predictions. For example, if the headline contains the word "Reuters", the verdict is biased toward "Real" despite the content.
- Performance degrades on recent articles because the dataset is only based on 2016-2017 articles.
- The greatest performance of the model is when the topic is politics.

Tech stack:
-
Python, HuggingFace Transformers, DistilBERT, PyTorch, Gradio, Pandas, Scikit-learn

Instructions:
-
If you want to run it locally:  
Requirements: Python 3.8+, Git

    1. **Clone the repository**
    ```bash
    git clone https://github.com/AlexandrSdrv/fake-news-detector.git
    cd fake-news-detector
    ```

    2. **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

    3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

    4. **Download the model**

    Download the model files from the [HuggingFace Space](https://huggingface.co/spaces/AlexandrSdrv/fake-news-detector/tree/main) and place them in a `model/` folder in the project root. You need these files:
    - `config.json`
    - `model.safetensors`
    - `tokenizer.json`
    - `tokenizer_config.json`

    5. **Run the app**
    ```bash
    python app.py
    ```
    Then open **http://127.0.0.1:7860** in your browser.
