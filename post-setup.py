"""Copyright (c) 2022 Juraj Zelman"""

import os
import shutil
from pathlib import Path

import click


def postSetup():
    print("---RUNNING POST-SETUP!---")

    local_path = os.path.join(os.getcwd())
    install_path = click.get_app_dir("githubber", roaming=True)
    install_path_config = os.path.join(install_path, "config")
    install_path_sample = os.path.join(install_path, "sample-files")

    # Create app directories
    Path(install_path_config).mkdir(parents=True, exist_ok=True)
    Path(install_path_sample).mkdir(parents=True, exist_ok=True)

    # Copy sample files
    for subdir, _, files in os.walk(os.path.join(local_path, "sample-files")):
        for file in files:
            file_target_path = os.path.join(install_path_sample, file)
            if os.path.exists(file_target_path):
                print(f"File already exists: {file_target_path}")
            else:
                shutil.copy(os.path.join(subdir, file), file_target_path)
                print(f"Copied: {file_target_path}")

    # Copy config file
    file_target_path = os.path.join(install_path_config, "account.json")
    if os.path.exists(file_target_path):
        print(f"File already exists: {file_target_path}")
    else:
        shutil.copy(
            os.path.join(local_path, "account.json"),
            file_target_path,
        )
        print(f"Copied: {file_target_path}")

    print("---POST-SETUP COMPLETED!---")


if __name__ == "__main__":
    postSetup()
