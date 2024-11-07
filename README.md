# Project Scaffold Generator

This project provides a Python script to generate a standardized repository structure for a Python project. The script creates a directory with the following structure and templates:

## Repository Structure

The scaffold will create the following directory and file structure:

```
<repo_name>/
├── config_logging.py
├── main.py
├── test_main.py
├── logs/
│   └── test/
│       ├── failure.log
│       └── summary.log
└── test/
    ├── config_test.yaml
    ├── test_cases.csv
    ├── tests_load.py
    └── test_cases.json
```

### Template Files
- `main.py`: The main Python script with a basic template for a `Solution` class.
- `config_logging.py`: A template for configuring logging, with support for failure and summary logs.
- `test_main.py`: A test file that uses `pytest` to run unit tests against the `Solution` class.
- `config_test.yaml`: A YAML configuration file containing test case settings.
- `test_cases.csv`: A CSV file to define test case data.
- `test_cases.json`: A JSON version of the test cases for flexible configuration.
- `failure.log` and `summary.log`: Log files where test results and summaries are stored.

## Usage

### Prerequisites
- Python 3.x
- `pytest` for running the tests
- `PyYAML` for handling YAML configuration

You can install the required dependencies using `pip`:

```bash
pip install pytest pyyaml
```

### Running the Scaffold Script

To generate the repository structure, simply run the `scaffold.py` script and provide the desired repository name as an argument.

1. Navigate to the directory where `scaffold.py` is located.
2. Run the script using Python:

```bash
python scaffold.py <repo_name>
```

For example, to create a repo called `my_project`, run:

```bash
python scaffold.py my_project
```

This will create a directory named `my_project` with the predefined structure and templates.

### How It Works

1. **Directory Creation**: The script creates a new directory for the repository one level above where the script is located. This directory will contain all necessary files and folders.
2. **Template Files**: The script will populate the `main.py` and `config_logging.py` files using templates stored in the `templates/` directory. Other files, like log files and configuration files, will be created as empty files (except for `test_main.py`, which includes a `pytest`-based test).
3. **Logging**: `config_logging.py` configures logging for the repository, including separate logs for failures and summaries of test results.

### Customization

You can easily modify the following parts:

- **Template Files**: Edit the templates in the `templates/` directory to adjust the content of the generated files.
- **Repository Structure**: Add or modify the files in the `structure` dictionary within the `create_repo_structure` function.

## Running Tests

After generating the repository structure, you can run tests using `pytest`:

```bash
pytest
```

This will run the tests defined in `test_main.py`, and log the results to the `failure.log` and `summary.log` files located in the `logs/test/` folder.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
