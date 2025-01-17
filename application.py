# Import necessary libraries
from flask import Flask, request, render_template, jsonify  # Flask modules for web app functionality
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline  # Custom classes for data handling and prediction

# Initialize the Flask application
application = Flask(__name__)  # Create a Flask application instance

# Alias for the Flask app instance
app = application

# Define a route for the home page
@app.route('/')
def home_page():
    """
    Route for the home page.
    Renders the 'index.html' template.
    """
    return render_template('index.html')  # Serve the homepage template

# Define a route for the prediction page
@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    """
    Route to handle data input and prediction.
    Supports both GET and POST requests.
    """
    if request.method == 'GET':
        # Render the input form for GET requests
        return render_template('form.html')
    else:
        # Process the form data for POST requests
        data = CustomData(
            carat=float(request.form.get('carat')),  # Retrieve and convert 'carat' input to float
            depth=float(request.form.get('depth')),  # Retrieve and convert 'depth' input to float
            table=float(request.form.get('table')),  # Retrieve and convert 'table' input to float
            x=float(request.form.get('x')),  # Retrieve and convert 'x' input to float
            y=float(request.form.get('y')),  # Retrieve and convert 'y' input to float
            z=float(request.form.get('z')),  # Retrieve and convert 'z' input to float
            cut=request.form.get('cut'),  # Retrieve 'cut' input (string)
            color=request.form.get('color'),  # Retrieve 'color' input (string)
            clarity=request.form.get('clarity')  # Retrieve 'clarity' input (string)
        )
        
        # Convert the custom data into a Pandas DataFrame
        final_new_data = data.get_data_as_dataframe()
        
        # Initialize the prediction pipeline
        predict_pipeline = PredictPipeline()
        
        # Predict using the input data
        pred = predict_pipeline.predict(final_new_data)
        
        # Round off the prediction result to 2 decimal places
        results = round(pred[0], 2)
        
        # Render the form template with the prediction result
        return render_template('form.html', final_result=results)

# Run the application
if __name__ == "__main__":
    # Run the Flask application on host '0.0.0.0' (accessible from all devices in the network)
    # Enable debug mode for live error tracking during development
    app.run(host='0.0.0.0', debug=True)