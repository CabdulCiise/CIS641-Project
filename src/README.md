# Run Instructions

To set up a virtual environment, navigate to the project src folder on your terminal and type the following command:

```bash
python -m venv .venv
```

This will create a new virtual environment named .venv. Next, you need to activate the virtual environment by sourcing the activation script:

```bash
.venv/scripts/activate
```

After executing this command, your prompt will change to indicate that you’re now operating from within the virtual environment. After you successfully set up and activated your virtual environment, then run the following to install all packages:

```bash
pip install -r requirements.txt
```

Then run either the console app by running

```bash
python ./console.py
```

or the UI and API by running

```bash
npm install
npm run dev
```

and 

```bash
flask run --port=5000 --debug
```