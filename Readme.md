# Subdomain Enumeration Tool

This tool is designed to enumerate subdomains for a given domain using a list of potential subdomains.

## Features

- Enumerates subdomains from a provided list.
- Uses `requests` to check if subdomains are valid.
- Logs results to a file.
- Provides colored output for better readability.
- Interactive menu for domain input.

## Requirements

- Python 3.x
- `requests` library
- `colorama` library

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Muhammadkafaby/subdomain-enum.git
   cd subdomain-enum
   ```

2. Install the required libraries:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Create a `subdomains.txt` file with a list of subdomains to check, one per line:

   ```plaintext
   www
   mail
   ftp
   blog
   dev
   test
   shop
   api
   ```

2. Run the tool:

   ```sh
   python subdomain-enum.py -d example.com
   ```

   Or, if you prefer to enter the domain interactively:

   ```sh
   python subdomain-enum.py
   ```

## Example

```sh
$ python subdomain-enum.py -d example.com
Valid domain: http://www.example.com
Invalid domain: http://mail.example.com
Connection error: http://ftp.example.com
Timeout error: http://blog.example.com
```
