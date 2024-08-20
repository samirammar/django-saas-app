from pathlib import Path
import requests

def download_to_local(url:str, out_path:Path, parent_makedir:bool=True):
    if not isinstance(out_path, Path):
        raise ValueError(f"{out_path} must be a valid pathlib Path object.")
    if parent_makedir:
        out_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        res = requests.get(url)
        res.raise_for_status()

        out_path.write_bytes(res.content)

        return True
    except requests.RequestException as err:
        print(f"Failed to download {url}: {err}")
        return False