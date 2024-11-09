import os
import sys
import ssl
import urllib.request  # Changed import to use urllib

def read_template(template_path):
    """Reads and returns the content of the given template file."""
    with open(template_path, 'r') as template_file:
        return template_file.read()

def fetch_gitignore():
    """Fetches the Python .gitignore from GitHub using urllib."""
    url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
    context = ssl._create_unverified_context()  # Create an unverified SSL context
    try:
        with urllib.request.urlopen(url, context=context) as response:
            # Read and decode the content from the response
            return response.read().decode('utf-8')
    except urllib.error.URLError as e:
        raise Exception(f"Failed to fetch .gitignore file from {url}. Error: {e}")

def create_repo_structure(repo_name):
    # Get the directory of the script and move one level up
    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)

    # Define the full path for the repository one level above
    repo_path = os.path.join(parent_dir, repo_name)

    # Define the directory and file structure
    structure = {
        "": ["config_logging.py", "main.py", "test_main.py"],  # Root files
        "logs/test": ["failure.log", "summary.log"],  # Log files inside logs/test
        "test": ["config_test.yaml", "test_cases.csv", "tests_load.py", "test_cases.json"]  # Test files
    }

    # Template mapping: file names to template paths
    templates = {
        "main.py": os.path.join(base_dir, 'templates', 'main.py'),
        "config_logging.py": os.path.join(base_dir, 'templates', 'config_logging.py'),
        "test_main.py": os.path.join(base_dir, 'templates', 'test_main.py'),
        "tests_load.py": os.path.join(base_dir, 'templates', 'tests_load.py'),
        "config_test.yaml": os.path.join(base_dir, 'templates', 'config_test.yaml')
    }

    try:
        # Create the root directory for the repository
        os.makedirs(repo_path, exist_ok=True)
        print(f"Created repository folder: {repo_path}")

        # Create each folder and file based on the structure dictionary
        for folder, files in structure.items():
            # Define the full path of the current folder
            dir_path = os.path.join(repo_path, folder)
            os.makedirs(dir_path, exist_ok=True)

            # Create each file in the current folder
            for file_name in files:
                file_path = os.path.join(dir_path, file_name)
                with open(file_path, "w") as file:
                    # Check if there's a template for this file
                    if file_name in templates:
                        file.write(read_template(templates[file_name]))
                    else:
                        pass  # Just create an empty file for others
                    print(f"Created file: {file_path}")

        # Fetch and add the .gitignore file
        gitignore_content = fetch_gitignore()
        gitignore_path = os.path.join(repo_path, ".gitignore")
        with open(gitignore_path, "w") as gitignore_file:
            gitignore_file.write(gitignore_content)
        print(f"Created .gitignore from: {gitignore_path}")

        print("Repository structure created successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scaffold <repo_name>")
    else:
        repo_name = sys.argv[1]
        create_repo_structure(repo_name)
