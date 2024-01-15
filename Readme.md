## Sample project with frontend using streamlit and backend using FastAPI

* Create a virtual environment and activate the same
* Install the dependencies using `pip install -r requirements.txt`
* Using terminal window, `cd` into the `backend` folder and run `uvicorn main:app --reload`
    * Go to `http://127.0.0.1:8000/docs` to verify the Swagger UI for FastAPI backend
* Create a new terminal window and `cd` into the `frontend` folder and run the `streamlit run app.py` command to start the frontend
* Go to `http://localhost:8501/` to view the app
