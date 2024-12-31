# Merged Network Port Prefix Project

This project merges multiple JSON files containing network port prefixes into a single JSON file. The project is set up to run automatically using GitHub Actions.

## Project Structure

```
.github/
    workflows/
        merge-json.yml
LICENSE
merged_network_port_prefix.json
port-lists/
    evm.json
port-lists-external/
    external.json
scripts/
    merge-json.py
```

### Files and Directories

- **.github/workflows/merge-json.yml**: GitHub Actions workflow file to automate the merging process.
- **LICENSE**: The MIT License file.
- **merged_network_port_prefix.json**: The output file containing the merged network port prefixes.
- **port-lists/**: Directory containing JSON files to be merged.
  - **evm.json**: An example JSON file in the port-lists directory.
- **port-lists-external/**: Directory containing JSON files with external URLs.
  - **external.json**: JSON file containing a list of external URLs to fetch additional JSON data.
- **scripts/**: Directory containing the Python script for merging JSON files.
  - **merge-json.py**: Python script to merge JSON files from port-lists and external URLs.

## How It Works

1. The GitHub Actions workflow (`merge-json.yml`) is triggered on every push to the `main` branch and on a daily schedule.
2. The workflow sets up a Python environment and installs the necessary dependencies.
3. The merge-json.py script is executed to merge JSON files from the port-lists directory and external URLs listed in external.json.
4. The merged data is saved to merged_network_port_prefix.json.
5. The changes are committed and pushed back to the repository.

## Contributing

To contribute by adding networks to the list, follow these steps:

1. **Fork the repository**: Click the "Fork" button at the top right of this page to create a copy of this repository in your GitHub account.

2. **Clone your fork**: Clone your forked repository to your local machine.
    ```sh
    git clone https://github.com/your-username/port-prefix-merge.git
    cd port-prefix-merge
    ```

3. **Create a new branch**: Create a new branch for your changes.
    ```sh
    git checkout -b add-new-network
    ```

4. **Add your network**:
    - If you are adding a network to an existing JSON file in the port-lists directory, open the appropriate file and add your network in the format:
        ```json
        "network_name": port_number
        ```
    - If you are adding a new JSON file, create a new file in the port-lists directory and add your networks in the format:
        ```json
        {
            "network_name": port_number,
            "another_network": another_port_number
        }
        ```

5. **Commit your changes**: Commit your changes with a descriptive message.
    ```sh
    git add .
    git commit -m "Add new network to port-lists"
    ```

6. **Push your changes**: Push your changes to your forked repository.
    ```sh
    git push origin add-new-network
    ```

7. **Create a Pull Request**: Go to the original repository and create a pull request from your forked repository. Provide a clear description of the changes you made.

## License

This project is licensed under the MIT License. See the 

LICENSE file for details.