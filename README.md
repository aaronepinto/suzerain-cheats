# Suzerain Cheats: Save File Modifier

This tool allows you to modify specific game save files for the game Suzerain, automating changes to certain game variables to enhance your gaming experience.

## Prerequisites

- Python 3.6 or higher installed on your machine.  You can download Python from [python.org](https://www.python.org/downloads/).
- Text editor to edit JSON files.

## Installation

1. **Clone the Repository**: First, you need to clone this repository to your local machine. Open a terminal or command prompt and run the following command:

    ```bash
    git clone https://github.com/aaronepinto/suzerain-cheats.git
    cd suzerain-cheats
    ```
2. **Modify Keys to Modify:**
Open `keys_to_modify.json` in a text editor to change values or add new key-value pairs for variables you want to modify.

## Running the Script

To run the script, you will navigate to the repository directory in your command line tool and execute the following command. Note that the command to run Python can vary by operating system; it is often `python3` on macOS and Linux:

### On Windows
```bash
python cheat.py
```

### On macOS and Linux
```bash
python3 cheat.py
```

## Troubleshooting

- Ensure Python is correctly installed by running `python --version` or `python3 --version` in your terminal.
- If you encounter permissions errors, ensure that you have read and write access to the save file directory.
- If the script does not find the save files, confirm the `SAVE_FILE_DIR` path in `cheat.py` is correctly set according to your installation of the game.

## Contributing

Contributions are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This script is released under the MIT License. See [LICENSE](LICENSE) for more information.