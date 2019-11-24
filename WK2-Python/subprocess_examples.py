import shlex, subprocess


subprocess.call(["ls", "-l"])
print(subprocess.check_output(["echo", "Hello World!"]))
command_line = input()
args = shlex.split(command_line)
print(args)
p = subprocess.Popen(args)

res = subprocess.Popen("sleep 15;echo 'hello'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(res.pid)
print(res.poll())
# Uncomment the following line and rerun the code, tell us what has happened?
# res.terminate()
print(res.stdout.read())
print(res.poll())
print(res.stderr.read())