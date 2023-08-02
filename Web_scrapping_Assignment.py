from bs4 import BeautifulSoup
import csv
import json
import os
import requests

# Method that extracts the bird species from the website

def birdspecies():
    # Replace with the website URL containing bird species data
    url = 'https://xeno-canto.org/collection/species/latest'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Implement web scraping inorder to extract bird species data
        bird_species = soup.find_all('table', class_='results')
        species_data = []
        for bird_table in bird_species:
            common_names = bird_table.find_all(
                'span', class_='common-name')
            sci_names = bird_table.find_all(
                'span', class_='sci-name')
            for common_name, sci_name in zip(common_names, sci_names):
                species_data.append(
                    {'common_name': common_name.text.strip(), 'sci_name': sci_name.text.strip()})
        return species_data
    else:
        print('Failed to fetch data from the website.')
        return []

# Function to generate CSV file

def create_csv_file(data):
    csv_filename = 'mybirdspecies.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['common_name', 'sci_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Function to generate JSON file

def create_json_file(data):
    json_filename = 'mybirdspecies.json'
    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    csv_filename = 'mybirdspecies.csv'
    json_filename = 'mybirdspecies.json'

    # Check if CSV and JSON files already exist
    if os.path.exists(csv_filename) and os.path.exists(json_filename):
        print("Files already exist.")
    else:
        bird_species_data = birdspecies()
        if bird_species_data:
            create_csv_file(bird_species_data)
            create_json_file(bird_species_data)
            print('CSV and JSON files generated successfully.')