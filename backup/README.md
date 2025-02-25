# Pytorch Image Classifier

A web application that uses TensorFlow's MobileNetV2 model to classify images. Users can upload images and get instant predictions about what the image contains.

## Features

- Simple, intuitive web interface
- Real-time image classification
- Support for JPEG, PNG, and GIF formats
- Top 3 predictions with confidence scores
- Pre-trained model capable of recognizing 1000 different categories

## Technologies Used

- Python 3.11
- Flask
- TensorFlow (MobileNetV2)
- HTML/CSS
- JavaScript

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/image-classifier.git
cd image-classifier
```

2. Create and activate a virtual environment:

```bash
python3.11 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:

```bash
python app.py
```

2. Open a web browser and navigate to:

```
http://127.0.0.1:5000
```

3. Upload an image and click "Classify Image" to get predictions

## Project Structure

```
image-classifier/
├── app.py              # Flask application
├── requirements.txt    # Project dependencies
├── README.md          # Project documentation
├── static/            # Static files
│   └── uploads/       # Uploaded images directory
└── templates/         # HTML templates
    ├── index.html     # Upload page
    └── result.html    # Results page
```

## Well-Recognized Categories

- Animals (dogs, cats, birds)
- Vehicles (cars, bikes, boats)
- Electronics (laptops, phones)
- Household items (coffee cups, furniture)
- Food and fruits

## Tips for Best Results

- Use clear, well-lit photographs
- Center the main object in the frame
- Avoid busy backgrounds
- Any image size works (will be resized to 224x224)
- Use JPEG, PNG, or GIF formats

## License

[Your chosen license]
