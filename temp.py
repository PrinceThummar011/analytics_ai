import streamlit as st
import pandas as pd
import chardet
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)

st.title("Data Analysis Assistant")
st.write("Upload your CSV or Excel file and ask questions about your data")

def detect_encoding(file):
    
    raw_data = file.read()
    
    file.seek(0)
    
    result = chardet.detect(raw_data)
    return result['encoding']

def read_file(uploaded_file):
   
    file_extension = uploaded_file.name.split('.')[-1].lower()
    
    if file_extension == 'csv':
        
        encoding = detect_encoding(uploaded_file)
        st.info(f"Detected CSV file encoding: {encoding}")
        return pd.read_csv(uploaded_file, encoding=encoding)
    
    elif file_extension in ['xlsx', 'xls']:
       
        return pd.read_excel(uploaded_file)
    
    else:
        raise ValueError("Unsupported file format")

def analyze_with_groq(data, question):
    prompt = f"""
    Here is the data: {data}
    
    Question: {question}
    
    Please analyze this data and provide a detailed answer. Include relevant statistics and insights.
    """
    
    try:
        
        completion = client.chat.completions.create(
            model="llama3-70b-8192", 
            messages=[
                {"role": "system", "content": "You are a helpful data analysis assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=1000
        )
        
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# File uploader
uploaded_file = st.file_uploader("Upload your data file", type=['csv', 'xlsx', 'xls'])
if uploaded_file:
    try:
        
        df = read_file(uploaded_file)
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
       
        st.subheader("Data Preview")
        st.dataframe(df.head())
        
        st.subheader("Available Columns")
        st.write(", ".join(df.columns.tolist()))
        
       
        st.subheader("Dataset Info")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"Total Rows: {df.shape[0]}")
        with col2:
            st.write(f"Total Columns: {df.shape[1]}")
        with col3:
            st.write(f"File Type: {uploaded_file.name.split('.')[-1].upper()}")
            
        question = st.text_input("What would you like to know about your data?",
                               placeholder="e.g., What are the main trends? What's the average of column X?")
        
        if st.button("Analyze"):
            with st.spinner("Analyzing data..."):
                
                data_summary = {
                    'columns': list(df.columns),
                    'sample_data': df.head().to_dict(),
                    'basic_stats': df.describe().to_dict(),
                    'data_types': df.dtypes.astype(str).to_dict()  
                }
                
                
                analysis = analyze_with_groq(str(data_summary), question)
                
                
                st.subheader("Analysis Results")
                st.markdown("---")
                st.write(analysis)
                st.markdown("---")
        
        
        with st.expander("Show Additional Analysis Options"):
            # Statistical summary
            if st.checkbox("Show Statistical Summary"):
                st.subheader("Statistical Summary")
                st.write(df.describe())
            
          
            if st.checkbox("Show Missing Values Analysis"):
                st.subheader("Missing Values")
                missing_data = df.isnull().sum()
                if missing_data.any():
                    st.write(missing_data[missing_data > 0])
                else:
                    st.write("No missing values found in the dataset!")
            
            # Data types
            if st.checkbox("Show Data Types"):
                st.subheader("Column Data Types")
                st.write(df.dtypes)
            
    except Exception as e:
        st.error(f"Error reading file: {str(e)}")
        st.info("Please make sure your file is properly formatted and not corrupted")

with st.sidebar:
    st.subheader("About")
    st.write("""
    This data analysis tool uses AI to help you understand your data.
    Upload a CSV or Excel file and ask questions in natural language.
    """)
    
    st.subheader("Supported File Types")
    st.write("""
    - CSV (.csv)
    - Excel (.xlsx, .xls)
    """)
    
    st.subheader("Tips")
    st.write("""
    - Make sure your file is properly formatted
    - For CSV files, UTF-8 encoding is recommended
    - Ask specific questions about your data
    - Try asking about:
        * Trends and patterns
        * Statistical summaries
        * Relationships between columns
        * Data distribution
    """)

st.markdown("---")
st.markdown("Built with Streamlit + AI")