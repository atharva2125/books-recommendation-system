import streamlit as st
import pandas as pd
import pickle

# Load data and model
df2 = pd.read_pickle("books_df2.pkl")
with open("knn_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("idlist.pkl", "rb") as f:
    idlist = pickle.load(f)

def bookRecom(name):
    book_list = []
    book_id = df2[df2['title'] == name].index
    if len(book_id) == 0:
        return []
    book_id = book_id[0]
    for new in idlist[book_id]:
        book_list.append(df2.loc[new].title)
    return book_list

st.title("Book Recommendation System")

book_titles = df2['title'].unique()
selected_book = st.selectbox("Select a book you like:", book_titles)

if st.button("Recommend"):
    recommendations = bookRecom(selected_book)
    if recommendations:
        st.write("Recommended Books:")
        for book in recommendations:
            st.write(f"- {book}")
    else:
        st.write("No recommendations found.")