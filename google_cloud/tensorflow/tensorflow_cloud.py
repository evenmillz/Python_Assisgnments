# Import required libraries
import os
import random
from google.cloud import storage
from google.cloud import aiplatform

# Set up project and region variables
PROJECT_ID = "tensorflow-460903"
REGION = "us-central1"
BUCKET_NAME = "my-new-bucket-" + str(random.randint(1000, 9999))  # Random bucket name
CREDENTIAL_PATH = "tensorflow-460903-c068a32b2d8f.json"
DATASET_PATH = "../../csv_assignment/image_dataset.csv"

# Authenticate and set up the Google Cloud Storage client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIAL_PATH

# Create Cloud Storage bucket
def create_bucket(bucket_name):
    """Create a new bucket in Google Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)
    print(f"Bucket created: ", bucket_name)

    # bucket = storage_client.bucket(bucket_name)
    # if not bucket.exists():
    #     bucket.create(location=REGION)
    #     print(f"Bucket {bucket_name} created.")
    # else:
    #     print(f"Bucket {bucket_name} already exists.")

# Upload a dataset file to the bucket
def upload_dataset(bucket_name, dataset_path):
    """Upload a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(os.path.basename(dataset_path))

    blob.upload_from_filename(dataset_path)

    print("Dataset file uploaded to Cloud Storage")

# Create Tabular Dataset in Vertex AI
def create_tabular_dataset(bucket_name, dataset_path):
    """Create a tabular dataset in Vertex AI."""
    aiplatform.init(project=PROJECT_ID, location=REGION)

    gcs_source_uri = f"gs://{bucket_name}/{os.path.basename(dataset_path)}"
    dataset = aiplatform.TabularDataset.create(display_name="my_dataset", gcs_source=gcs_source_uri)
    print("Tabular dataset created:", dataset.display_name)

# Analyze the dataset
def analyze_dataset(bucket_name, dataset_path):
    """Analyze the dataset."""
     # This code was in the hint but is incorrect
    # It throws an error due to incorrect parameters
    # It should be aiplatform.TabularDataset.create(*parameters*)
    dataset = aiplatform.TabularDataset(
        project=PROJECT_ID,
        location=REGION,
        display_name="my_dataset",
        gcs_source=f"gs://{bucket_name}/{os.path.basename(dataset_path)}",
    )
    analysis = dataset.analyze()
    print("Dataset analysis results:")
    print(analysis)



    # This code is to compare the results of two different ways of writing the same code
    # dataset1 = aiplatform.TabularDataset.create(
    #     project=PROJECT_ID,
    #     location=REGION,
    #     display_name="my_dataset_analysis",
    #     gcs_source=f"gs://{bucket_name}/{os.path.basename(dataset_path)}",
    # )

    # analysis1 = dataset1.analyze()
    # print("Dataset1 analysis results:")
    # print(analysis1)

    # dataset2 = create_tabular_dataset(BUCKET_NAME, DATASET_PATH)
    # analysis2 = dataset2.analyze()
    # print("Dataset2 analysis results:")
    # print(analysis2)

    # if( analysis1 == analysis2 ):
    #     print("The datasets are identical.")


# Main function
def main():
    # Create a new bucket
    create_bucket(BUCKET_NAME)

    # Upload the dataset file to the bucket
    upload_dataset(BUCKET_NAME, DATASET_PATH)

    # Create a tabular dataset in Vertex AI
    create_tabular_dataset(BUCKET_NAME, DATASET_PATH)

    # Analyze a tabular dataset in Vertex AI
    analyze_dataset(BUCKET_NAME, DATASET_PATH)

# Execute the main function
if __name__ == "__main__":
    main()