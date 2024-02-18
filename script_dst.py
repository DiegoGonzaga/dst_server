import os
import platform
from abc import abstractmethod


def start_server(cluster):

    actual_system = platform.system()

    if actual_system == "Windows":
        dont_starter = DontStarveWindows(
            cluster,
            persistent_path=os.environ["WINDOWS_PERSISTENT_PATH"],
        )
        
    elif actual_system == "Linux":
        dont_starter = DontStarveLinux(
            cluster,
            persistent_path=os.environ["LINUX_PERSISTENT_PATH"],
        )
    else:
        raise Exception("System not cataloged")

    dont_starter.start_shard("Master")
    dont_starter.start_shard("Caves")


class DontStarveStarter:
    dedicated_server_path = None
    command_interpreter = None
    bin = "dontstarve_dedicated_server_nullrenderer_x64"

    def __init__(
        self,
        cluster,
        command_interpreter,
        shard_list: list = None,
        persistent_path=None,
    ):
        self.cluster = cluster
        self.command_interpreter = command_interpreter
        self.persistent_path = persistent_path
        if shard_list is None:
            self.shard_list = ["Master", "Caves"]

    def prepare_command(self, shard_name):
        os.chdir(self.dedicated_server_path)
        command = f"{self.bin}  -console"

        if self.persistent_path:
            command = command + f" -persistent_storage_root {self.persistent_path}"
        command = command + f" -cluster {self.cluster} -shard {shard_name}"
        return command

    @abstractmethod
    def start_shard(self, shard_name):
        command = self.prepare_command(shard_name)
        print(command)


class DontStarveWindows(DontStarveStarter):
    def __init__(
        self,
        cluster,
        command_interpreter=None,
        shard_list: list = None,
        persistent_path=None,
    ):
        super(DontStarveWindows, self).__init__(
            cluster, command_interpreter, shard_list, persistent_path
        )
        if command_interpreter is None:
            self.command_interpreter = "powershell"
        self.dedicated_server_path = os.environ["WINDOWS_DEDICATED_SERVER_PATH"]

    def start_shard(self, shard_name):
        command = self.prepare_command(shard_name)
        print(command)
        os.system(f'start "{self.cluster} - {shard_name}" ./{command}')


class DontStarveLinux(DontStarveStarter):
    bin = "./dontstarve_dedicated_server_nullrenderer_x64"

    def __init__(
        self,
        cluster,
        command_interpreter=None,
        shard_list: list = None,
        persistent_path=None,
    ):
        super(DontStarveLinux, self).__init__(
            cluster, command_interpreter, shard_list, persistent_path
        )
        if command_interpreter is None:
            self.command_interpreter = "gnome-terminal"
        self.dedicated_server_path = os.environ["LINUX_DEDICATED_SERVER_PATH"]

    def start_shard(self, shard_name):
        command = self.prepare_command(shard_name)
        print(command)
        os.system(
            f"gnome-terminal --title='{self.cluster} - {shard_name}' -- {command}"
        )
