import streamlit as st
from main import get_qa_chain, create_vector_db

# Title of the application
st.title("Campus Queries App")

# Sidebar for navigation
st.sidebar.title("Navigation")
selected_option = st.sidebar.radio("Choose an option:", ["Ask a Question", "Create Knowledgebase"])

# Create Knowledgebase section
if selected_option == "Create Knowledgebase":
    st.header("Create Knowledgebase")
    btn = st.button("Create Knowledgebase")
    if btn:
        with st.spinner("Creating knowledgebase..."):
            create_vector_db()
            st.success("Knowledgebase created successfully!")
    st.write("Click the button above to create or update the knowledgebase.")

# Ask a Question section
elif selected_option == "Ask a Question":
    st.header("Ask a Question")

    question = st.text_input("Type your question here:")

    if question:
        with st.spinner("Getting the answer..."):
            chain = get_qa_chain()
            response = chain({"query": question})

            # Display the answer and source documents
            st.subheader("Answer")
            st.write(response["result"])

# Footer
st.markdown("""
    ---
    - Built by Kashif Ahmad
    - [GitHub](https://github.com/kashifgour)
    - [LinkedIn](https://www.linkedin.com/in/kashif-ahmad-548983220/)
""")
