import base64
from kubernetes import client, config
from kubernetes.client.rest import ApiException
from .print_color import print_color_text, RED, BLUE, YELLOW


class TokenForClusterRole:
    """创建只读权限的集群角色"""

    def __init__(self, ):
        config.load_kube_config()
        self.core_v1_api = client.CoreV1Api()
        self.rbac_api = client.RbacAuthorizationV1Api()

    def check_namespace_exist(self, namespace):
        """检查 NameSpace 是否存在"""
        try:
            self.core_v1_api.read_namespace(namespace)
            print_color_text(f"NameSpace: {namespace} 已存在", YELLOW)
            return True  # Namespace 存在
        except ApiException as e:
            return False
            
    def create_namespace(self, namespace):
        """创建NameSpace"""
        body = client.V1Namespace(
                metadata=client.V1ObjectMeta(name=namespace)
            )

        if not self.check_namespace_exist(namespace):
            try:
                self.core_v1_api.create_namespace(body)
                # print_color_text(api_response)
                print_color_text(f"NameSpace: {namespace} 创建成功", BLUE)
            except Exception as e:
                print_color_text(f"NameSpace {namespace} 创建失败", RED)
                print_color_text(f"ERROR: {e}", RED)

    def check_cluster_role_exist(self, cluster_role):
        """检查 ClusterRole 是否存在"""
        try:
            self.rbac_api.read_cluster_role(cluster_role)
            # print_color_text(self.rbac_api.read_cluster_role(cluster_role))
            print_color_text(f"ClusterRole: {cluster_role} 已存在", YELLOW)
            return True
        except ApiException as e:
            return False
        
    def create_cluster_role(self, cluster_role):
        """创建 ClusterRole"""
        rule = client.V1PolicyRule(
                api_groups=[""],
                resources=[""],
                verbs=[""]
            )
        body = client.V1ClusterRole(
            metadata=client.V1ObjectMeta(name=cluster_role),
            rules=[rule]
        )

        if not self.check_cluster_role_exist(cluster_role):
            try:
                self.rbac_api.create_cluster_role(body)
                print_color_text(f"ClusterRole: {cluster_role} 创建成功", BLUE)
            except ApiException as e:
                print_color_text(f"ClusterRole: {cluster_role} 创建失败: {e}", RED)

    def check_service_account_exist(self, namespace, service_account):
        """检查ServiceAccount是否存在"""
        try:
            self.core_v1_api.read_namespaced_service_account(service_account, namespace)
            print_color_text(f"ServiceAccount: {service_account} 已存在", YELLOW)
            return True
        except ApiException as e:
            return False

    def create_service_account(self, namespace, service_account):
        """创建ServiceAccount"""
        body = client.V1ServiceAccount(
            metadata=client.V1ObjectMeta(name=service_account)
        )

        if not self.check_service_account_exist(namespace, service_account):
            try:
                self.core_v1_api.create_namespaced_service_account(namespace, body)
                print_color_text(f"ServiceAccount: {service_account} 创建成功", BLUE)
            except ApiException as e:
                print_color_text(f"ServiceAccount: {service_account} 创建失败", RED)
                print_color_text(f"ERROR: {e}", RED)

    def check_cluster_role_binding_exist(self, cluster_role_binding):
        """检查 ClusterRoleBinding是否存在"""
        try:
            self.rbac_api.read_cluster_role_binding(cluster_role_binding)
            print_color_text(f"ClusterRoleBinding: {cluster_role_binding} 已存在", YELLOW)
            return True
        except ApiException as e:
            return False

    def create_cluster_role_binding(self, namespace, cluster_role, cluster_role_binding, service_account):
        """创建ClusterRoleBinding"""
        subject = {
            "kind": "ServiceAccount",
            "name": service_account,
            "namespace": namespace,
        } 
        
        body = client.V1ClusterRoleBinding(
            metadata=client.V1ObjectMeta(name=cluster_role_binding),
            subjects=[subject],
            role_ref=client.V1RoleRef(
                kind="ClusterRole",
                name=cluster_role,
                api_group="rbac.authorization.k8s.io"
            )
        )

        if not self.check_cluster_role_binding_exist(cluster_role_binding):
            try:
                self.rbac_api.create_cluster_role_binding(body)
                print_color_text(f"ClusterRoleBinding: {cluster_role_binding} 创建成功", BLUE)
            except ApiException as e:
                print_color_text(f"ClusterRoleBinding: {cluster_role_binding} 创建失败", RED)
                print_color_text(f"ERROR: {e}", RED)

    def create_secret(self, namespace, service_account, secret_name):
        """为ServiceAccount创建Secret"""
        body = client.V1Secret(
            metadata=client.V1ObjectMeta(
                name=secret_name,
                namespace=namespace,
                annotations={
                    "kubernetes.io/service-account.name": service_account
                }
            ),
            type="kubernetes.io/service-account-token"
        )

        try:
            self.core_v1_api.create_namespaced_secret(namespace, body)
            print_color_text(f"Secret: {secret_name} 创建成功", BLUE)
        except ApiException as e:
            if e.status == 409:
                print_color_text(f"Secret: {secret_name} 已存在", YELLOW)
                return False
            else:
                print_color_text(f"Secret: {secret_name} 创建失败", RED)
                print_color_text(f"ERROR:{e}", RED)

    def get_secret_token(self, namespace, secret_name):
        """获取Token"""
        try:
            secret_result = self.core_v1_api.read_namespaced_secret(secret_name, namespace)
            secret_token = secret_result.data.get('token')
            if secret_token:
                print_color_text(f"Token: {base64.b64decode(secret_token).decode('utf-8')}", YELLOW)
            else:
                print_color_text("Token 获取失败", RED)
        except ApiException as e:
            print_color_text(f"Token不存在: {e}", RED)


# if __name__ == "__main__":
#     pass