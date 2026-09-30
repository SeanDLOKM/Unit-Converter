# Unit Converter
A simple **Python Flask application** that converts a selected unit and its quantity to a target unit and quantity.
It takes a CSV file, containing columns for **Source Unit**, **Target Unit** and the **Factor** associated with each conversion.
The app creates a dictionary from the conversion data provided in the CSV, effectively acting as an adjacency list where units are the nodes.
**Breadth First Search** is utilised in order to indirectly convert between units, if a direct conversion is not available but the units are connected through multiple conversions.

### Setup Instructions
1. After pulling application files, it is strongly recommended to create a **virtual environment**.<br>(e.g. ```py -m venv env```)
2. Once the virtual environment has been created, activate it.<br>(e.g. ```.\env\Scripts\Activate.ps1```)
3. Install the required packages by using ```pip install -r requirements.txt```.
4. A local development server to run the app can be started by using ```flask run```. It can be ended at any time using CTRL + C.
5. Where it says ```Running on http://...:5000```, copy and paste the link into your browser, to access the application.

### Usage Instructions
After selecting the **source unit** you want to convert to another unit, press the "Update Target Units" button to refresh the "Target Unit" options (it will filter to only show valid conversions).
Enter the quantity you would like to convert, and hit "Calculate Conversion" for the result.<br>
You can use your own CSV for unit conversions. Make sure the CSV is named ```unit_conversions.csv```, and is formatted in the following way:<br>
* Three header columns: SourceUnit, TargetUnit, Factor
* Any number of conversions and their corresponding factors in the following rows. Reverse conversions are optional as missing reverse conversions are calculated and added after the application starts.

### Disclosure on AI Usage
ChatGPT was used to assist in development of the application. Initial development was split into two parts: 
1. Python script containing functions to read the attached unit conversions CSV, followed by algorithms to find conversions for a given source and target.
2. Python flask application, providing a user interface for the Unit Converter.

ChatGPT was used to:
* Troubleshoot errors during development
* Provide sources to python documentation sites (primarily for helping implement the BFS algorithm into my solution)
* Help Integrate my converter.py script solution into my flask application (connect the functions from converter.py with the form submission from the Flask app)
* Help review my final work, remove unnecessary code (such as unused packages, etc.) and clean up before pushing to repository.

Additionally, Claude was used to generate a larger unit_conversions.csv file for testing on a larger amount of data. As the final unit conversion file is AI generated, I cannot guarantee
that all conversion factors are 100% accurate - feel free to replace with your own file.
