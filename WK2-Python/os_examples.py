import os
import subprocess


class FolderOperation:
    def __init__(self,
                 base_dir: str,
                 suffix: str):
        self.base_dir = base_dir
        self.suffix = suffix
        self.counter = 0

    def get_files_or_folders_in_the_base_dir(self):
        return os.listdir(self.base_dir)

    def get_files(self):
        return os.walk(self.base_dir)

    def get_all_files_with_suffix_in_the_base_dir(self):
        import glob
        return glob.glob(self.base_dir + "/" + "*." + self.suffix)

    @staticmethod
    def path_join_example():
        print("1:", os.path.join('aaaa', '/bbbb', 'ccccc.txt'))
        print("2:", os.path.join('/aaaa', '/bbbb', '/ccccc.txt'))
        print("3:", os.path.join('eeee', 'dddd', 'aaaa', './bbb', 'ccccc.txt'))

    def write_file(self):
        with open('tmp_file.txt', 'w') as f:
            self.counter += 1
            f.write(f"This will overwrite the previous result {self.counter}\n")

    def append_file(self):
        with open('tmp_file.txt', 'a') as f:
            self.counter += 1
            f.write(f"This will not overwrite the previous result {self.counter}\n")

    @staticmethod
    def run_cmd(cmd):
        os.system(cmd)

    @staticmethod
    def another_way_to_run_cmd():
        subprocess.call(['df', '-h'])

    @staticmethod
    def yet_another_way_to_run_cmd():
        # Ask the user for input
        host = input("Enter a host to ping: ")

        # Set up the echo command and direct the output to a pipe
        p1 = subprocess.Popen(['ping', '-c 2', host], stdout=subprocess.PIPE)

        # Run the command
        '''
        The communicate() method returns a tuple (stdoutdata, stderrdata). 

        Popen.communicate() interacts with process: Send data to stdin.
        
        Read data from stdout and stderr, until end-of-file is reached.
        
        Wait for process to terminate.
        
        Basically, when you use communicate() it means that you want to
        execute the command
        '''
        output = p1.communicate()[0]

        print(output)


if __name__ == '__main__':
    print("-------- Current folder --------")
    current_folder_op = FolderOperation(base_dir=os.getcwd(), suffix="py")
    print(current_folder_op.get_files_or_folders_in_the_base_dir())
    print(current_folder_op.get_all_files_with_suffix_in_the_base_dir())
    print("Let us walk through the current folder")
    for result in current_folder_op.get_files():
        print(result)

    print("-------- Parent folder --------")
    parent_folder_op = FolderOperation(base_dir="../", suffix="py")
    print(parent_folder_op.get_files_or_folders_in_the_base_dir())
    print(parent_folder_op.get_all_files_with_suffix_in_the_base_dir())
    print("Let us walk through the parent folder")
    for result in parent_folder_op.get_files():
        print(result)

    print("-------- Path Join --------")
    FolderOperation.path_join_example()

    print("-------- Path Join --------")
    current_folder_op.write_file()
    current_folder_op.append_file()
    current_folder_op.write_file()

    print("-------- Run CMD --------")
    FolderOperation.run_cmd("ls")
    FolderOperation.another_way_to_run_cmd()
    FolderOperation.yet_another_way_to_run_cmd()

