# Multi-Project Repository
This repository contains multiple Python projects for different purposes. Each project is designed to handle specific tasks related to data analysis, image processing, and documentation.

## 1. Chart Similarity Checker
A tool to analyze and identify similar images using deep learning techniques.

### Directory Structure
```
Chart-Similarity-Checker/
├── image-sim-main/
│   ├── file/
│   │   ├── **pycache**/
│   │   ├── **init**.py
│   │   ├── check_image_similarities.py
│   │   └── img_plotter.py
│   ├── .gitignore
│   ├── main.py
│   ├── README.md
│   ├── output/
│   └── png/
```

### Usage
1. Place your images in the `png` directory
2. Run the script:
```bash
python3 -m main
```
3. Similar images will be stored in the `output` directory

## 2. Unused Import / Variable Checker
A GUI tool to analyze Python code for unused imports and variables.

### Features
- Detects unused imports using vulture
- Identifies unused columns in data dictionaries
- Tracks numpy function usage
- Provides GUI interface for results

### Usage
```bash
python unused_imports_checker.py
```

## 3. Documentation Generator
A tool to generate documentation and metadata for Jupyter notebooks.

### Features
- Creates metadata CSV files
- Creates data CSV files
- Generates one **shot go** script to paste the respectives links on the web tool we used.  

### Example Usage
```python
# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# (See provided script for full implementation)
```

## 4. NebulaNoteHarvester
A tool for processing and organizing Jupyter notebooks with Google Drive integration.

### Features
- Downloads and processes Colab notebooks
- Extracts and saves visualizations (both static and Plotly)
- Generates comprehensive metadata
- Handles data dictionary extraction
- Supports multiple plot title detection methods
- File organization and Google Drive management

### Key Components
- Authentication and Google Drive API integration
- Automatic file type detection
- Support for multiple visualization formats
- Metadata generation with detailed attributes
- Additional file dependency detection

### Usage
```python
# Initialize with Google Drive folders
image_folder_id = "your_image_folder_id"
data_folder_id = "your_data_folder_id"
metadata_folder_id = "your_metadata_folder_id"
drive_folder_id = "your_drive_folder_id"

# Process a Colab notebook
colab_link = "https://colab.research.google.com/drive/<File-ID>?usp=sharing"
notebook_name = get_colab_name(colab_id)
notebook_file = download_notebook(colab_id)
analyze_notebook(notebook_file, colab_id)
```

## Dependencies
### Core Dependencies
- Python 3.x
- NumPy
- Pandas
- Torch
- PIL
- sklearn

### Additional Dependencies
- tkinter (for GUI)
- vulture (for unused import detection)
- google-colab (for documentation generator)
- plotly (for interactive visualizations)
- googleapiclient
- base64

## Installation
Clone the repository:
```bash
git clone https://github.com/Theternos/Multimodality-Gemini.git
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact
If anything is needed or if you have any queries, contact me at **kavin.apm2003@gmail.com**