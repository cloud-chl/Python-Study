import os
import tarfile
import subprocess
from datetime import datetime
from .print_color import print_color_text, GREEN, RED, YELLOW, BLUE


class Log:
    """日志打印和收集"""

    def __init__(self):
        # 云魔方日志和配置文件
        self.cmc_java_cfg = {
            "cta-alarm-boot": "*/cta-alarm-boot/config/config.*", 
            "cta-business-major-boot": "*/cta-business-major-boot/config/application.*"
        }
        self.cmc_java_log = {
            "csf-auth": "*/csf-auth/csf-auth-debug.log",
            "cta-alarm-boot": "*/cta-alarm-boot/cta-alarm-boot-debug.log", 
            "cta-business-major-boot": "*/cta-business-major-boot/cta-business-major-boot-debug.log",
            "cta-node-manage-boot": "*/cta-node-manage-boot/cta-node-manage-boot-debug.log", 
            "cta-updater-boot": "*/cta-updater-boot/cta-updater-boot-debug.log"
        }
        self.cmc_middleware_log = {
            "clickhouse-server": "*/clickhouse-server/clickhouse-server.log", 
            "mysql": "*/mysql/log/error.log", 
            "redis": "*/redis/redis.log", 
            "nginx": "*/nginx/access.log", 
            "kafka": "*/kafka/logs/server.log"
        }
        self.cmc_middleware_cfg = {
            "nginx": "*/nginx/nginx.conf", 
            "redis": "*/redis/redis.conf", 
            "zookeeper": "*/zookeeper/conf/zoo.cfg", 
            "kafka": "*/kafka/config/server.properties", 
            "mysql": "*/mysql/my.cnf"
        }
        self.cmc_service = {
            "csf": "*csf-auth.service", 
            "cta-node-manage-boot": "*cta-node-manage-boot.service", 
            "cta-business-major-boot": "*cta-business-major-boot.service", 
            "cscmc-alarm-worker": "*cscmc-alarm-worker.service", 
            "cap-controller": "*cap-controller.service", 
            "cta-alarm-boot": "*cta-alarm-boot.service", 
            "zookeeper": "*zookeeper.service", 
            "clickhouse-server": "*clickhouse-server.service", 
            "nginx": "*nginx.service", 
            "mysql": "*mysql*service", 
            "kafka": "*kafka*service", 
            "redis": "*redis*service"
        }
        self.cmc_system_log = "/var/log/message*"

        # 解析器 分析器配置文件和日志
        self.parser_cfg = "*/assets.cfg"
        self.analyzer_cfg = "*/analyzer.cfg"
        self.log_list = {
            "parser": "*/parser/*.log", 
            "analyzer": "*/analyzer/*.log", 
            "monitor": "*/monitor/*.log"
        }
        self.service_list = {
            "parser": "parser.service", 
            "analyzer": "analyzer.service", 
            "monitor": "monitor.service"
        }

        # 混天绫日志和配置文件
        
    def find_abs_file(self, filepath):
        """找出对应修改的配置文件"""
        res = subprocess.run(['/bin/find', '/', '-path', f'{filepath}', '-type', 'f'], capture_output=True, text=True)
        if res.returncode != 0:
            print_color_text(f"未找到 {filepath}", RED)
            return None
        
        return res.stdout.strip().split('\n')
    
    def find_base_dir(self, file_list):
        abs_path = [self.find_abs_file(file_path) for _, file_path in file_list.items()]
        if not abs_path: return None
        # 返回文件绝对路径中的公共路径
        return os.path.commonpath(abs_path)

    def tar_file(self, tar, file_list, target_dir):
        base_dir = self.find_base_dir(file_list)
        if not base_dir: 
            print_color_text("无法找到公共目录", RED)
            return
        
        for filename, filepath in file_list.items():
            for abs_file in self.find_abs_file(filepath):
                abs_dir = os.path.dirname(abs_file)
                relpath = os.path.realpath(abs_dir, base_dir)
            
            # 构建压缩包目录结构
            arcname = os.path.join(target_dir, relpath)
            if abs_dir and os.path.exists(abs_dir):

                tar.add(abs_dir, arcname=arcname)
                print_color_text(f"{target_dir.capitalize()} 文件 {filename} 已压缩", GREEN)

    def collect_cmc_log(self):

        time = datetime.strftime(datetime.datetime.now(), "%Y-%m-%d_%H:%M:%")
        output_tar_file = f"CMC_{time}.tar.gz"
        try:
            with tarfile.open(output_tar_file, 'w:gz') as tar:
                # java日志
                self.tar_file(tar, self.cmc_java_log, "logs")
                # java配置
                self.tar_file(tar, self.cmc_java_cfg, "conf")
                # 中间件日志
                self.tar_file(tar, self.cmc_middleware_log, "logs")
                # 中间件配置
                self.tar_file(tar, self.cmc_middleware_cfg, "conf")
                # Systemd文件
                self.tar_file(tar, self.cmc_service, "systemd")

        except Exception as e:
            print_color_text(f"ERROR: {e}", RED)

        print_color_text(f"CMC 日志和配置文件已收集到 {output_tar_file}", YELLOW)

    def print_cmc_log_and_config_path(self):
        for filename, filepath in self.cmc_java_cfg.items():
            filepath = self.find_abs_file(filepath)
            print_color_text(f"JAVA 配置文件：{filename} 路径: {filepath}", BLUE)
        for filename, filepath in self.cmc_java_log.items():
            filepath = self.find_abs_file(filepath)
            print_color_text(f"JAVA 日志：{filename} 路径: {filepath}", BLUE)
        for filename, filepath in self.cmc_middleware_cfg.items():
            filepath = self.find_abs_file(filepath)
            print_color_text(f"中间件配置文件：{filename} 路径: {filepath}", BLUE)
        for filename, filepath in self.cmc_middleware_log.items():
            filepath = self.find_abs_file(filepath)
            print_color_text(f"中间件日志：{filename} 路径: {filepath}", BLUE)
        for filename, filepath in self.cmc_service.items():
            filepath = self.find_abs_file(filepath)
            print_color_text(f"Systemd文件 {filename} 路径: {filepath}", BLUE)

    def collect_parser_and_analyzer_log(self):
        time = datetime.strftime(datetime.datetime.now(), "%Y-%m-%d_%H:%M:%")
        output_tar_file = f"CMC_Parser_Analyzer_{time}.tar.gz"

        try:
            with tarfile.open(output_tar_file, 'w:gz') as tar:
                # Systemd启动配置
                self.tar_file(tar, self.service_list, "systemd")
                # 日志文件
                self.tar_file(tar, self.log_list, "logs")
        except Exception as e:
            print_color_text(f"ERROR: {e}", RED)

        print_color_text(f"解析器和分析器日志和配置文件已收集到 {output_tar_file}", YELLOW)        
    def print_parser_and_analyzer_log(self):
        print_color_text(f"Parser配置: {self.find_abs_file(self.parser_cfg)}", BLUE)
        print_color_text(f"Analyzer配置: {self.find_abs_file(self.analyzer_cfg)}", BLUE)
        for filename, filepath in self.log_list.items():
            filepath = self.find_abs_file(filepath)
            print_color_text(f"{filename.capitalize()} 日志：{filename} 路径: {filepath}", BLUE)
        for filename, filepath in self.cmc_service.items():
            filepath = self.find_abs_file(filepath)
            print_color_text(f"{filename.capitalize()} Systemd文件 {filename} 路径: {filepath}", BLUE)

    def collect_cas_log(self):
        # 混天绫服务日志和配置文件
        pass

    def print_cas_log_and_config_path(self):
        pass


# if __name__ == "__main__":
#     pass