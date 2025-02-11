# GenAI Poetry

**Generative AI for Poetry in Spanish and English**

## Overview

GenAI_Poetry is a project in Generative AI to create poetry in both Spanish and English. The model is fine-tuned on state-of-the-art large language model (LLM) GPT2 and is deployed through a web application utilizing Amazon AWS services for its architecture.

## Project Structure

- **data**: Contains the DVC file linked to regenerate data from S3 Bucket.
- **src**: Source code for data processing, model training, and deployment.
- **webapp**: Code for the web application that allows users to generate poetry.

## Datasets

The project utilizes two primary datasets:

1. **English Poetry Dataset**: Sourced from the [Poetry Foundation Poems](https://www.kaggle.com/datasets/tgdivy/poetry-foundation-poems) available on Kaggle.
2. **Spanish Poetry Dataset**: Collected through web scraping from [Poemas del Alma](https://www.poemas-del-alma.com) and made publicly available [here](https://www.kaggle.com/datasets/jgarnicaaza/spanish-poetry-dataset-dataset-poemas-en-espaol).

## Getting Started

To get started with this project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jgarnicaa/GenAI_Poetry.git
   cd GenAI_Poetry
