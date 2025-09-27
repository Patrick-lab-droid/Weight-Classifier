Weight Classification App ⚖️🧑‍⚕️ — A machine learning project that classifies obesity levels (NObeyesdad) based on demographic, lifestyle, and health factors such as age, gender, diet habits, physical activity, and family history. The model is deployed with FastAPI for serving predictions through API endpoints, and locally uses Streamlit for an interactive web interface where users can input their data and instantly see classification results. This project showcases the end-to-end pipeline of ML model training, deployment, and user-friendly visualization for health insights and predictive analytics.

To run this Streamlit app locally, you can follow these instructions: 
1. Go to the folder where you store all the downlaoded files in this repo
2. Go to the address bar and time cmd then code .
3. Start up the API using the CLI in VS Code (ctrl+`) to show the CLI
4. Run this line "uvicorn deploy:app --reload" wait till it says application startup complete
5. Then open a new CLI; you can use the + button on the bottom right (don't close the FastAPI CLI)
6. Then run "streamlit run app.py"
