**Overview**: Quick documentation (with UI) is a Python application that automates the process of generating documentation for projects by leveraging AI-powered language models. It offers a user-friendly graphical interface to input project information, select languages, and choose AI models for optimal results.

**Features**:
- Supports multiple programming languages and AI models
- Easily integrates with Git for version control
- Quick generation of project documentation
- Customizable prompts for tailored documentation
- Provides a graphical user interface for easy input and monitoring

**Structure**:
- The project consists of two main Python modules: the backend (main) and the frontend (GUI).
- The backend_module logic resides in the `backend.py` file, handling the crucial tasks of the application. It includes classes such as `AutoDock` and `DataHandler`.
- The frontend_module contains the user interface, mainly defined in the `GUI` folder, including HTML (`index.html`), CSS (`style.css`), and JavaScript (`script.js`) files to interact with users.

**Usage**:
1. To run the application, execute the backend script, e.g., `python backend.py`.
2. Open the provided HTML file in a web browser (e.g., through the file:/// URL).
3. Fill in the required input fields, such as project name, path, and ignore files.
4. Specify additional preferences such as languages, prompts, and AI model versions.
5. Click the "Gen doc" button to initiate the documentation generation process.

The application will use the specified AI model to generate project documentation and save the output in a suitable format (e.g., markdown files, README.md).

Note: Please ensure that the AI model and any necessary dependencies are installed and properly configured in the project before running the application.
# backend.py Documentation

## Usage

To use the `backend.py` file, you first need to create an instance of the `AutoDock` class by providing the necessary parameters. Then, call the `gen_doc()` method on the instance to generate the documentation for your project.

```python
from quick_doc_py.main import worker
from quick_doc_py.config import LANGUAGE_TYPE, GPT_MODELS
from quick_doc_py.providers_test import provider_test

from backend import AutoDock

# Set root directory, name of project, ignore patterns, and languages
root_dir = "C:/Users/sinic/Python_Project/Quick-doc-py UI/"
name = "Test Project UI"
ignore = [".venv"]
languages = ["en"]

# Get active providers for a specific GPT version
gpt_version = "gpt-3.5-turbo"
providers = DataHandler().get_active_providers(gpt_version)

# Get a list of supported languages
supported_languages = DataHandler().support_languages()

# Get a list of supported GPT versions
supported_versions = DataHandler().support_versions()

# Create an instance of the AutoDock class with the required parameters
ad = AutoDock(name_project=name, root_dir=root_dir, ignore=ignore, languages=languages)

# Generate the documentation using the gen_doc() method
ad.gen_doc()
```

## Methods

### AutoDock class

The `AutoDock` class is used to generate the documentation for a given project. Here are its methods:

- `__init__(...):` This is the constructor method for the `AutoDock` class. It initializes the object with the given project name, ignore patterns, root directory, languages, and additional options such as GPT version, provider, general prompt, and default prompt.

- `gen_doc():` This method is used to generate the documentation for the project. It parses the given arguments using `argparse`, and then calls the `worker` function from the `main` module in the `quick-doc-py` package to generate the documentation using the selected GPT version, provider, and prompts.

### DataHandler class

The `DataHandler` class provides helper methods for getting available providers, supported languages, and GPT versions. Here are its methods:

- `get_active_providers(gpt_version: str):` This method returns a list of available providers for the given GPT version.

- `support_languages():` This method returns a list of supported languages.

- `support_versions():` This method returns a list of supported GPT versions.

By using these methods, you can create documentation for your projects efficiently and with ease.
# QuickDocPy UI Documentation

This document aims to describe the usage and methods of the `index.html` file for the QuickDocPy UI.

## Usage

The `index.html` file serves as the main user interface for the QuickDocPy application. It allows the user to input the necessary details for generating documentation.

### Input Sections

- **Name of project**: A text field where the user can input the name of their Python project. This information is later used to generate documentation content.
- **Project path**: A text field where the user can input the project's path. This is required for QuickDocPy to access the project's files and folders.
- **Ignore file**: A text field where the user can input the name of a file (or multiple files separated by commas) that should be ignored during documentation generation.
- **General prompt**: A text field where the user can enter a specific prompt that will be used for the documentation generation process.
- **Default prompt**: A text field where the user can enter a default prompt to be used if no specific general prompt is provided.

### Language Selection

- A dynamic section to display the list of available languages for documentation generation. Upon selecting a language, a tick mark appears to indicate that it has been chosen for the project.

### GPT Version Selection

- A dropdown menu where users can select a specific version of the GPT (Generative Pretraining Technology) to be used during documentation generation.

### Generate Documentation Button

- A button labeled "Gen doc" that is enabled once all required fields have been filled out by the user. When clicked, an asynchronous JavaScript function `gen_doc()` is called, initiating the documentation generation process.

## Methods

- `gen_doc()`: A function that, when triggered by the "Gen doc" button, initiates the documentation generation process with the provided inputs and user-selected settings in the user interface.

This documentation provides a brief overview of the `index.html` file's usage and methods, enabling further understanding of the interactive capabilities of the QuickDocPy UI application.
# script.js

This file contains a JavaScript code for a GUI application. It includes methods and functions for getting information, displaying languages and versions, and generating documentation. The code is structured using Google's JavaScript Style Guide best practices.

## Usage

This file is intended to interact with Python scripts for generating documentation and displaying information through the `eel` library.

### Methods

1. `window.onload = function ()`

   - This function is executed when the HTML page finishes loading.
   - It sets the window size to 500 width and 800 height.
   - Calls the `getInfo()` function to retrieve information about languages and versions.
   - Logs the languages and versions to the console.

2. `async function getInfo()`

   - An async function that retrieves the documentation information by calling the `eel.get_info()` function asynchronously.
   - Logs the retrieved data to the console.
   - Displays languages and versions from the output.
   - Calls the `add_languages()` function to populate a UI element with the available languages.
   - Calls the `add_gpt()` function to populate a UI element with the available GPT versions.

3. `function add_languages(langs)`

   - Takes a list of languages as input and populates a UI element with checkboxes.
   - Creates a new `<div>` element with the class name "language" for each language.
   - Adds the language name and checkbox to the "language" element.
   - Displays these elements inside a parent element with the class name "left" and the class "input".
   - Enables users to select their desired languages.

4. `function add_gpt(gpt_vesions)`

   - Takes a list of GPT versions as input and populates a UI element with dropdown options.
   - Creates a new `<option>` element for each GPT version and sets its value and text.
   - Adds these `<option>` elements inside a parent element with the class name "right" and the class "input".
   - Enables users to choose a GPT version from the dropdown.

5. `function gen_doc()`

   - Gathers input values from the user, which include project name, path, ignore items, g-prompt, d-prompt, and selected GPT version.
   - Obtains selected languages from the UI element populated by the `add_languages()` function.
   - Calls the `eel.gen_doc()` function with the input values and languages.

6. `function get_lang()`

   - Retrieves the checkbox inputs on UI elements with class names "tick", "language", and "left" inside the "input" element.
   - Filters checked inputs (languages) and returns them in an array.

*Note: This file assumes the existence of an `eel` library for Python-to-JavaScript interactions and relevant HTML elements for rendering the GUI.*
# visual.py

This file is part of the Quick-doc-py UI project that uses Electron [Electron](https://www.electronjs.org/) to render a web-based GUI to quickly generate project documentation using Google's AutoML APIs.

The `visual.py` file contains methods exposed to the GUI for interacting with the backend (specifically `backend.DataHandler` and `backend.AutoDock` classes) for fetching language and version data, as well as generating project documentation.

## Usage

1. **Preparation**: Install dependencies and initialize the Electron environment.
2. **Launch the App**: Run the `visual.py` file and open the app in a browser by navigating to the specified address (e.g. `http://127.0.0.1:809/`). 

## Methods

### `get_info()`
_Gets supported languages and versions for documentation generation._

#### Arguments
No arguments.

#### Return
A dictionary named `data` with two keys: `"languages"` (a list of supported languages) and `"versions"` (a list of supported versions).

### `gen_doc(name: str, root_dir: str, ignore: list[str], languages: list[str], g_prompt: str, d_prompt: str, version: str)`
_Generates project documentation using the provided project information and AutoML parameters._

#### Arguments
- `name` (str): Name of the project to generate documentation for.
- `root_dir` (str): Root directory of the project.
- `ignore` (list[str]): List of file paths or patterns to ignore when scanning project files.
- `languages` (list[str]): List of supported languages for documentation.
- `g_prompt` (str): Prompt for general information (used by AutoML).
- `d_prompt` (str): Prompt for documentation generation (used by AutoML).
- `version` (str): Version of the Google's AI model to use.

#### Returns
No return value.

### Example
```python
from visual import get_info, gen_doc

# Fetch available languages and versions
doc_data = get_info()

# Generate documentation with specified project details
gen_doc(
    name="TestProject",
    root_dir="/path/to/project",
    ignore=["README.md", "*.txt"],
    languages=doc_data["languages"],
    g_prompt="General prompt for project details",
    d_prompt="Documentation generation prompt",
    version="recent"
)
```
