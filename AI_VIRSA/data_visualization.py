import os
import pandas as pd
import matplotlib.pyplot as plt
from text_to_speech_virsa import speak

DATASETS_FOLDER = r"E:\Python Project\Python AI\AI-VIRSA\AI_VIRSA\Datasets"
VISUALIZATIONS_FOLDER = r"E:\Python Project\Python AI\AI-VIRSA\AI_VIRSA\Visualizations"


def visualize_data(dataset_name):
    dataset_path = os.path.join(DATASETS_FOLDER, dataset_name)

    if not os.path.exists(dataset_path):
        speak(f"The dataset {dataset_name} does not exist.")
        return

    try:
        data = pd.read_csv(dataset_path)
        # Creating a simple visualization
        plt.figure(figsize=(10, 6))
        for column in data.columns:
            if column != "Date":
                plt.plot(data["Date"], data[column], label=column)

        plt.title(f'Data Visualization for {dataset_name}')
        plt.xlabel('Date')
        plt.ylabel('Values')
        plt.xticks(rotation=45)
        plt.legend()

        # Ensure the visualizations folder exists
        if not os.path.exists(VISUALIZATIONS_FOLDER):
            os.makedirs(VISUALIZATIONS_FOLDER)

        visualization_path = os.path.join(VISUALIZATIONS_FOLDER, f"{dataset_name}_visualization.png")
        plt.savefig(visualization_path)
        plt.close()

        speak(f"The data visualization for {dataset_name} has been created and saved at {visualization_path}.")
    except Exception as e:
        speak(f"An error occurred while creating the visualization: {e}")


if __name__ == "__main__":
    dataset_name = "sample_dataset.csv"  # Replace with your dataset
    visualize_data(dataset_name)
