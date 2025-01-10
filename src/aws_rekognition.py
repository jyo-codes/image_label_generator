
import boto3
import json
import os

def analyze_images(bucket_name, images_folder, output_folder):
    """
    Analyze images in the given S3 bucket using AWS Rekognition.

    Parameters:
    bucket_name (str): Name of the S3 bucket.
    images_folder (str): Local folder containing images.
    output_folder (str): Folder to save the output JSON files.

    Returns:
    None
    """
    client = boto3.client('rekognition')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for image_name in os.listdir(images_folder):
        if image_name.endswith(('.jpg', '.png', '.jpeg')):
            image_path = os.path.join(images_folder, image_name)
            with open(image_path, 'rb') as image_file:
                response = client.detect_labels(
                    Image={'Bytes': image_file.read()},
                    MaxLabels=50
                )

            annotated_data = {
                'image': image_name,
                'labels': response['Labels']
            }

            with open(os.path.join(output_folder, f"{image_name}.json"), 'w') as f:
                json.dump(annotated_data, f, indent=4)

            print(f"Processed {image_name}")