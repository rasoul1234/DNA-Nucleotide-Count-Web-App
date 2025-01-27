# DNA Nucleotide Count Web App

This project is a simple web application built using **Streamlit**. The app allows users to input a DNA sequence and computes the count of each nucleotide (Adenine, Thymine, Guanine, Cytosine) in the sequence. Additionally, the app provides visualizations of the nucleotide counts.

---

## Features

1. **DNA Sequence Input**:

   - Users can input their DNA sequence in a text area.
   - The app processes the sequence to remove headers and combine lines into a single string.

2. **Nucleotide Count**:

   - Computes the count of each nucleotide (A, T, G, C).

3. **Output Formats**:

   - Displays nucleotide counts as:
     - A dictionary.
     - Text output.
     - A data table.

4. **Visualization**:

   - Displays a bar chart of nucleotide counts using Altair.

5. **Image Display**:

   - Displays a DNA-related image loaded from a URL.

---

## Requirements

The following Python libraries are required for this project:

- `streamlit`
- `pandas`
- `numpy`
- `altair`
- `Pillow`
- `requests`

You can install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

---

## File Structure

```
.
├── DNA-Nucleotide-Count-Web-App.py  # Main application script
├── requirements.txt                 # List of dependencies
├── README.md                        # Documentation file
```

---

## How to Run the App

1. Clone this repository:

   ```bash
   git clone https://github.com/rasoul1234/DNA-Nucleotide-Count-Web-App.git
   ```

2. Navigate to the project directory:

   ```bash
   cd DNA-Nucleotide-Count-Web-App
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run DNA-Nucleotide-Count-Web-App.py
   ```

5. Open the app in your web browser at `http://localhost:8501`.

---

## Example

### Input

```text
DNA> Query
GACATGGGAGGGGGTTTTAAAAGGTTTAAAACCCCCGACATGGGAGGGGGTTTTAAAAGGTTTAAAACCCCCGAC
ATGGGAGGGGGTTTTAAAAGGTTTAAAACCCCC
```

### Output

1. **Dictionary**:

   ```python
   {'A': 20, 'T': 20, 'G': 21, 'C': 19}
   ```

2. **Text**:

   - There are 20 adenine (A).
   - There are 20 thymine (T).
   - There are 21 guanine (G).
   - There are 19 cytosine (C).

3. **Bar Chart**:
   A bar chart visualizing the nucleotide counts.

---

## Contributing

If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add feature-name'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Acknowledgments

- **Streamlit**: For providing a simple and efficient framework for building web apps.
- **Altair**: For creating beautiful data visualizations.
- **Pillow**: For handling image processing.

Developed by Muhammad Rasoul Sahibzadah.

