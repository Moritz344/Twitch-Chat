
#!/bin/bash 

if [ -z "$VIRTUAL_ENV" ]; then 
  echo "Make sure you are in a venv"
  echo "python3 -m venv venv"
  echo "source venv/bin/activate"
else
  # install requirements
  echo "Downloading reuqirements:"
  pip install -r requirements.txt
  

  python3 main.py
fi

