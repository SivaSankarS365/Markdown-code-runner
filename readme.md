# Markdown Code Runner

Markdown Code Runner is a tool designed for processing Markdown files with executable code blocks. It automatically executes these blocks and inserts the output into the Markdown file, making it ideal for note-taking and documentation purposes. This tool supports custom inputs, runtime measurement, and caching mechanisms.

## Features

![Parse and run code in markdown files](assets/imgs/demo1.png)

![Supports custom predefined inputs or inputs from stdio](assets/imgs/demo2.png)

![Supports runtime measurement](assets/imgs/timeit.jpeg)

- **Execute Code Blocks**: Automatically runs code within Markdown files and inserts the output.
- **Custom Inputs**: Supports predefined inputs or inputs from standard I/O.
- **Runtime Measurement**: Measures and displays runtime statistics for code blocks.
- **Cache Control**: Allows selective caching of outputs to avoid rerunning code blocks unnecessarily.

> Supported Langauges: `C,C++,Python`

## Installation

Markdown Code Runner supports macOS, Linux, and Windows Subsystem for Linux (WSL).

### 1. **Install Dependencies**

Ensure that you have `python3`, `pip`, and `g++` installed. If not, follow the instructions below for your platform:

#### **On macOS:**

1. **Install Homebrew** (if you don’t have it):

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install `python3` and `g++`**:

   ```bash
   brew install python
   brew install gcc
   ```

3. **Install `pip`** (if not already installed):

   ```bash
   python3 -m ensurepip --upgrade
   ```

#### **On Linux (Debian/Ubuntu):**

1. **Update package lists**:

   ```bash
   sudo apt-get update
   ```

2. **Install `python3`, `pip`, and `g++`**:

   ```bash
   sudo apt-get install -y python3 python3-pip g++
   ```

#### **On Windows Subsystem for Linux (WSL):**

1. **Update package lists**:

   ```bash
   sudo apt-get update
   ```

2. **Install `python3`, `pip`, and `g++`**:

   ```bash
   sudo apt-get install -y python3 python3-pip g++
   ```

### 2. **Install the Markdown Code Runner Package**

After installing the dependencies, install the Markdown Code Runner package via `pip`:

```bash
pip install mdcoderunner
```

### 3. **Configure Paths**

You may need to specify the paths for `python3` and `g++` in the configuration:

1. **Edit `config.py`** (located in the package directory) to specify the paths:

   ```python
   # config.py

   PYTHON_LOCATION = 'python3'  # Adjust this path if necessary
   GPP_LOCATION = 'g++'          # Adjust this path if necessary
   ```

   - Replace the paths with the correct locations of `python3` and `g++` on your system.
   - On macOS and Linux, you can typically find the paths using `which python3` and `which g++`.


## Definitions

### Code Blocks

A code block in Markdown Code Runner consists of three components: code, input, and output.

#### Example Code Block

````
<codeStart/>

```python
a = input()
print("hello world", a)
```

```input
Siva
```

```output
hello world Siva
```

<codeEnd/>
````

### Special Elements

- **`<codeStart/>`**: Marks the beginning of a code block.
- **`<codeEnd/>`**: Marks the end of a code block.

#### Skipping Code Blocks

To skip a code block during execution, add the `skip` class:

```
<codeStart class="skip"/>
...
<codeEnd/>
```

#### Avoiding Cache

To force a code block to rerun every time without caching the output, use the `nocache` class:

```
<codeStart class="nocache"/>
...
<codeEnd/>
```

#### Runtime Measurement

To measure runtime statistics for a code block, use the `timeit` class in conjunction with `nocache`:

```
<codeStart class="timeit nocache"/>
...
<codeEnd/>
```

## Usage

```bash
usage: mdcoderunner.py [-h] [--clear-outputs] [--create-code-tags] [--clear-code-tags] input_path [output_path]

Process a Markdown file with executable code blocks.

positional arguments:
  input_path          Path to the input Markdown file.
  output_path         Path to the output Markdown file (optional). If not provided, the input file will be
                      overwritten.

optional arguments:
  -h, --help          Show this help message and exit.
  --clear-outputs     Clear all code outputs in the Markdown file.
  --create-code-tags  Wrap code blocks in <codeStart/> and <codeEnd/> tags.
  --clear-code-tags   Remove <codeStart/> and <codeEnd/> tags from code blocks.
```

## Example Usage

To process a Markdown file, run the following commands:

```bash
mdcoderunner ./assets/hello_world.md ./assets/hello_world_rendered.md
```

```bash
mdcoderunner ./assets/demo.md ./assets/demo_rendered.md
```

## Inspiration

Markdown Code Runner was developed as a tool for preparing for technical interviews, particularly for learning Data Structures and Algorithms (DSA). The goal was to create a lightweight, non-interactive alternative to Jupyter notebooks, enabling seamless note-taking and code execution within Markdown files. This project was built in a single day of focused development. This project supports C, C++ and Python code execution from the same markdown file!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
