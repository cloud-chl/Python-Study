import os
import stat
import paramiko
from .print_color import print_color_text, RED, BLUE


class SftpManager:
    """文件上传下载"""
    def __init__(self, ip, port, username, password):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.ssh_conn = None
        self.sftp_client = None
        self.connect()

    def connect(self):
        """建立 SSH 和 SFTP 连接"""
        try:
            # 建立SSH对象
            self.ssh_conn = paramiko.Transport((self.ip, self.port))
            # 建立 SSH 客户端
            self.ssh_conn.connect(username=self.username, password=self.password)
            # 建立 SFTP 客户端
            self.sftp_client = paramiko.SFTPClient.from_transport(self.ssh_conn)

        except Exception as e:

            print_color_text(f"Failed to connect: {e}", RED)

            if self.ssh_conn:
                self.disconnect()

            if self.ssh_conn:
                self.ssh_conn.close()

            raise

    def disconnect(self):
        """关闭 SSH 和 SFTP 连接"""

        if self.sftp_client:
            self.sftp_client.close()

        if self.ssh_conn:
            self.ssh_conn.close()

    def check_remote_dir_exist(self, path):
        """递归创建远程主机目录"""

        if not path:
            return

        try:
            self.sftp_client.stat(path)

        except IOError:
            # 目录不存在，创建目录
            dirname = os.path.dirname(path)

            # 目录存在，重新递归调用判断
            if dirname:
                self.check_remote_dir_exist(dirname)
            self.sftp_client.mkdir(path)

    def sftp_put(self, local_path, remote_path):
        """上传文件或目录"""
        
        try:
            if os.path.isfile(local_path):
                remote_file_dir = os.path.dirname(remote_path)
                self.check_remote_dir_exist(remote_file_dir)
                # 上传单个文件
                self.sftp_client.put(local_path, remote_path)
                print_color_text(f"成功上传文件: {local_path} -> {remote_path}", BLUE)

            elif os.path.isdir(local_path):

                # 确认远程目录是否存在
                self.check_remote_dir_exist(remote_path)

                # 遍历本地目录并上传每一个
                for item in os.listdir(local_path):
                    local_item_path = os.path.join(local_path, item)
                    remote_item_path = os.path.join(remote_path, item).replace('\\', '/')

                    if os.path.isdir(local_item_path):
                        self.sftpPut(local_item_path, remote_item_path)
                        print_color_text(f"成功下载文件: {remote_path} -> {local_path}", BLUE)

                    else:
                        remote_file_dir = os.path.dirname(remote_item_path)
                        self.check_remote_dir_exist(remote_file_dir)
                        remote_item_path = remote_item_path.replace('\\', '/')
                        # 上传单个文件
                        self.sftp_client.put(local_item_path, remote_item_path)
                        print_color_text(f"成功上传文件: {local_item_path} -> {remote_item_path}", BLUE)

        except Exception as e:
            print_color_text(f"上传失败: {local_path} -> {remote_path}: {e}", RED)
            raise

    def sftp_get(self, remote_path, local_path):

        try:
            # 获取目录或文件状态
            attrs = self.sftp_client.stat(remote_path)

            # 判断是不是文件
            if stat.S_ISREG(attrs.st_mode):
                # 下载单个文件
                self.sftp_client.get(remote_path, local_path)
            
            # 判断目录还是文件
            elif stat.S_ISDIR(attrs.st_mode):
                os.makedirs(local_path, exist_ok=True)

                # 获取目录下面所有文件或目录
                for item in self.sftp_client.listdir(remote_path):
                    remote_item_path = remote_path + '/' + item
                    local_item_path = os.path.join(local_path, item)
                    item_attrs = self.sftp_client.stat(remote_item_path)

                    # 目录下面还是目录, 重新进行递归调用
                    if stat.S_ISDIR(item_attrs.st_mode):
                        os.makedirs(os.path.dirname(local_item_path), exist_ok=True)
                        self.sftp_get(remote_item_path, local_item_path)

                    else:
                        self.sftp_client.get(remote_item_path, local_item_path)
                        print_color_text(f"成功下载文件: {remote_item_path} -> {local_item_path}", BLUE)

        except Exception as e:
            print_color_text(f"下载失败: {remote_path} -> {local_path}: {e}", BLUE)
            raise

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()


# if __name__ == "__main__":
#     pass