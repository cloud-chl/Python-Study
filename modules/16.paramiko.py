import os
import paramiko


# def sshDemo():
#
#     # 实例化对象
#     ssh_client = paramiko.SSHClient()
#     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh_client.connect(hostname="192.168.125.111", port=22, username="root", password="qwe")
#
#     stdin, stdout, stderr = ssh_client.exec_command("ls /")
#     res = stdout.read().decode("utf-8")
#     print(res)
#     ssh_client.close()


# def sshExecCMD(ip, port, username, password, cmd):
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(hostname=ip, port=port, username=username, password=password)
#     stdin, stdout, stderr = ssh.exec_command(cmd)
#     res = stdout.read().decode('utf-8')
#     print(res)
#     ssh.close()


# def sshUploadFile():
#     ssh_conn = paramiko.Transport(("192.168.125.111", 22))
#     ssh_conn.connect(username="root", password="qwe")
#
#     ftp_client = paramiko.SFTPClient.from_transport(ssh_conn)
#     # ftp_client.get("/etc/hosts", r"F:\Python-Study\modules\tmp\hosts")
#     ftp_client.put(r"F:\Python-Study\modules\tmp\hosts", "/tmp/hosts")
#     ssh_conn.close()


def sshPutFile(ip, port ,username, password, localfile, remotedir):

    file_name = os.path.basename(localfile)
    if not remotedir.endswith('/'):
        remotedir += '/'
    dest_file_name = remotedir + file_name
    ssh_conn = paramiko.Transport((ip, port))
    ssh_conn.connect(username=username, password=password)

    ftp_client = paramiko.SFTPClient.from_transport(ssh_conn)
    ftp_client.put(localfile, dest_file_name)

    ssh_conn.close()


if __name__ == '__main__':
    # sshDemo()
    # ip = input("IP地址: ")
    # port = input("端口: ")
    # username = input("用户名: ")
    # password = input("密码: ")
    # cmd = input("执行命令: ")
    # sshExecCMD(ip=ip, port=port, username=username, password=password, cmd=cmd)

    # sshUploadFile()
    sshPutFile(ip="192.168.125.111", port=22, username="root", password="qwe", localfile=r"F:\Python-Study\modules\tmp\hosts", remotedir="/tmp")