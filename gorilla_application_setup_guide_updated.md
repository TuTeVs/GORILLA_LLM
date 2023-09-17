SETUP LINK:
https://github.com/ShishirPatil/gorilla/blob/main/inference/README.md


# Gorilla Application Setup Guide

## Introduction

This guide will walk you through setting up a local Gorilla application with Streamlit. This setup will allow you to run the application by simply double-clicking a file.

## Step 1: Setting Up Your Python Environment

Since you are using your native Python version, there is no need to install Python 3.10 separately. You can verify your Python version by running the following command in your terminal or command prompt:

python --version

## Step 2: Installing Pipenv

Pipenv is a packaging tool for Python that aims to bring the best of all packaging worlds to the Python world. To install Pipenv, run the following command:

pip install pipenv

## Step 3: Setting Up Pipenv Environment

Once Pipenv is installed, navigate to your project directory and run the following command to create a virtual environment:

pipenv --python 3.11.5

Replace `3.x` with your native Python version.

## Step 4: Installing Dependencies

Next, install the necessary dependencies from the `requirements.txt` file using the following command:

pipenv install -r requirements.txt

## Step 5: Downloading the Necessary Models and Weights

1. **LLaMA Weights:**
   - Obtain the weights from [this form](https://...).
   - Convert them to the Hugging Face Transformers format using the conversion script:
    
     python src/transformers/models/llama/convert_llama_weights_to_hf.py --input_dir /path/to/downloaded/llama/weights --model_size 7B --output_dir /output/path

    CHANGE PATHS

2. **Gorilla Weights:**
   - Download the Gorilla delta weights from the [Hugging Face website](https://huggingface.co/gorilla-llm/).
   - Apply the delta weights to your LLaMA model:
  
     python3 apply_delta.py --base-model-path path/to/hf_llama/ --target-model-path path/to/gorilla-7b-hf-v0 --delta-path path/to/models--gorilla-llm--gorilla-7b-hf-delta-v0

    CHANGE PATHS

## Step 6: Setting Up the Gorilla Server

To set up the Gorilla server locally, use the following command:

python3 serve/gorilla_cli.py --model-path path/to/gorilla-7b-{hf,th,tf}-v0

CHANGE PATHS

## Step 7: Setting Up Streamlit Application

Refer to the Streamlit app script you provided earlier in the conversation. Save that script as `app.py` in your project directory.

## Step 8: Creating a Batch File for Automation

Create a batch file (`.bat` for Windows) with the following content to automate the starting process of the Streamlit app and the Gorilla server:


@echo off
start python3 serve/gorilla_cli.py --model-path path/to/gorilla-7b-{hf,th,tf}-v0
start streamlit run app.py

Save this batch file in the same directory as your `app.py`. Double-clicking this batch file will automatically start the Gorilla server and the Streamlit app.

## Conclusion

You now have a fully functional Gorilla application running locally, accessible via Streamlit. The setup process is automated, allowing you to run the entire application by simply double-clicking a file.

