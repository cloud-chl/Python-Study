import os
import sys
import subprocess
from datetime import datetime
import xml.etree.ElementTree as ET
from .print_color import print_color_text, RED, BLUE, YELLOW, GREEN


class InitProduct:
    """初始化混天绫和云魔方"""

    def __init__(self, newIp):
        self.newIp = newIp

    def find_file(self, FilePath):
        # 找出对应修改的配置文件
        res = subprocess.run(
            ["/bin/find", "/", "-path", f"{FilePath}", "-type", "f"],
            capture_output=True,
            text=True,
        )
        if res.returncode != 0:
            print_color_text(f"未找到 {FilePath} 配置文件", RED)
            return None

        return res.stdout.strip().split("\n")

    def kafka_config(self, product):
        # kafka 配置文件
        kafka_config_path = "*/kafka/config/server.properties"
        kafka_config_file = self.find_file(kafka_config_path)

        cmd = [
            "/bin/sed",
            "-i",
            f"s/^advertised\\.listeners=PLAINTEXT://{self.newIp}:9092",
            self.find_file(kafka_config_path),
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)

        if res.returncode == 0:
            subprocess.run(
                ["/bin/systemctl", "restart", "kafka"], capture_output=True, text=True
            )
            # 混天绫初始化才需要重启ck
            if product == "cas":
                subprocess.run(
                    ["/bin/systemctl", "restart", "clickhouse-server"],
                    capture_output=True,
                    text=True,
                )
                print_color_text(f"修改 {kafka_config_file} 成功", BLUE)
                cmd2 = [
                    "/bin/sed",
                    f"/^advertised/p",
                    self.find_file(kafka_config_path),
                ]
                res2 = subprocess.run(cmd2, capture_output=True, text=True)
                print_color_text(f"下面是 {kafka_config_file} 配置修改的内容", YELLOW)
                print_color_text(f"Kafka: {res2.stdout}", BLUE)
        else:
            print_color_text(f"修改 {kafka_config_file} 失败", RED)

    def clickhouse_config(self):
        # clickhouse-server 配置文件
        clickhouse_config_path = "*/clickhouse-server/config.xml"
        clickhouse_config_file = self.find_file(clickhouse_config_path)

        # 解析配置文件
        clickhous_tree = ET.parse(clickhouse_config_file)
        clickhous_root = clickhous_tree.getroot()

        try:
            for host in clickhous_root.findall(
                ".//remote_servers/cas_cluster/shard/replica/host"
            ):
                old_host = host.text
                host.text = host.text.replace(f"{old_host}", f"{self.newIp}")
            # 将内容写入配置文件
            clickhous_tree.write(
                clickhouse_config_file, encoding="utf-8", xml_declaration=True
            )
            print_color_text(f"修改 {clickhouse_config_file}  配置成功", BLUE)
            modify_content = ET.tostring(
                clickhous_root, method="xml", encoding="utf-8"
            ).decode("utf-8")
            print_color_text(f"下面是 {clickhouse_config_file} 配置修改的内容", YELLOW)
            print_color_text(f"ClickHouse: {modify_content}", BLUE)

        except ET.ParseException as e:
            print_color_text(f"XML解析错误: {e}", RED)
        except FileNotFoundError as e:
            print_color_text(f"未找到 {clickhouse_config_path}", RED)
        except Exception as e:
            print_color_text(f"ERROR: {e}", RED)

    def center_config(self):
        # cta-alarm-boot 配置文件
        alarm_config_path = "*/cta-alarm-boot/config/config.properties"
        alarm_config_file = self.find_file(alarm_config_path)

        cmd_ip = ["/bin/sed", "-i", f"s/^ip=.*$/ip={self.newIp}/", alarm_config_file]
        cmd_centerIp = [
            "/bin/sed",
            "-i",
            f"s/^center\.ip=.*$/center\.ip={self.newIp}/",
            alarm_config_file,
        ]

        res1 = subprocess.run(cmd_ip, capture_output=True, text=True)
        res2 = subprocess.run(cmd_centerIp, capture_output=True, text=True)

        if res1.returncode == 0 and res2.returncode == 0:
            subprocess.run(
                ["/bin/systemctl", "restart", "cta-alarm-boot"],
                capture_output=True,
                text=True,
            )
            print_color_text(f"修改 {alarm_config_file} 成功", BLUE)
            cmd3 = ["/bin/sed", f"/^center\.ip=.*$/p", f"{alarm_config_file}"]
            res3 = subprocess.run(cmd3, capture_output=True, text=True)
            print_color_text(f"下面是 {alarm_config_file} 配置修改的内容", YELLOW)
            print_color_text(f"Kafka: {res3.stdout}", BLUE)

    def center_host_config(self, hostname_pattern="colasoft.cas"):
        # hosts 文件
        host_config_file = "/etc/hosts"
        now = datetime.now().strftime("%Y-%m-%d")
        # 备份hosts
        subprocess.run(
            ["/bin/cp", "/etc/hosts", f'/etc/hosts.bak_{now.strftime("%Y-%m-%d")}'],
            capture_output=True,
            text=True,
        )

        cmd1 = [
            "/bin/sed",
            "-i",
            f"/{hostname_pattern}/s/\\b[0-9]\\{{1,3\\}}\\.[0-9]\\{{1,3\\}}\\.[0-9]\\{{1,3\\}}\\.[0-9]\\{{1,3\\}}\\b/{self.new_ip}/",
            host_config_file,
        ]
        res = subprocess.run(cmd1, capture_output=True, text=True)

        if res.returncode == 0:
            cmd2 = ["sed", f"/{hostname_pattern}/p", host_config_file]
            res2 = subprocess.run(cmd2, capture_output=True, text=True)
            print_color_text(f"修改 {host_config_file} 成功", BLUE)
            print_color_text(f"下面是 {host_config_file} 配置修改的内容", YELLOW)
            print_color_text(f"hosts: {res2.stdout}", BLUE)
        else:
            print_color_text(f"修改 {host_config_file} 失败", RED)

    def center_parser_config(self):
        # 解析器配置文件路径
        parser_config_suffix = "*/parser.cfg"
        parser_config_file = self.find_file(parser_config_suffix)

        # 解析配置文件
        parser_tree = ET.parse(parser_config_file)
        parser_root = parser_tree.getroot()

        try:
            for ip in parser_root.findall(".//appcenter.ip/ip"):
                old_ip = ip.text
                ip.text = ip.text.replace(f"{old_ip}", f"{self.newIp}")
            # 将内容写入配置文件
            parser_tree.write(
                parser_config_file, encoding="utf-8", xml_declaration=True
            )
            print_color_text(
                f"修改 {parser_config_file}, Parser: {ip.text} 配置成功", BLUE
            )

            modify_content = ET.tostring(
                parser_root, encoding="utf-8", method="xml"
            ).decode("utf-8")
            print_color_text(f"下面是 {parser_config_file} 配置修改的内容", YELLOW)
            print_color_text(f"Parser: {modify_content}", BLUE)

        except ET.ParseError as e:
            print_color_text(f"XML解析错误: {e}", RED)
        except FileNotFoundError as e:
            print_color_text(f"未找到 {parser_config_suffix}", RED)
        except Exception as e:
            print_color_text(f"ERROR: {e}", RED)

    def center_analyzer_config(self):
        # 分析器配置文件路径
        analyzer_config_suffix = "*/analyzer.cfg"
        analyzer_config_file = self.find_file(analyzer_config_suffix)

        # 解析配置文件
        analyzer_tree = ET.parse(analyzer_config_file)
        analyzer_root = analyzer_tree.getroot()

        try:
            for brokers in analyzer_root.findall(".//mq.bargain.brokers/brokers"):
                old_brokers = brokers.text
                brokers.text = brokers.text.replace(
                    f"{old_brokers}", f"{self.newIp}:9200"
                )
            # 将内容写入配置文件
            analyzer_tree.write(
                analyzer_config_file, encoding="utf-8", xml_declaration=True
            )
            print_color_text(
                f"修改 {analyzer_config_file}, Analyzer: {brokers.text} 配置成功", BLUE
            )
            modify_content = ET.tostring(
                analyzer_root, method="xml", encoding="utf-8"
            ).decode("utf-8")
            print_color_text(f"下面是 {analyzer_config_file} 配置修改的内容", YELLOW)
            print_color_text(f"Analyzer: {modify_content}", BLUE)

        except ET.ParseError as e:
            print_color_text(f"XML解析错误: {e}", RED)
        except FileNotFoundError as e:
            print_color_text(f"未找到 {analyzer_config_suffix}", RED)
        except Exception as e:
            print_color_text(f"ERROR: {e}", RED)


# if __name__ == "__main__":

#     action = sys.argv[1]

#     if len(sys.argv) < 2:
#         # sys.argv.append("manual")
#         print_color_text(
#             f"执行 {os.path.basename(__file__)} help 查看脚本使用方法", RED
#         )

#     if action == "help":
#         print_color_text(f"Usage: {os.path.basename(__file__)} [ACTION] [OPTIONS]", GREEN)
#         print_color_text(f"""init: 更换管理IP之后, 修改中间件IP地址""", GREEN)
#         print_color_text(f"""
# init: 更换管理IP之后, 修改中间件IP地址
#     {os.path.basename(__file__)} init cas newip           初始化 混天绫
#     {os.path.basename(__file__)} init cmc newip center    初始化 云魔方 center
#     {os.path.basename(__file__)} init cmc newip worker    初始化 云魔方 worker
#     {os.path.basename(__file__)} init cmc newip parser    初始化 云魔方 parser 
#     {os.path.basename(__file__)} init cmc newip analyzer  初始化 云魔方 analyzer
#     {os.path.basename(__file__)} init cmc newip ck        初始化 ClickHouse (根据部署架构操作)
# """, RED)
        
#     elif action == "init":
#         # 产品名称
#         product = sys.argv[2]
#         # 新 IP 地址
#         new_ip = sys.argv[3]

#         if product == "cas":
#             InitProduct(new_ip).kafka_config(product)

#         elif product == "cmc":
#             # 区分center worker parser
#             component = sys.argv[4]

#             match (product, component):
#                 case ("cmc", "center"):
#                     InitProduct(new_ip).kafka_config(product)
#                     InitProduct(new_ip).center_host_config()
#                     InitProduct(new_ip).center_config()
#                 case ("cmc", "worker"):
#                     InitProduct(new_ip).kafka_config(product)
#                     InitProduct(new_ip).center_config()
#                 case ("cmc", "parser"):
#                     InitProduct(new_ip).center_parser_config()
#                 case ("cmc", "analyzer"):
#                     InitProduct(new_ip).center_analyzer_config()
#                 case ("cmc", "ck"):
#                     InitProduct(new_ip).clickhouse_config()
#                 case _:
#                     print_color_text(f"无效的组件: {product} or {component}", RED)
