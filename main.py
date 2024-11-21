import subprocess
import os

def run_tests_in_order():
    # Run registration tests first
    print("Running registration tests...")
    subprocess.run(["behave", "--no-capture", "--no-skipped", rf"features{os.sep}login.feature"], check=True)

    # Run login tests next
    print("Running login tests...")
    subprocess.run(["behave", "--no-capture", "--no-skipped", rf"features{os.sep}registration.feature"], check=True)

    print("Running sauce_demo checkout tests...")
    subprocess.run(["behave", "--no-capture", "--no-skipped", rf"features{os.sep}sauce_demo.feature"], check=True)

    print("Running sauce_demo logout url tests...")
    subprocess.run(["behave", "--no-capture", "--no-skipped", rf"features{os.sep}logout.feature"], check=True)

    print("Running sauce_demo media url tests...")
    subprocess.run(["behave", "--no-capture", "--no-skipped", rf"features{os.sep}media.feature"], check=True)

    print("All tests passed!")

if __name__ == "__main__":
    run_tests_in_order()
