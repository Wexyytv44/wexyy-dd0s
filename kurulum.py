import os

def install_packages(pip_command):
    try:
        # Install the required packages using the specified pip command
        os.system(f"{pip_command} install requests")
        os.system(f"{pip_command} install asyncio")
        os.system(f"{pip_command} install aiohttp")
        os.system(f"{pip_command} install fade")
        print("Packages installed successfully.")
    except Exception as e:
        print(f"Error during installation: {e}")

def install_dependencies():
    try:
        # Install necessary dependencies
        os.system("apt-get update")
        os.system("apt-get install -y python3 python3-pip")
    except Exception as e:
        print(f"Error during dependency installation: {e}")

def main():
    c = input("Choose your environment: [0] pip / [1] pip3 : ")

    if c == "0":
        install_dependencies()
        install_packages("pip")
    elif c == "1":
        install_dependencies()
        install_packages("pip3")
    else:
        print("Invalid choice. Please choose either 0 or 1.")

if __name__ == "__main__":
    main()
