# Data Summary

## Data Origin

- The English poetry dataset comes from [Poetry Foundation Poems](https://www.kaggle.com/datasets/tgdivy/poetry-foundation-poems), available on *Kaggle*.
- The Spanish poetry dataset was collected using web scraping from [Poemas del Alma](https://www.poemas-del-alma.com). After that, the dataset was uploaded for public use and can be found here: [Spanish poetry dataset | Dataset poemas en español](https://www.kaggle.com/datasets/jgarnicaaza/spanish-poetry-dataset-dataset-poemas-en-espaol).

## Data Load Scripts

- The data is stored in CSV format and can be loaded as shown in the [EDA notebook](https://github.com/jgarnicaa/GenAI_Poetry/blob/main/src/EDA/EDA_ES.ipynb).

### Data Storage Location

- In this project, both raw and cleaned data are stored in an S3 Bucket, which can be accessed here: [Data bucket](https://genaipoetry-bucket.s3.eu-west-3.amazonaws.com/files/).
- There are two datasets: one containing Spanish poetry and the other containing English poetry.

# Data Dictionary

## English Dataset

**Contains 13,754 unique poems and additional attributes.**

| Variable | Description                       | Type    | Range                |
| -------- | --------------------------------- | ------- | -------------------- |
| #        | Unique poem identifier            | Integer | [0 - 9999]           |
| Title    | Poem title                        | String  | 13,240 unique values |
| Poem     | Poem text                         | String  | 13,754 unique values |
| Poet     | Poet's name                       | String  | 3,128 unique values  |
| Tags     | Tags labeled by Poetry Foundation | String  | 12,795 unique values |

## Spanish Dataset

**Contains 13,084 unique poems and additional attributes.**

| Variable | Description | Type   | Range                |
| -------- | ----------- | ------ | -------------------- |
| Title    | Poem title  | String | 12,149 unique values |
| Poem     | Poem text   | String | 13,084 unique values |
| Author   | Poet's name | String | 1,354 unique values  |

# Data Report

## General Data Summary

The dataset contains a total of **25,563** samples. The English dataset has **5 variables**, while the Spanish dataset has **3 variables**. Some poems are excessively long, which could introduce noise, making it necessary to filter and remove them.

## Data Quality Summary

The main quality issue is the length of some poems and inconsistencies in line breaks. 

![image](https://github.com/user-attachments/assets/2994d288-5f5e-43ad-ab50-7880637f05fc)


After filtering out excessively long poems, the distribution improves.

![image](https://github.com/user-attachments/assets/474c567f-57e1-48af-8024-ecd01a40837d)

## Target Variable

The chosen tokenizer for the **LLM model (GPT-2)** is responsible for generating the target variable. It predicts the next character based on the input data, ensuring coherent text generation.


