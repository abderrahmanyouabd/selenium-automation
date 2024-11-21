import subprocess

def run_tests_in_order():
    # Run registration tests first
    print("Running registration tests...")
    subprocess.run(["behave", "--tags", "@run_first"], check=True)

    # Run login tests next
    print("Running login tests...")
    subprocess.run(["behave", "--tags", "@run_second"], check=True)

if __name__ == "__main__":
    run_tests_in_order()
