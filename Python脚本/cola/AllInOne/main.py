import os
import sys
from utils.scan_port import ScanPort
from utils.unlock_account import UnlockAccount
from utils.reset_password import ResetPassword
from utils.init_product import InitProduct
from utils.k8s_clusterrole import TokenForClusterRole
from utils.log_collect import Log
from utils.print_color import print_color_text, RED, GREEN, BLUE


def main():

    try:
        action = sys.argv[1]

        if len(sys.argv) < 2:
            # sys.argv.append("manual")
            print_color_text(
                f"执行 {os.path.basename(__file__)} help 查看脚本使用方法", RED
            )

        if action == "help":
            print_color_text(
                f"Usage: {os.path.basename(__file__)} [ACTION] [OPTIONS]", GREEN
            )
            print_color_text(
                f"""
    OPTIONS:
      ACTION:
        reset: 重置产品默认密码, 支持: RAS UPM CMC CAS

        unlock: 解锁平台账户, 支持: RAS UPM CMC CAS

        scan: 扫描指定IP的TCP或UDP端口状态, (UDP 端口扫描结果不可靠)

        log: 打印日志路径, 收集日志

        init: 更换管理IP之后, 修改中间件IP地址

        token: 在K8S集群中创建只读权限的ClusterRole
""",
                GREEN,
            )
            return

        elif action == "reset" or action == "unlock":
            # 产品名称
            product = sys.argv[2]
            if len(sys.argv) < 2:
                print_color_text(
                    f"""
    reset: 重置产品默认密码, 支持: ras upm cas cmc
        {os.path.basename(__file__)} reset cas

    unlock: 解锁平台账户, 支持: ras upm cas cmc
        {os.path.basename(__file__)} unlock cas
""",
                    RED,
                )
                return

            match (action, product):
                case ("unlock", "cas"):
                    UnlockAccount.cmc_and_cas("dblue")
                case ("unlock", "cmc"):
                    UnlockAccount.cmc_and_cas("cta-business-major")
                case ("unlock", "upm"):
                    UnlockAccount.upm()
                case ("unlock", "ras"):
                    UnlockAccount.ras()
                case ("reset", "cas"):
                    ResetPassword.cmc_and_cas("dblue")
                case ("reset", "cmc"):
                    ResetPassword.cmc_and_cas("cta-business-major")
                case ("reset", "upm"):
                    ResetPassword.upm()
                case ("reset", "ras"):
                    ResetPassword.ras()
                case _:
                    print_color_text(
                        f"无效的 action 或 product : {action} or {product}", RED
                    )

        elif action == "scan":
            # 协议类型 (tcp/udp)
            protocol = sys.argv[2]
            # 目标 IP 地址和端口号
            targetip = sys.argv[3]
            port = int(sys.argv[4])

            if len(sys.argv) < 2:
                print_color_text(
                    f"""
    scan: 扫描指定 IP 端口并检查 TCP 和 UDP 状态, (UDP 端口扫描结果不可靠)
        {os.path.basename(__file__)} scan tcp 192.168.1.1 22
        {os.path.basename(__file__)} scan udp 192.168.1.1 514
""",
                    RED,
                )
                return

            if protocol == "tcp":
                ScanPort(targetip, port).scan_tcp()
            elif protocol == "udp":
                ScanPort(targetip, port).scan_udp()

        elif action == "log":
            # 日志操作 (print/collect)
            operate = sys.argv[2]

            if len(sys.argv) < 2:
                print_color_text(
                    f"""
    log: 打印日志路径, 收集日志
        {os.path.basename(__file__)} log print  cmc/cas          打印配置文件和日志路径
        {os.path.basename(__file__)} log collect  cmc/cas/parser 收集日志
"""
                )
                return

            if operate == "print":
                pass
            elif operate == "collect":
                product = sys.argv[3]
                match (operate, product):
                    case ("collect", "cmc"):
                        Log.collect_cmc_log()
                    case _:
                        print_color_text(
                            f"无效的 action 或 product : {action} or {product}", RED
                        )

        elif action == "init":
            # 产品名称
            product = sys.argv[2]
            # 新 IP 地址
            new_ip = sys.argv[3]

            if len(sys.argv) < 2:
                print_color_text(
                    f"""
    init: 更换管理IP之后, 修改中间件IP地址
        {os.path.basename(__file__)} init cas           初始化 混天绫
        {os.path.basename(__file__)} init cmc center    初始化 云魔方 center
        {os.path.basename(__file__)} init cmc worker    初始化 云魔方 worker
        {os.path.basename(__file__)} init cmc parser    初始化 云魔方 parser 
        {os.path.basename(__file__)} init cmc analyzer  初始化 云魔方 analyzer
        {os.path.basename(__file__)} init cmc ck        初始化 ClickHouse (根据部署架构操作)
""",
                    RED,
                )
                return

            if product == "cas":
                InitProduct(new_ip).kafka_config(product)

            elif product == "cmc":
                # 区分center worker parser
                component = sys.argv[4]

                match (product, component):
                    case ("cmc", "center"):
                        InitProduct(new_ip).kafka_config(product)
                        InitProduct(new_ip).center_host_config()
                        InitProduct(new_ip).center_config()
                    case ("cmc", "worker"):
                        InitProduct(new_ip).kafka_config(product)
                        InitProduct(new_ip).center_config()
                    case ("cmc", "parser"):
                        InitProduct(new_ip).center_parser_config()
                    case ("cmc", "analyzer"):
                        InitProduct(new_ip).center_analyzer_config()
                    case ("cmc", "ck"):
                        InitProduct(new_ip).clickhouse_config()
                    case _:
                        print_color_text(f"无效的组件: {product} or {component}", RED)

        elif action == "token":
            # 操作、命名空间、只读clusterrole
            operate = sys.argv[2]
            # 命名空间
            namespace = sys.argv[3]
            # 集群角色
            cluster_role = sys.argv[4]
            # secret名
            secret_name = f"{cluster_role}" + "-secret"
            # 服务账户
            service_account = f"{cluster_role}" + "-service-account"
            # rolebindg名
            cluster_role_binding = f"{cluster_role}" + "-clusterrolebinding"
            # 加载k8s默认config配置
            k8s_client = TokenForClusterRole()

            if len(sys.argv) < 2:
                print_color_text(
                    f"""
    token: 在k8s集群中创建只读权限的clusterrole
        namespace: cola-ns  
        clusterrole: cola
        {os.path.basename(__file__)} token create cola-ns cola    创建只读账户
        {os.path.basename(__file__)} token view cola-ns cola      查看账户Token
""",
                    RED,
                )
                if operate == "create":
                    # 创建lusterrole及关联的资源
                    k8s_client.create_namespace(namespace)
                    k8s_client.create_cluster_role(cluster_role)
                    k8s_client.create_service_account(namespace, service_account)
                    k8s_client.create_cluster_role_binding(
                        namespace, cluster_role, cluster_role_binding, service_account
                    )
                    k8s_client.create_secret(namespace, service_account, secret_name)

                elif operate == "view":
                    # 查看clusterrole的Token
                    k8s_client.get_secret_token(namespace, secret_name)

            else:
                print_color_text(f"无效的参数: {action}", RED)

        else:
            print_color_text("不支持此操作系统", RED)

    except Exception as e:
        return


if __name__ == "__main__":
    main()
