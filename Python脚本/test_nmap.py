import nmap

# 创建一个PortScanner对象
nm = nmap.PortScanner()

target = '192.168.125.111'  # 目标IP地址或域名
ports = '1-1000'      # 扫描的端口范围

print("开始TCP端口扫描...")
# 执行TCP端口扫描
nm.scan(target, ports, arguments='-sT')  # -sT选项表示进行TCP连接扫描
for host in nm.all_hosts():
    print(f"主机: {host} ({nm[host].hostname()})")
    for proto in nm[host].all_protocols():
        print(f"协议: {proto}")
        lport = nm[host][proto].keys()
        for port in lport:
            state = nm[host][proto][port]['state']
            print(f"端口: {port}\t状态: {state}")

print("\n开始UDP端口扫描...")
# 执行UDP端口扫描
nm.scan(target, ports, arguments='-sU')  # -sU选项表示进行UDP扫描
for host in nm.all_hosts():
    print(f"主机: {host} ({nm[host].hostname()})")
    for proto in nm[host].all_protocols():
        print(f"协议: {proto}")
        lport = nm[host][proto].keys()
        for port in lport:
            state = nm[host][proto][port]['state']
            print(f"端口: {port}\t状态: {state}")