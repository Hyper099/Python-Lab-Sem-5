import os
import subprocess
from pathlib import Path
import platform

def backup_files(source_folder, dest_folders):
   """Backup files from source folder to multiple destination folders."""
   if not os.path.exists(source_folder):
      raise FileNotFoundError(f"Source folder '{source_folder}' does not exist!")

   print(f"Starting backup from: {source_folder}")
   processes = []

   for dest in dest_folders:
      Path(dest).mkdir(parents=True, exist_ok=True)
      print(f"Backing up to: {dest}")

      if platform.system() == "Windows":
         cmd = ["xcopy", source_folder, dest, "/E", "/I", "/Y"]
         process = subprocess.Popen(cmd, shell=False)
      else:
         cmd = ["cp", "-r", source_folder, dest]
         process = subprocess.Popen(cmd, shell=False)

      processes.append(process)

   for p in processes:
      p.wait()

   print("Backup completed successfully!")

if __name__ == "__main__":
   script_dir = os.path.dirname(os.path.abspath(__file__))
   workspace_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
   
   source = os.path.join(workspace_root, "Data")

   destinations = [
      os.path.join(workspace_root, "backup"),
      #? We can add more destinaion paths
      # os.path.join(workspace_root, "backup2"),
   ]

   backup_files(source, destinations)