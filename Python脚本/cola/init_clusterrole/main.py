import os
import sys
from utils.k8s_clusterrole import TokenForClusterRole
from utils.log_collect import Log
from utils.init_product import InitProduct
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

        elif action == "log":
            # 日志操作 (print/collect)
            operate = sys.argv[2]

            if len(sys.argv) < 2:
                print_color_text(
                    f"""
        log: 打印日志路径, 收集日志
        example:
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
        example:
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
                            print_color_text(
                                f"无效的组件: {product} or {component}", RED
                            )

                elif action == "token":
                    # 操作、命名空间、只读clusterrole
                    operate = sys.argv[2]
                    namespace = sys.argv[3]  # 命名空间
                    cluster_role = sys.argv[4]  # 集群角色
                    secret_name = f"{cluster_role}" + "-secret"  # secret名
                    service_account = f"{cluster_role}" + "-service-account"  # 服务账户
                    cluster_role_binding = (
                        f"{cluster_role}" + "-clusterrolebinding"
                    )  # rolebindg名

                    # 加载k8s默认config配置
                    k8s_client = TokenForClusterRole()

                    if len(sys.argv) < 2:
                        print_color_text(
                            f"""
    token: 在k8s集群中创建只读权限的clusterrole
        example:
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
                            namespace,
                            cluster_role,
                            cluster_role_binding,
                            service_account,
                        )
                        k8s_client.create_secret(
                            namespace, service_account, secret_name
                        )

                    elif operate == "view":
                        # 查看clusterrole的Token
                        k8s_client.get_secret_token(namespace, secret_name)

                else:
                    print_color_text(f"无效的参数: {action}", RED)

            else:
                print_color_text("不支持此操作系统", RED)

    except Exception as e:
        # print_color_text(f"执行 {os.path.basename(__file__)} manual 查看脚本使用方法", RED)
        return


if __name__ == "__main__":
    main()
