# Langchain_All_In_One

# Openai question answering project workflow
<p align="center">
  <img src="https://github.com/AIWalaBro/Langchain_All_In_One/blob/main/flow_Charts/openai_que_ans.png" width=100% height=100%>
</p>

# Ollama- Llama3 
<p align="center">
  <img src="https://github.com/AIWalaBro/Langchain_All_In_One/blob/381fb25e91f32e747b324459a68532acd11f184d/flow_Charts/ollama-llama3.png" width=100% height=100%>
</p>

# API Creation Architecture
<p align="center">
  <img src="https://github.com/AIWalaBro/Langchain_All_In_One/blob/main/flow_Charts/api_architecture.png" width=100% height=100%>
</p>



# Retriever chain
<p align="center">
  <img src="https://github.com/AIWalaBro/Langchain_All_In_One/blob/05ae60e2aacc3dad24bb7d570ac63876e09400e0/flow_Charts/retrieverchain.png" width=100% height=100%>
</p>


# Multi-Search Retriever chain
<p align="center">
  <img src="https://github.com/AIWalaBro/Langchain_All_In_One/blob/main/flow_Charts/multi_images.png" width=75% height=50%>
</p>

<p align="center">
  <img src="https://github.com/AIWalaBro/Langchain_All_In_One/blob/main/flow_Charts/multi_retrieverchain_1.png" width=100% height=100%>
</p>







# Step to run this project

### How to run locally  

#### step1: create virtual environment
```bash
- conda create -p venv_langchain_all_in_one python=3.11 -y

```

#### step2: Activate virtual environment
```bash
- conda activate venv_langchain_all_in_one 
```

#### step3: Install Requirement Package
```bash
- pip install -r requirements.txt
```

### step4: Setup your environment variables and the API keys
```bash
- e.g: OPENAI_API_KEY = "abcd***************z"
```

#### step5: Run file 
```bash
- streamlit run app.py
- streamlit run ollama.py
```

- NOTE: always remember before running ollama.py in VS Code IDE. you have to run it first locally in CMD, by command (ollama run "model_name").
- then you will run streamlit run ollama.py in terminal otherwise it will throw an Connection Error at front end of streamlit.




