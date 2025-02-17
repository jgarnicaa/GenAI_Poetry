## Final Model Summary

### Executive Summary
- The model is capable of generating poems in **both English and Spanish**.
- Adjusting **temperature** is necessary to balance **coherence and creativity**, preventing repetitive outputs.
- In general, the model performs **better in Spanish**, likely due to dataset distribution.

### Problem Description
- The goal of this project was to **deploy a generative model** capable of creating **poems from a given first line**.
- Currently, the model generates poems with a **fixed length of 150 words**.

### Model Description
- **Fine-tuning a pre-trained LLM** was chosen as a **modern, accurate, and cost-efficient solution**.
- **GPT-2** was selected due to its **multilingual capabilities** and **low inference cost**.
- The fine-tuned model was optimized to generate structured poetic text while maintaining fluency.

### Conclusions & Recommendations
- **Inference on CPU is slow**, but the model produces **acceptable results**.
- **Hyperparameters like `top_p` and `temperature` were adjusted** to enhance creativity while keeping coherence.
- Deploying on **GPU-based instances** (e.g., AWS EC2 with GPU or AWS SageMaker) could significantly **reduce inference time**.


