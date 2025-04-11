import subprocess

def apply_rule(protocol, port, action):
    command = ["iptables", "-A", "INPUT", "-p", protocol, "--dport", port, "-j", action]
    subprocess.run(command)
