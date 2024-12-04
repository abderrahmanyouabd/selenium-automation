import subprocess
import os

def run_tests_in_order():
    print("Running registration tests...")
    subprocess.run(["behave", "--no-capture", "--no-skipped", rf"features{os.sep}login.feature"], check=True)

    print("Running login tests...")
    subprocess.run(["behave", "--no-capture", "--no-skipped", rf"features{os.sep}registration.feature"], check=True)

    print("Running sauce_demo checkout tests...")
    subprocess.run(["behave", "--no-capture", "--no-skipped", rf"features{os.sep}sauce_demo.feature"], check=True)

    print("Running sauce_demo logout url tests...")
    subprocess.run(["behave", "--no-capture", "--no-skipped", rf"features{os.sep}logout.feature"], check=True)

    print("Running sauce_demo media url tests...")
    subprocess.run(["behave", "--no-capture", "--no-skipped", rf"features{os.sep}media.feature"], check=True)
    print("Running demo_blaze product addition tests...")
    subprocess.run(["behave", "--no-capture", "--no-skipped", rf"features{os.sep}product.feature"], check=True)
    print("Running demo_blaze about us opening page tests...")
    subprocess.run(["behave", "--no-capture", "--no-skipped", rf"features{os.sep}about.feature"], check=True)
    print("Running demo_blaze contact us opening page tests...")
    subprocess.run(["behave", "--no-capture", "--no-skipped", rf"features{os.sep}contact.feature"], check=True)

    print("All tests passed!")

if __name__ == "__main__":
    run_tests_in_order()
