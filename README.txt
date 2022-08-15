The following Files and Folder are made available :

VisualizationProject 
	AirBnBPredictiveModel.ipynb - Jupyter Notebook File to Perform Data Analysis, Train the XGBoost Model and Run different Experiments
	Airbnb_Final_ALL.csv - Final Data Set used in the model
	Data Scrapping: 
		Google Places Data Scrapping.ipynb - Google Colab Notebook to append nearby places data via Google Places API and median_income data to the Airbnb properties.
	GUI:
		app.py - Code to Start Flask Server, run the API Calls and use the model to predict the Occupancy Rates for user input
		XGBoost.pickle - A pickle file of the trained model (used in app.py)
		templates - HTML Files
	

We would require Anaconda and Python PIP to set up an environment to run this Project
 - install Anaconda - https://docs.anaconda.com/anaconda/install/index.html
 - install python pip - https://www.makeuseof.com/tag/install-pip-for-python/


Step 1) Setup Conda Environment:
		- Navigate to the Project Directory on Command Line
		- Please create a new Conda enviroment by running the below script on command line from the project directory 
			conda create --name testenv

Step 2) Activate the new Environment
		- Run the following on command line
			conda activate testenv

Step 3) Once in the Environment run the following commands:
 		 pip install jupyter 
 		 pip install numpy
 		 pip install pandas 
 		 pip install matplotlib
 		 pip install seaborn
 		 pip install sklearn
 		 pip install xgboost
 		 pip install Flask

Step 4) Adding the new kernel to Jupyter
		Type the following on the command line and press enter
			python -m ipykernel install --user --name testenv --display-name "Python (testenv)"
			You should see the following returned - Installed kernelspec testenv in C:\Users\gaura\AppData\Roaming\jupyter\kernels\testenv

Step 5) Start Jupyter Notebook
		Type the following from within the Env on Command Line
			jupyter notebook
		Directions on how to open the Jupyter Notebook should be returned(eg below)
			To access the notebook, open this file in a browser:
        			file:///C:/XXX/XXX/AppData/Roaming/jupyter/runtime/nbserver-54920-open.html
    				Or copy and paste one of these URLs:
        			http://localhost:8889/?token=f602cb0e56e132b8dcd88ac78143d988dc1f25cc3cbc92b2
     				or http://127.0.0.1:8889/?token=f602cb0e56e132b8dcd88ac78143d988dc1f25cc3cbc92b2
		Open the localhost link on a web browser
		You should be able to the see the Jupyter Notebook Files on the Brower ->Click on AirBnBPredictiveModel.ipynb
		Click on Kernel -> Change Kernel- > Python (testenv)

Step 6) Run the model
		Click on Kernel -> Restart & Run All (Wait for all cells to be executed)
		Once the entire file runs, one can see the Experiment Results Starting from Cell 56 Onwards
		A pickle file will also be generated of the trained XGBoost model in the GUI Folder

Step 7) Shut the Kernel
		Click on Kernel ->Shutdown
		Click on Logout
		On the command Line type Ctrl + C to Shutdown the kernel

Step 8) Start the User Interface
		- Now Navigate to GUI Directory inside AirbnbOccupancyRate Folder from the Command Line 
		- Type python app.py and press enter
		- The command line would return the server path to view the UI (Example given below)
			Running on http://localhost:9999/ (Press CTRL+C to quit)

Step 9) User Interface
		- Navigate  to http://localhost:9999/ on a Browser
		- This is the User Interface which calls the already trained model to predict Occupancy Rate for the input parameters provided by a User 
		- The UI also contains links to the Visulaizations we have created in the project. The Visualizations have been done on Public Tableau. 
		- Pleasure Capture Values in all Text Boxes of the UI

Step 10) Visualizations 
		- The Visualizations can be found in the following Public Tableau link:
			https://public.tableau.com/app/profile/fei.chi6769/viz/ProjectMars_16377166692490/LineGraphs-OccupancyRateVs_NearbyPlacesByPropertyType_1
