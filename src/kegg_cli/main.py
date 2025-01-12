import os
import requests
import time
import typer

app = typer.Typer()

# Color codes for messages (useful for terminal output)
GREEN = '\033[0;32m'
RED = '\033[0;31m'
NC = '\033[0m'  # No Color

def success(message):
    print(f"{GREEN}{message}{NC}")

def failure(message):
    print(f"{RED}{message}{NC}")

def main():
    app()

if __name__ == "__main__":
    main()
