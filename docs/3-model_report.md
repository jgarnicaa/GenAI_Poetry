# Final Model Summary

## Executive summary

- The model is capable to generate English and Spanish poems, it's necessary adjust the temperature to get coherent and non-repetitive poems. In general terms the model is more suitable to generate spanish poems.

## Problem description

- The main objective of this development was deploy a model which is able to generate poems from the first line given. For the moment is only necessary generate poems with 150 words length.

## Model description

- Using finetuning over a LLM archichecture was a modern, accurate and low cost solution, for that reason GPT2 model was choosen to be finetuned. This SOTA LLM hast multilingual support, has a low cost inference

## Evaluación del Modelo

- El rendimiento del modelo se evaluó por medio del `accuracy`, el cual tuvo un valor de $0.9906$ con los datos de prueba. La matriz de confusión se puede ver a continuación, en donde se identificó que hubo más falsos positivos que negativos, pero este modelo es bastante consistente con la clasificación de perfiles.

|   | 0 | 1 |
| --- | --- | --- |
| 0 | 10715 | 191 |
| 1 | 14 | 10891 |

## Conclusiones y Recomendaciones

- El rendimiento del último modelo fue bastante satisfactorio, teniendo en cuenta la métrica utilizada.

## Referencias

- [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Matplotlib - Pyplot](https://matplotlib.org/stable/tutorials/pyplot.html)
- [Imbalanced-learn](https://imbalanced-learn.org/stable/)
- [Seaborn](https://seaborn.pydata.org/) 
