import subprocess, platform
if platform.system() == 'Windows':
    print("Setting up virtual environment...\n")
    subprocess.run(['python', '-m', 'venv', '.venv'])
    print("Installing required packages...\n")
    subprocess.run(['.venv\\Scripts\\pip', 'install', '-r', 'requirements.txt'])
    subprocess.run(['mkdir', 'media'])
else:
    print("Setting up virtual environment...\n")
    subprocess.run(['python3', '-m', 'venv', '.venv'])
    print("Installing required packages...\n")
    subprocess.run(['.venv/bin/pip', 'install', '-r', 'requirements.txt'])
    subprocess.run(['mkdir', 'media'])
    subprocess.run(['python', 'manage.py', 'createsuperuser', '--email', 'atticus.falkner.walton@gmail.com', '--username', 'admin'], input=['admin', 'admin', 'Y'])
print("\n\nSetup complete. To activate the virtual environment, run 'source .venv/bin/activate'.")


