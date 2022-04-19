# iomete-pyhive-example

Example project to show how to connect to the iomete lakehouse cluster and run any SQL statements using PyHive


### How to Run

Initialize project by running following commands
```bash
python3 -m virtualenv .env;
source .env/bin/activate;

pip install -r requirements.txt
```

To run application use
```bash
python main.py
```

Note that you will need to change connection properties in `connection.py` file