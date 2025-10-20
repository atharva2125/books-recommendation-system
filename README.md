# Book Recommendation System

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-0.24+-green.svg)

A machine learning-powered book recommendation system that suggests similar books based on user selection. This application uses K-Nearest Neighbors (KNN) algorithm to find books with similar features and presents recommendations through an interactive Streamlit web interface.

## Features

- Interactive web interface built with Streamlit
- Book recommendations based on similarity using KNN algorithm
- Large dataset of books with detailed information
- Fast and efficient recommendation generation

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/books-recommendation-system.git
   cd books-recommendation-system
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install streamlit pandas scikit-learn pickle-mixin
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. The application will open in your default web browser. If it doesn't, navigate to the URL shown in the terminal (typically http://localhost:8501).

3. Select a book you like from the dropdown menu and click the "Recommend" button to get similar book recommendations.

## Example

```python
# The application uses the following function to generate recommendations
def bookRecom(name):
    book_list = []
    book_id = df2[df2['title'] == name].index
    if len(book_id) == 0:
        return []
    book_id = book_id[0]
    for new in idlist[book_id]:
        book_list.append(df2.loc[new].title)
    return book_list
```

## Project Structure

```
books-recommendation-system/
├── app.py                      # Streamlit application
├── books.csv                   # Original dataset
├── books_df2.pkl               # Processed book dataframe
├── books_recommendation.ipynb  # Jupyter notebook with model development
├── features.pkl                # Extracted book features
├── idlist.pkl                  # List of book IDs
└── knn_model.pkl               # Trained KNN model
```

## Data

The system uses a dataset of books that includes information such as:
- Book titles
- Authors
- Publication details
- Genre information
- User ratings

## Model

The recommendation system uses a K-Nearest Neighbors (KNN) algorithm to find books with similar features. The model is pre-trained and saved as `knn_model.pkl`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code follows the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The dataset used in this project is derived from [Goodreads](https://www.goodreads.com/)
- Thanks to all contributors who have helped shape this project

## Contact

If you have any questions or suggestions, please open an issue or contact the repository owner.

---

Made with ❤️ by ROSPL07