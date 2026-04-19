# fake-news-detector

Fine-tuned DistilBERT model for fake news detection

Live working model:
Try here - https://huggingface.co/spaces/AlexandrSdrv/fake-news-detector

If you want to run it locally:
Requirements: Python 3.8+, Git

    1. Clone the repository
    ```bash
    git clone https://github.com/AlexandrSdrv/fake-news-detector.git
    cd fake-news-detector
    ```

    2. Create and activate a virtual environment
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

    3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

    4. Download the model

    Download the model files from the [HuggingFace Space](https://huggingface.co/spaces/AlexandrSdrv/fake-news-detector/tree/main) and place them in a `model/` folder in the project root. You need these files:
    - `config.json`
    - `model.safetensors`
    - `tokenizer.json`
    - `tokenizer_config.json`

    5. Run the app
    ```bash
    python app.py
    ```
    Then open **http://127.0.0.1:7860** in your browser.
