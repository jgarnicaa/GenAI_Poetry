# Data Summary

## Data Origin

- English poetry dataset comes from [Poetry Foundation Poems](https://www.kaggle.com/datasets/tgdivy/poetry-foundation-poems) avaliable in *Kaggle*.
- Spanish poetry dataset was taken using web scraping from [Poemas del Alma](https://www.poemas-del-alma.com), after that dataset were uploaded to public use, could be found here [Spanish poetry dataset | Dataset poemas en español](https://www.kaggle.com/datasets/jgarnicaaza/spanish-poetry-dataset-dataset-poemas-en-espaol)

## data load scripts

- Data is used in csv format, could be load like is shown in [EDA](https://github.com/jgarnicaa/GenAI_Poetry/blob/main/src/EDA/EDA_ES.ipynb).

### Data origin route

- In this project the brute and cleaned data was stored in a S3 Bucket, could be see here: [Data bucket](https://genaipoetry-bucket.s3.eu-west-3.amazonaws.com/files/)
- There are two tables one with spanish poetry dataset and another one with english dataset.

# Data dictionary

## Database. English Dataset.

** English poems and other atributes. 13754 unique poems.

| Variable | Description | Type | Range |
| --- | --- | --- | --- |
| # | Poem key to identify each one | Integer | [0 - 9999] |
| Title | Poem's Title | String | - (13240 unique values) |
| Poem | Poem itself | String | - (13754 unique values)|
| Poet | Poet's name | String | - (3128 unique values) |
| Tags | The tags as labelled by Poetry Foundation for the poem | String | - (12795 unique values) |

## Database. Spanish Dataset.

** Spanish poems and other atributes. 13084 unique poems.

| Variable | Description | Type | Range |
| --- | --- | --- | --- |
| Title | Poem's Title | String | - (12149 unique values) |
| Poem | Poem itself | String | - (13084 unique values)|
| Author | Poet's name | String | - (1354 unique values) |


# Data report

## Data general summary

El conjunto de datos cuenta con un total de $438557$ observaciones. Se tienen $17$ variables socioeconómicas y $2$ variables relacionadas con el pago de los créditos. En la primera tabla se evidencia la falta de datos para la columna de "ocupación" además de la presencia de información duplicada.

All dataset has a total of $25563$ samples. We had 5 variables to English Dataset and 3 variables for spanish dataset. We see a some poems are too long, which could be intrepeted as noise, for that reason it's necessary to drop it out.

## Quality summary data

The only issue could be the length of some poems and some breaklines. As we see after dropping poems extra large the distribution is better.

## Target variable

In this case the tokenizer for LLM chosen (GPT2) is in charge to generate the target variable, will be the next character in function with the data in enter, in this way it will predict the next character.



