# K5412598_project_code
The supporting code and python files for the EMA Project for Jaden Walker K5412598

## Setup instructions 

I would reccomend simply cloning this repository to yoru local machine to ensure the file structures are created correctly. 

It is important to make use of a virtual environment as specfic version numbers of libraries are used. The following instructions are based on a windows machine, UNIX based operating systems will differ. 

1. Generating a virtual environment<br>
    The below command will setup a virtual enviornment in the current working directory called 'venv' the remaining instructions will be based on the name 'venv' being used.<br>
    ```python -m venv venv```<br>

2. Activate the virtual environment<br>
    To activate the virtual environment on windows, start a terminal session from the root of the project directory and run the below: <br>
    ```.\venv\Scripts\activate ```<br>
    Confirm the virtual environment is active by observing the presence of ```(venv)``` at the start of the terminal line. 

3. Install required libraries<br>
    The ```requirements.txt``` file in the root project directory contains a list of libraries and version numbers needed to run the project code. To install from this file: <br>
    ```pip install -r requirements.txt```

## File structure

The main method in the library is the ```orchestration.py``` file which adds a layer of abstraction for the user in order to simplify the process requiring only two arguments: the input .pdf path and the output path where to save the new .pdf file. 

The ```photpackTools.py``` file is used to deconstruct the input .pdf and extract images to be scanned, the methods in this library will also re-insert the scanned (and blurred) images into the .pdf retaining the original structure and saving to the passed output .pdf path. 

The ```faceBlur.py``` file accepts the path to an individual image which will be passed through the scanner using the model ```best.pt``` trained for this scenario. If a face is detected, the bounding-box coordinates for the region will be provided and a blur will be inserted into the image on the region to blur out the face before the image is saved. 

## Blurring faces in a .pdf file

To run a .pdf file through the scanner, the ```orchestration.py``` file should be called from the command line (ensuring the virutal enviroment is active) with the input and output file paths as seperate arguments. e.g. <br>
```python orchestration.py -i ./test_face.pdf -o ./testing_output.pdf```

The ```test_face.pdf``` file is an example .pdf which includes images of a variety of human faces and is included within the repository for demonstration. 

There is also a ```./test_case/``` directory which contains examples of home reports which aids evaluation of the project in terms of the scope outlined in the report. 