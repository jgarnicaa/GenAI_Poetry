## Project Charter

### Project Name  
**Poetry Generator ES-EN**  

### Objective  
Develop a **Generative AI (GenAI) model** for text generation focused on Spanish and English poetry. The model will be fine-tuned on a **state-of-the-art (SOTA) large language model (LLM)** and deployed through a web application using **Amazon AWS services** for software architecture.  

### Project Scope  

The project consists of the following activities:  

- **Dataset acquisition:** Use public datasets or extract new ones through web scraping from public poetry websites/blogs.  
- **Exploratory Data Analysis (EDA):** Examine the dataset characteristics, identify patterns, missing values, anomalies, and class imbalance. Analyze dataset properties, including the number of poems, authors, and maximum length. Identify null values and define handling strategies, ensuring a balance between English and Spanish datasets.  
- **Data cleaning and preprocessing:** Perform data cleaning, transformation, and balancing. Remove NaN values, extract only the poem corpus, and properly handle line breaks and spaces.  
- **Model fine-tuning:** Select a base model for fine-tuning, set up **MLflow** logging, and integrate it with AWS to ensure traceability of training experiments.  
- **Model evaluation:** Use **perplexity** as a performance metric and conduct **human evaluation** to assess the quality of generated poems.  
- **Model deployment:** Deploy the model to be accessible through a **web application** using **containers** or an **API-based approach**.  
- **Web application development:** Develop a **simple and intuitive web application** that allows users to generate poems in both languages.  

### Project Deliverables  

✅ **Datasets:**  
- One dataset for **English poetry**, including **author, title, poem, and tags**.  
- One dataset for **Spanish poetry** obtained via **web scraping**.  

✅ **Expected Outcomes:**  
- Two **high-quality datasets** (Spanish and English poetry).  
- A **fine-tuned model** capable of generating **coherent** and **contextually relevant** poems.  
- A **functional web application** that allows any user to generate poetry.  

✅ **Success Criteria:**  
- The **model successfully generates** poetry in **English and Spanish**.  
- The **web application is accessible, user-friendly, and functional**.  

### Methodology  

- **Web Scraping:** Retrieve a **Spanish poetry dataset** through automated web scraping.  
- **Data Preparation:** Clean, transform, and balance the data.  
- **Model Fine-Tuning:** Select a **base model**, apply fine-tuning, and analyze results.  
- **Evaluation:** Test the model locally, **document results with MLflow**, and analyze outputs.  
- **Deployment:** Deploy the best model iteration using **FastAPI and/or Docker** to integrate it into a web app.  

### Project Team  
- **Jose Eduardo Garnica Aza**  

### Budget  

💰 **Projected Costs:**  
- **Cloud Computing & AWS Services:** Storage and cloud-based model training.  
- **Human Resources:** Development time, experimentation, and optimization.  
- **Web Application Maintenance:** API hosting or website deployment costs.  


