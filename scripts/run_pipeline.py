import subprocess
print("Starting pipeline...")
# This runs your recommendation script
subprocess.run(['python', 'recommender.py'])
print("Pipeline finished successfully!")