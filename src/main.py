from scripts.read_file import read_csv_file
from scripts.clean_data import clean_data
from scripts.inspect_data import inspect_data
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load the data
df = read_csv_file()

# Clean the data
df = clean_data(df, ["Comments"])

# Inspect data
df = inspect_data(df, ["GHI", "DNI", "DHI", "ModA", "ModB", "WS", "WSgust"])
