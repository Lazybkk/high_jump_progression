# High Jump World Record Progression Analysis

This project analyzes the progression of women's high jump world records over time, using data scraped from Wikipedia and visualized with Python libraries.

## Environment

- **OS:** Windows 11
- **Python:** 3.9.0
- **Libraries:**
    - pandas
    - matplotlib

## Setup

1. **Create virtual environment:**
   ```bash
   python3 -m venv high_jump_env 


2. **Activate virtual environment:**

    ```bash
    .\high_jump_env\Scripts\activate

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt


## Usage

1. **Run the script:**
    ```
    python main.py
    ```
    This will generate a PNG file named high_jump_progression.png containing the chart.

## Data Source
The world record data is extracted from the "Record progression" table on this Wikipedia page:

https://en.wikipedia.org/wiki/Women%27s_high_jump_world_record_progression

## Project Structure

**main.py:** 

**process_data_from_url:** Fetches and cleans the data from Wikipedia.

**generate_chart:** Creates the visualization of the record progression.