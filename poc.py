import os

print("POC: attacker-controlled PR code executed")

with open("poc-proof.txt", "w") as f:
    f.write("Proof of execution from pull_request_target workflow")
