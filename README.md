# Mini-Project_Harga-Rumah-di-Tangerang
Learning loGic looping dan conditional

This commit implements a complete system for predicting house prices based on similarity of attributes.

Main components and workflow:

1. Data Loading
   - Load raw house price data from an external URL (harga_rumah.txt) using requests and CSV parsing.
   - Convert raw data rows into a list of dictionaries for easier attribute-based access.

2. Attribute Extraction and Analysis
   - Implement functions to extract all values of a specific attribute from the dataset.
   - Find minimum and maximum values per attribute to facilitate normalization.

3. Data Normalization
   - Define a transformation function to scale attribute values between 0 and 1 using min-max normalization.
   - Apply normalization to all numeric attributes in the dataset, updating the dataset in place.
   - Store min and max values per attribute in a dictionary (`attr_info`) for later use.

4. Input Data Transformation
   - Normalize new input data using the same min-max scale derived from the dataset, ensuring consistent comparison.

5. Similarity-Based Price Prediction
   - Compute similarity between the new input data and each data point in the normalized dataset.
   - Similarity measured by sum of absolute differences across selected attributes.
   - Predict house price as the price of the most similar data point (minimum attribute difference).

6. Output
   - Display the predicted house price based on the nearest neighbor in attribute space.

This design enables a simple but effective K-Nearest Neighbor (KNN)-style approach without explicit machine learning models, leveraging data normalization and attribute-based similarity.

The code is modularized into functions for clarity and reusability, and handles data ingestion, transformation, and prediction in discrete steps.
