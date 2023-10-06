import os

# Path to the requirements.txt file
requirements_file = 'requirements.txt'

# Check if the requirements.txt file exists
if os.path.exists(requirements_file):
    # Run pip to install the packages listed in requirements.txt
    os.system(f'pip install -r {requirements_file}')
    print("Requirements installed successfully.")
else:
    print(f"The {requirements_file} file does not exist.")
