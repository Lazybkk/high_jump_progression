import pandas as pd
import matplotlib.pyplot as plt


def generate_chart(data: pd.DataFrame):
    # Create a line plot
    print("Generate Chart")
    plt.figure(figsize=(20, 12))  # Adjust figure size as needed
    plt.plot(data['Athlete_Year'], data['Mark'], marker='o', linestyle='-')

    plt.xticks(rotation=45, ha='right')

    # Add labels and title
    title = 'High Jump World Record Progression'
    output_format = "png"
    filename = "".join([title.replace(" ", "_"), ".", output_format])

    plt.xlabel('Athlete - Year')
    plt.ylabel('Mark (meters)')
    plt.title(title)

    # Save image with png type
    plt.savefig(filename, format=output_format, dpi=300)  # Replace with desired options


def process_data_from_url(link: str):
    print("Read data from url")
    df = pd.read_html(link)
    data = df[0]  # we get first table in source page

    # Add Year comlumn use for generate chart
    data['Year'] = pd.to_datetime(data['Date']).dt.year.astype(str)

    data['Mark'] = data['Mark'].astype(str).str.replace(r' \(.*\)', '', regex=True)  # Remove units from "Mark"
    data['Athlete_Year'] = data['Athlete'] + ' - ' + data['Year']
    return data


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Women%27s_high_jump_world_record_progression"
    data_table = process_data_from_url(url)
    generate_chart(data_table)
    print("Done!")
