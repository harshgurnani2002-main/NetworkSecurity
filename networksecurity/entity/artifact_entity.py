from dataclasses import dataclass


@dataclass
class DataIngestionAritfact:
    trained_file_path:str
    test_file_path:str