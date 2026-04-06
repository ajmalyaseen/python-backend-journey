class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def __enter__(self):
        print(f"Connecting to {self.db_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.db_name}")
        if exc_type:
          print(f" Error was: {exc_val}")

with DatabaseConnection("mydb") as db:
    print(" Running queries...")
    raise Exception("Something went wrong!")
    print("This never runs")

from contextlib import contextmanager

@contextmanager
def database_connection(db_name):
    print(f"Connecting to {db_name}")
    yield                    # ← everything before = __enter__
    print(f" Closing {db_name}")  # ← everything after = __exit__

with database_connection("mydb") as db:
    print(" Running queries...")