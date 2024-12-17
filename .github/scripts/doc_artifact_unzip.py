import os
import zipfile

def unpack_doc_artifact(path_to_doc:str) -> str:
        for filename in os.listdir(path_to_doc):
            filepath = os.path.join(path_to_doc, filename)
            if zipfile.is_zipfile(filepath):
                with zipfile.ZipFile(filepath, 'r') as zip_ref:
                    print(f"Unpacking {filename}...")
                    zip_ref.extractall(path_to_doc)
                print(f"Removing {filename}...")
                os.remove(filepath)
            else:
                print(f"{filename} is not a ZIP file. Skipping...")
        return "Documentation has unpacked"