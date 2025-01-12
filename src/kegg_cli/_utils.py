from os import getcwd
from datetime import datetime

def get_random_file_name_current(ext: str) -> str:
    """
    generates a file name with the given ext parameter in the current working dir
    """
    now = datetime.now()
    date_time = now.strftime("%H%M_%d%m%Y")
    path = getcwd()
    path = f"{path}/{date_time}.{ext}"
    return path


def combine_ids(ids:list[str]) -> list[str]:
    combined_list = [
                    "+".join(ids[i:i + 10]) 
                    for i in range(0, len(ids), 10)
                        ]
    return combined_list


def file_to_list(file:str) -> list[str]:
    try:
        with open(file, 'r') as f:
            gene_ids = [line.split('\t')[1].strip() for line in f]
        return gene_ids
    except FileNotFoundError:
        print(f"[red]{file} not found. Cannot proceed with gene sequence retrieval.[/red]")
        exit(1)

