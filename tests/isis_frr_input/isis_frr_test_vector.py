isis_neighbors_output = \
"""
Area 1:
 System Id           Interface   L  State        Holdtime SNPA
sonic         PortChannel01202  Up            25       2020.2020.2020
sonic2         PortChannel01212  Up            25       2020.2020.2020
"""

isis_neighbors_system_id_output = \
"""
Area 1:
sonic
    Interface: PortChannel0120, Level: 2, State: Up, Expires in 24s
    Adjacency flaps: 1, Last: 4d23h33m44s ago
    Circuit type: L2, Speaks: IPv4, IPv6
    SNPA: 2020.2020.2020
    Area Address(es):
      49.0001
    IPv4 Address(es):
      104.44.20.172
    IPv6 Address(es):
      fe80::2e6b:f5ff:fee7:9c9
    Global IPv6 Address(es):
      2603:1060:0:12::f0dd
"""

isis_neighbors_hostname_output = \
"""
Area 1:
sonic
    Interface: PortChannel0120, Level: 2, State: Up, Expires in 24s
    Adjacency flaps: 1, Last: 4d23h33m44s ago
    Circuit type: L2, Speaks: IPv4, IPv6
    SNPA: 2020.2020.2020
    Area Address(es):
      49.0001
    IPv4 Address(es):
      104.44.20.172
    IPv6 Address(es):
      fe80::2e6b:f5ff:fee7:9c9
    Global IPv6 Address(es):
      2603:1060:0:12::f0dd
"""

isis_neighbors_verbose_output = \
"""
Area 1:
sonic
    Interface: PortChannel0120, Level: 2, State: Up, Expires in 24s
    Adjacency flaps: 1, Last: 4d23h33m44s ago
    Circuit type: L2, Speaks: IPv4, IPv6
    SNPA: 2020.2020.2020
    Area Address(es):
      49.0001
    IPv4 Address(es):
      104.44.20.172
    IPv6 Address(es):
      fe80::2e6b:f5ff:fee7:9c9
    Global IPv6 Address(es):
      2603:1060:0:12::f0dd
sonic2
    Interface: PortChannel0121, Level: 2, State: Up, Expires in 24s
    Adjacency flaps: 1, Last: 4d23h33m44s ago
    Circuit type: L2, Speaks: IPv4, IPv6
    SNPA: 2020.2020.2020
    Area Address(es):
      49.0001
    IPv4 Address(es):
      104.44.20.182
    IPv6 Address(es):
      fe80::2e6b:f5ff:fee7:9d4
    Global IPv6 Address(es):
      2603:1060:0:12::f0e8
"""

isis_neighbors_invalid_hostname_output = \
"""Invalid system id sonic3
"""

isis_neighbors_invalid_system_id_output = \
"""Invalid system id 10.10.10
"""

isis_neighbors_invalid_help_output = \
"""Usage: neighbors [OPTIONS] [SYSTEM_ID]
Try "neighbors --help" for help.

Error: The argument: "?" is invalid. Try "-?".
"""

def mock_show_isis_neighbors(request):
    if request.param == 'isis_neighbors_output':
        return isis_neighbors_output
    elif request.param == 'isis_neighbors_system_id_output':
        return isis_neighbors_system_id_output
    elif request.param == 'isis_neighbors_hostname_output':
        return isis_neighbors_hostname_output
    elif request.param == 'isis_neighbors_verbose_output':
        return isis_neighbors_verbose_output
    elif request.param == 'isis_neighbors_invalid_hostname_output':
        return isis_neighbors_invalid_hostname_output
    elif request.param == 'isis_neighbors_invalid_system_id_output':
        return isis_neighbors_invalid_system_id_output
    elif request.param == 'isis_neighbors_invalid_help_output':
        return isis_neighbors_invalid_help_output
    else:
        return ""


isis_database_output = \
"""Area 1:
IS-IS Level-2 link-state database:
LSP ID                  PduLen  SeqNumber   Chksum  Holdtime  ATT/P/OL
sonic1.00-00             1284   0x0000020e  0x3d7e   48072    0/0/0
sonic1.00-01             197   0x00000136  0x4474   64797    0/0/0
sonic2.00-00             1192   0x000001ae  0xd970   47837    0/0/0
sonic2.00-01             367   0x00000136  0xe315   31986    0/0/0
sonic3.00-00             1319   0x000001a9  0x3349   47881    0/0/0
sonic3.00-00             1115   0x000002e7  0x1b38   54629    0/0/0
    6 LSPs 
"""

isis_database_lsp_id_output = \
"""Area 1:
IS-IS Level-2 link-state database:
LSP ID                  PduLen  SeqNumber   Chksum  Holdtime  ATT/P/OL
sonic1.00-00             1284   0x0000020e  0x3d7e   48072    0/0/0
"""

isis_database_verbose_output = \
"""Area 1:
IS-IS Level-2 link-state database:
LSP ID                  PduLen  SeqNumber   Chksum  Holdtime  ATT/P/OL
sonic1.00-00             1284   0x0000020e  0x3d7e   47678    0/0/0
  Protocols Supported: IPv4, IPv6
  Area Address: 39.752f.0100.0014.0000.b000.1000
  Hostname: sonic1
  TE Router ID: 104.44.1.146
  Router Capability: 104.44.1.146 , D:0, S:0
    Segment Routing: I:1 V:1, Global Block Base: 16000 Range: 8000
    SR Local Block Base: 15000 Range: 1000
    SR Algorithm:
      0: SPF
      1: Strict SPF
    Node Maximum SID Depth: 10
  Extended Reachability: 1040.4400.1056.00 (Metric: 5000)
    Administrative Group: 0x10002
    Local Interface IP Address(es): 104.44.19.218
    Remote Interface IP Address(es): 104.44.19.219
    Local Interface IPv6 Address(es): 2603:1060:0:10::f36d
    Remote Interface IPv6 Address(es): 2603:1060:0:10::f36e
    Maximum Bandwidth: 1.125e+09 (Bytes/sec)
    Maximum Reservable Bandwidth: 5.625e+08 (Bytes/sec)
    Unreserved Bandwidth:
      [0]: 5.625e+08 (Bytes/sec),       [1]: 5.625e+08 (Bytes/sec)
      [2]: 5.625e+08 (Bytes/sec),       [3]: 5.625e+08 (Bytes/sec)
      [4]: 5.625e+08 (Bytes/sec),       [5]: 5.625e+08 (Bytes/sec)
      [6]: 5.625e+08 (Bytes/sec),       [7]: 5.625e+08 (Bytes/sec)
    Traffic Engineering Metric: 5000
    Adjacency-SID: 100006, Weight: 0, Flags: F:0 B:0, V:1, L:1, S:0, P:0
    Adjacency-SID: 100008, Weight: 0, Flags: F:1 B:0, V:1, L:1, S:0, P:0
  Extended Reachability: 1040.4400.1145.00 (Metric: 500)
    Administrative Group: 0x10002
    Local Interface IP Address(es): 104.44.28.152
    Remote Interface IP Address(es): 104.44.28.153
    Local Interface IPv6 Address(es): 2603:1060:0:10::f309
    Remote Interface IPv6 Address(es): 2603:1060:0:10::f30a
    Maximum Bandwidth: 1.5e+09 (Bytes/sec)
    Maximum Reservable Bandwidth: 7.5e+08 (Bytes/sec)
    Unreserved Bandwidth:
      [0]: 7.5e+08 (Bytes/sec), [1]: 7.5e+08 (Bytes/sec)
      [2]: 7.5e+08 (Bytes/sec), [3]: 7.5e+08 (Bytes/sec)
      [4]: 7.5e+08 (Bytes/sec), [5]: 7.5e+08 (Bytes/sec)
      [6]: 7.5e+08 (Bytes/sec), [7]: 7.5e+08 (Bytes/sec)
    Traffic Engineering Metric: 500
    Adjacency-SID: 100026, Weight: 0, Flags: F:0 B:0, V:1, L:1, S:0, P:0
    Adjacency-SID: 100028, Weight: 0, Flags: F:1 B:0, V:1, L:1, S:0, P:0
  Extended Reachability: 1040.4400.1056.00 (Metric: 5000)
    Administrative Group: 0x10002
    Local Interface IP Address(es): 104.44.18.252
    Remote Interface IP Address(es): 104.44.18.253
    Local Interface IPv6 Address(es): 2603:1060:0:10::f2a1
    Remote Interface IPv6 Address(es): 2603:1060:0:10::f2a2
    Maximum Bandwidth: 7.5e+08 (Bytes/sec)
    Maximum Reservable Bandwidth: 3.75e+08 (Bytes/sec)
    Unreserved Bandwidth:
      [0]: 3.75e+08 (Bytes/sec),        [1]: 3.75e+08 (Bytes/sec)
      [2]: 3.75e+08 (Bytes/sec),        [3]: 3.75e+08 (Bytes/sec)
      [4]: 3.75e+08 (Bytes/sec),        [5]: 3.75e+08 (Bytes/sec)
      [6]: 3.75e+08 (Bytes/sec),        [7]: 3.75e+08 (Bytes/sec)
    Traffic Engineering Metric: 5000
    Adjacency-SID: 100002, Weight: 0, Flags: F:0 B:0, V:1, L:1, S:0, P:0
    Adjacency-SID: 100004, Weight: 0, Flags: F:1 B:0, V:1, L:1, S:0, P:0
  IPv4 Interface Address: 104.44.1.146
  IPv6 Interface Address: 2603:1060:0:1::ff3e
  Extended IP Reachability: 104.44.1.146/32 (Metric: 0)
    Subtlvs:
      SR Prefix-SID Index: 2025, Algorithm: 0, Flags: NODE PHP
  Extended IP Reachability: 104.44.7.40/31 (Metric: 20000)
  Extended IP Reachability: 104.44.17.0/31 (Metric: 100000)
  Extended IP Reachability: 104.44.18.174/31 (Metric: 500)
  Extended IP Reachability: 104.44.18.252/31 (Metric: 5000)
  Extended IP Reachability: 104.44.19.218/31 (Metric: 5000)
  Extended IP Reachability: 104.44.28.152/31 (Metric: 500)
  Extended IP Reachability: 104.44.33.174/31 (Metric: 500)
  Extended IP Reachability: 104.44.33.184/31 (Metric: 500)
  Extended IP Reachability: 104.44.29.12/31 (Metric: 10000)
  IPv6 Reachability: 2603:1060:0:1::ff3e/128 (Metric: 0)
  IPv6 Reachability: 2603:1060:0:10::f000/126 (Metric: 20000)
  IPv6 Reachability: 2603:1060:0:10::f2a0/126 (Metric: 5000)
  IPv6 Reachability: 2603:1060:0:10::f2cc/126 (Metric: 500)
  IPv6 Reachability: 2603:1060:0:10::f308/126 (Metric: 500)
  IPv6 Reachability: 2603:1060:0:10::f35c/126 (Metric: 100000)
  IPv6 Reachability: 2603:1060:0:10::f36c/126 (Metric: 5000)
  IPv6 Reachability: 2603:1060:0:12::f4d4/126 (Metric: 500)
  IPv6 Reachability: 2603:1060:0:12::f4e8/126 (Metric: 500)
  IPv6 Reachability: 2603:1060:0:10::f3d4/126 (Metric: 10000)

.......

    6 LSPs
"""

isis_database_lsp_id_verbose_output = \
"""Area 1:
IS-IS Level-2 link-state database:
LSP ID                  PduLen  SeqNumber   Chksum  Holdtime  ATT/P/OL
sonic1.00-00             1284   0x0000020e  0x3d7e   47678    0/0/0
  Protocols Supported: IPv4, IPv6
  Area Address: 39.752f.0100.0014.0000.b000.1000
  Hostname: sonic1
  TE Router ID: 104.44.1.146
  Router Capability: 104.44.1.146 , D:0, S:0
    Segment Routing: I:1 V:1, Global Block Base: 16000 Range: 8000
    SR Local Block Base: 15000 Range: 1000
    SR Algorithm:
      0: SPF
      1: Strict SPF
    Node Maximum SID Depth: 10
  Extended Reachability: 1040.4400.1056.00 (Metric: 5000)
    Administrative Group: 0x10002
    Local Interface IP Address(es): 104.44.19.218
    Remote Interface IP Address(es): 104.44.19.219
    Local Interface IPv6 Address(es): 2603:1060:0:10::f36d
    Remote Interface IPv6 Address(es): 2603:1060:0:10::f36e
    Maximum Bandwidth: 1.125e+09 (Bytes/sec)
    Maximum Reservable Bandwidth: 5.625e+08 (Bytes/sec)
    Unreserved Bandwidth:
      [0]: 5.625e+08 (Bytes/sec),       [1]: 5.625e+08 (Bytes/sec)
      [2]: 5.625e+08 (Bytes/sec),       [3]: 5.625e+08 (Bytes/sec)
      [4]: 5.625e+08 (Bytes/sec),       [5]: 5.625e+08 (Bytes/sec)
      [6]: 5.625e+08 (Bytes/sec),       [7]: 5.625e+08 (Bytes/sec)
    Traffic Engineering Metric: 5000
    Adjacency-SID: 100006, Weight: 0, Flags: F:0 B:0, V:1, L:1, S:0, P:0
    Adjacency-SID: 100008, Weight: 0, Flags: F:1 B:0, V:1, L:1, S:0, P:0
  Extended Reachability: 1040.4400.1145.00 (Metric: 500)
    Administrative Group: 0x10002
    Local Interface IP Address(es): 104.44.28.152
    Remote Interface IP Address(es): 104.44.28.153
    Local Interface IPv6 Address(es): 2603:1060:0:10::f309
    Remote Interface IPv6 Address(es): 2603:1060:0:10::f30a
    Maximum Bandwidth: 1.5e+09 (Bytes/sec)
    Maximum Reservable Bandwidth: 7.5e+08 (Bytes/sec)
    Unreserved Bandwidth:
      [0]: 7.5e+08 (Bytes/sec), [1]: 7.5e+08 (Bytes/sec)
      [2]: 7.5e+08 (Bytes/sec), [3]: 7.5e+08 (Bytes/sec)
      [4]: 7.5e+08 (Bytes/sec), [5]: 7.5e+08 (Bytes/sec)
      [6]: 7.5e+08 (Bytes/sec), [7]: 7.5e+08 (Bytes/sec)
    Traffic Engineering Metric: 500
    Adjacency-SID: 100026, Weight: 0, Flags: F:0 B:0, V:1, L:1, S:0, P:0
    Adjacency-SID: 100028, Weight: 0, Flags: F:1 B:0, V:1, L:1, S:0, P:0
  Extended Reachability: 1040.4400.1056.00 (Metric: 5000)
    Administrative Group: 0x10002
    Local Interface IP Address(es): 104.44.18.252
    Remote Interface IP Address(es): 104.44.18.253
    Local Interface IPv6 Address(es): 2603:1060:0:10::f2a1
    Remote Interface IPv6 Address(es): 2603:1060:0:10::f2a2
    Maximum Bandwidth: 7.5e+08 (Bytes/sec)
    Maximum Reservable Bandwidth: 3.75e+08 (Bytes/sec)
    Unreserved Bandwidth:
      [0]: 3.75e+08 (Bytes/sec),        [1]: 3.75e+08 (Bytes/sec)
      [2]: 3.75e+08 (Bytes/sec),        [3]: 3.75e+08 (Bytes/sec)
      [4]: 3.75e+08 (Bytes/sec),        [5]: 3.75e+08 (Bytes/sec)
      [6]: 3.75e+08 (Bytes/sec),        [7]: 3.75e+08 (Bytes/sec)
    Traffic Engineering Metric: 5000
    Adjacency-SID: 100002, Weight: 0, Flags: F:0 B:0, V:1, L:1, S:0, P:0
    Adjacency-SID: 100004, Weight: 0, Flags: F:1 B:0, V:1, L:1, S:0, P:0
  IPv4 Interface Address: 104.44.1.146
  IPv6 Interface Address: 2603:1060:0:1::ff3e
  Extended IP Reachability: 104.44.1.146/32 (Metric: 0)
    Subtlvs:
      SR Prefix-SID Index: 2025, Algorithm: 0, Flags: NODE PHP
  Extended IP Reachability: 104.44.7.40/31 (Metric: 20000)
  Extended IP Reachability: 104.44.17.0/31 (Metric: 100000)
  Extended IP Reachability: 104.44.18.174/31 (Metric: 500)
  Extended IP Reachability: 104.44.18.252/31 (Metric: 5000)
  Extended IP Reachability: 104.44.19.218/31 (Metric: 5000)
  Extended IP Reachability: 104.44.28.152/31 (Metric: 500)
  Extended IP Reachability: 104.44.33.174/31 (Metric: 500)
  Extended IP Reachability: 104.44.33.184/31 (Metric: 500)
  Extended IP Reachability: 104.44.29.12/31 (Metric: 10000)
  IPv6 Reachability: 2603:1060:0:1::ff3e/128 (Metric: 0)
  IPv6 Reachability: 2603:1060:0:10::f000/126 (Metric: 20000)
  IPv6 Reachability: 2603:1060:0:10::f2a0/126 (Metric: 5000)
  IPv6 Reachability: 2603:1060:0:10::f2cc/126 (Metric: 500)
  IPv6 Reachability: 2603:1060:0:10::f308/126 (Metric: 500)
  IPv6 Reachability: 2603:1060:0:10::f35c/126 (Metric: 100000)
  IPv6 Reachability: 2603:1060:0:10::f36c/126 (Metric: 5000)
  IPv6 Reachability: 2603:1060:0:12::f4d4/126 (Metric: 500)
  IPv6 Reachability: 2603:1060:0:12::f4e8/126 (Metric: 500)
  IPv6 Reachability: 2603:1060:0:10::f3d4/126 (Metric: 10000)
"""

isis_database_unknown_lsp_id_output = \
"""Area 1:
"""

isis_database_invalid_help_output = \
"""Usage: database [OPTIONS] [LSP_ID]
Try "database --help" for help.

Error: The argument: "?" is invalid. Try "-?".
"""

def mock_show_isis_database(request):
    if request.param == 'isis_database_output':
        return isis_database_output
    elif request.param == 'isis_database_lsp_id_output':
        return isis_database_lsp_id_output
    elif request.param == 'isis_database_verbose_output':
        return isis_database_verbose_output
    elif request.param == 'isis_database_lsp_id_verbose_output':
        return isis_database_lsp_id_verbose_output
    elif request.param == 'isis_database_unknown_lsp_id_output':
        return isis_database_unknown_lsp_id_output
    elif request.param == 'isis_database_invalid_help_output':
        return isis_database_invalid_help_output
    else:
        return ""

isis_hostname_output = \
"""vrf     : default
Level  System ID      Dynamic Hostname
2      1000.2000.4000 sonic2    
     * 1000.2000.3000 sonic
"""

isis_hostname_invalid_help_output = \
"""Usage: hostname [OPTIONS]
Try "hostname --help" for help.

Error: Got unexpected extra argument (?)
"""


def mock_show_isis_hostname(request):
    if request.param == 'isis_hostname_output':
        return isis_hostname_output
    elif request.param == 'isis_hostname_invalid_help_output':
        return isis_hostname_invalid_help_output
    else:
        return ""

isis_interface_output = \
"""Area 1:
  Interface   CircId   State    Type     Level
  PortChannel01200x0      Up       p2p      L2 
"""

isis_interface_invalid_help_output = \
"""Usage: interface [OPTIONS] [INTERFACE]
Try "interface --help" for help.

Error: The argument: "?" is invalid. Try "-?".
"""

isis_interface_ifname_output = \
"""Area 1:
  Interface: PortChannel0002, State: Up, Active, Circuit Id: 0x0
    Type: p2p, Level: L2
    Level-2 Information:
      Metric: 10, Active neighbors: 1
      Hello interval: 3, Holddown count: 10 (no-pad)
      CNSP interval: 10, PSNP interval: 2
    IP Prefix(es):
      104.44.20.173/31
    IPv6 Link-Locals:
      fe80::5054:8ff:fe6c:8b47/64
"""

isis_interface_ifname_output = \
"""Area 1:
  Interface: PortChannel0002, State: Up, Active, Circuit Id: 0x0
    Type: p2p, Level: L2
    Level-2 Information:
      Metric: 10, Active neighbors: 1
      Hello interval: 3, Holddown count: 10 (no-pad)
      CNSP interval: 10, PSNP interval: 2
    IP Prefix(es):
      104.44.20.173/31
    IPv6 Link-Locals:
      fe80::5054:8ff:fe6c:8b47/64
"""

isis_interface_verbose_output = \
"""Area 1:
  Interface: PortChannel0002, State: Up, Active, Circuit Id: 0x0
    Type: p2p, Level: L2
    Level-2 Information:
      Metric: 10, Active neighbors: 1
      Hello interval: 3, Holddown count: 10 (no-pad)
      CNSP interval: 10, PSNP interval: 2
    IP Prefix(es):
      104.44.20.175/31
    IPv6 Link-Locals:
      fe80::5054:8ff:fe6c:8b49/64
  Interface: PortChannel0121, State: Up, Active, Circuit Id: 0x0
    Type: p2p, Level: L2
    Level-2 Information:
      Metric: 10, Active neighbors: 1
      Hello interval: 3, Holddown count: 10 (no-pad)
      CNSP interval: 10, PSNP interval: 2
    IP Prefix(es):
      104.44.20.175/31
    IPv6 Link-Locals:
      fe80::5054:8ff:fe6c:8b49/64
"""

isis_interface_unknown_ifname_output = \
'Usage: interface [OPTIONS] [INTERFACE]\n' \
'Try "interface --help" for help.\n\n' \
'Error: Invalid value for "[INTERFACE]": invalid choice: sonic1. ' \
'(choose from Ethernet0, Ethernet4, Ethernet8, Ethernet12, Ethernet16, ' \
'Ethernet20, Ethernet24, Ethernet28, Ethernet32, Ethernet36, Ethernet40, ' \
'Ethernet44, Ethernet48, Ethernet52, Ethernet56, Ethernet60, Ethernet64, ' \
'Ethernet68, Ethernet72, Ethernet76, Ethernet80, Ethernet84, Ethernet88, ' \
'Ethernet92, Ethernet96, Ethernet100, Ethernet104, Ethernet108, Ethernet112, ' \
'Ethernet116, Ethernet120, Ethernet124, PortChannel0001, PortChannel0002, ' \
'PortChannel0003, PortChannel0004, PortChannel1001)\n'

def mock_show_isis_interface(request):
    if request.param == 'isis_interface_output':
        return isis_interface_output
    elif request.param == 'isis_interface_ifname_output':
        return isis_interface_ifname_output
    elif request.param == 'isis_interface_verbose_output':
        return isis_interface_verbose_output
    elif request.param == 'isis_interface_ifname_verbose_output':
        return isis_interface_ifname_output
    elif request.param == 'isis_interface_unknown_ifname_output':
        return isis_interface_unknown_ifname_output
    else:
        return ""

show_run_isis_output = \
"""Building configuration...

Current configuration:
!
frr version 8.2.2
frr defaults traditional
hostname vlab-01
log syslog informational
log facility local4
no service integrated-vtysh-config
!
password zebra
enable password zebra
!
interface PortChannel101
 ip router isis 1
 ipv6 router isis 1
 isis network point-to-point
exit
!
router isis 1
 is-type level-2-only
 net 49.0001.1720.1700.0002.00
 lsp-mtu 1383
 lsp-timers level-1 gen-interval 30 refresh-interval 900 max-lifetime 1200
 lsp-timers level-2 gen-interval 30 refresh-interval 305 max-lifetime 900
 log-adjacency-changes
exit
!
end
"""

show_run_isis_config_db_output = \
"""
{
    "1": {
        "dynamic-hostname": "true",
        "level-capability": "level-2",
        "log-adjacency-changes": "true",
        "lsp-mtu-size": "1383",
        "net": "49.0001.1720.1700.0002.00"
    }
}
{
    "1|level-2": {
        "lsp-maximum-lifetime": "350",
        "lsp-refresh-interval": "305"
    }
}
{
    "1|PortChannel101": {
        "hello-padding": "false",
        "ifname": "PortChannel101",
        "instance": "1",
        "ipv4-routing-instance": "1",
        "ipv6-routing-instance": "1",
        "network-type": "POINT_TO_POINT_NETWORK"
    }
}
"""

show_run_isis_invalid_help_output = \
"""
Usage: show run isis [OPTIONS]
Try "show run isis -h" for help.

Error: Got unexpected extra argument (?)
"""

def mock_show_run_isis(request):
    if request.param == 'show_run_isis_output':
        return show_run_isis_output
    elif request.param == 'show_run_isis_config_db_output':
        return show_run_isis_config_db_output
    elif request.param == 'show_run_isis_invalid_help_output':
        return show_run_isis_invalid_help_output
    else:
        return ""


isis_summary_output = \
"""
r1# show isis summary 
vrf             : default
Process Id      : 4663
System Id       : 0000.0000.0000
Up time         : 00:04:31 ago
Number of areas : 1
Area 1:
  Net: 10.0000.0000.0000.0000.0000.0000.0000.0000.0000.00
  TX counters per PDU type:
     L2 IIH: 144
     L2 LSP: 4
    L2 CSNP: 29
   LSP RXMT: 0
  RX counters per PDU type:
     L2 IIH: 143
     L2 LSP: 4
  Drop counters per PDU type:
     L2 IIH: 1
  Advertise high metrics: Disabled
  Level-1:
    LSP0 regenerated: 3
         LSPs purged: 0
    SPF:
      minimum interval  : 1
    IPv4 route computation:
      last run elapsed  : 00:04:25 ago
      last run duration : 111 usec
      run count         : 3
    IPv6 route computation:
      last run elapsed  : 00:04:25 ago
      last run duration : 23 usec
      run count         : 3
  Level-2:
    LSP0 regenerated: 4
         LSPs purged: 0
    SPF:
      minimum interval  : 1
    IPv4 route computation:
      last run elapsed  : 00:04:21 ago
      last run duration : 45 usec
      run count         : 9
    IPv6 route computation:
      last run elapsed  : 00:04:21 ago
      last run duration : 14 usec
      run count         : 9
"""

isis_summary_json_output = \
"""
{
  "vrf":"default",
  "process-id":4663,
  "system-id":"0000.0000.0000",
  "up-time":"00:06:30",
  "number-areas":1,
  "areas":[
    {
      "area":"1",
      "net":"10.0000.0000.0000.0000.0000.0000.0000.0000.0000.00",
      "tx-pdu-type":{
        "l2-iih":206,
        "l2-lsp":4,
        "l2-csnp":42,
        "lsp-rxmt":0
      },
      "rx-pdu-type":{
        "l2-iih":206,
        "l2-lsp":4
      },
      "levels":[
        {
          "id":1,
          "lsp0-regenerated":3,
          "lsp-purged":0,
          "spf":"no pending",
          "minimum-interval":1,
          "last-run-elapsed":"00:06:24",
          "last-run-duration-usec":23,
          "last-run-count":3
        },
        {
          "id":2,
          "lsp0-regenerated":4,
          "lsp-purged":0,
          "spf":"no pending",
          "minimum-interval":1,
          "last-run-elapsed":"00:06:20",
          "last-run-duration-usec":14,
          "last-run-count":9
        }
      ]
    }
  ]
}
"""

isis_summary_invalid_help_output = \
"""Usage: summary [OPTIONS]
Try "summary --help" for help.
Error: Got unexpected extra argument (?)
"""

def mock_show_isis_summary(request):
    if request.param == 'isis_summary_output':
        return isis_summary_output
    elif request.param == 'isis_summary_invalid_help_output':
        return isis_summary_invalid_help_output
    elif request.param == 'isis_summary_json_output':
        return isis_summary_json_output
    else:
        return ""


testData = {
    'isis_neighbors': {
        'args': [],
        'rc': 0,
        'rc_output': isis_neighbors_output
    },
    'isis_neighbors_system_id': {
        'args': ['1000.2000.3000'],
        'rc': 0,
        'rc_output': isis_neighbors_system_id_output
    },
    'isis_neighbors_hostname': {
        'args': ['sonic'],
        'rc': 0,
        'rc_output': isis_neighbors_hostname_output
    },
    'isis_neighbors_verbose': {
        'args': ['--verbose'],
        'rc': 0,
        'rc_output': isis_neighbors_verbose_output
    },
    'isis_neighbors_invalid_hostname': {
        'args': ['sonic3'],
        'rc': 0,
        'rc_output': isis_neighbors_invalid_hostname_output
    },
    'isis_neighbors_invalid_system_id': {
        'args': ['10.10.10'],
        'rc': 0,
        'rc_output': isis_neighbors_invalid_system_id_output
    },
    'isis_neighbors_invalid_help': {
        'args': ['?'],
        'rc': 2,
        'rc_output': isis_neighbors_invalid_help_output
    },
    'isis_database': {
        'args': [],
        'rc': 0,
        'rc_output': isis_database_output
    },
    'isis_database_lsp_id': {
        'args': ['sonic1.00-00'],
        'rc': 0,
        'rc_output': isis_database_lsp_id_output
    },
    'isis_database_verbose': {
        'args': ['--verbose'],
        'rc': 0,
        'rc_output': isis_database_verbose_output
    },
    'isis_database_lsp_id_verbose': {
        'args': ['sonic1.00-00', '--verbose'],
        'rc': 0,
        'rc_output': isis_database_lsp_id_verbose_output
    },
    'isis_database_unknown_lsp_id': {
        'args': ['sonic1'],
        'rc': 0,
        'rc_output': isis_database_unknown_lsp_id_output
    },
    'isis_database_invalid_help': {
        'args': ['?'],
        'rc': 2,
        'rc_output': isis_database_invalid_help_output
    },
    'isis_hostname': {
        'args': [],
        'rc': 0,
        'rc_output': isis_hostname_output
    },
    'isis_hostname_invalid_help': {
        'args': ['?'],
        'rc': 2,
        'rc_output': isis_hostname_invalid_help_output
    },
    'isis_interface': {
        'args': [],
        'rc': 0,
        'rc_output': isis_interface_output
    },
    'isis_interface_ifname': {
        'args': ['PortChannel0002'],
        'rc': 0,
        'rc_output': isis_interface_ifname_output
    },
    'isis_interface_verbose': {
        'args': ['--verbose'],
        'rc': 0,
        'rc_output': isis_interface_verbose_output
    },
    'isis_interface_ifname_verbose': {
        'args': ['PortChannel0002', '--verbose'],
        'rc': 0,
        'rc_output': isis_interface_ifname_output
    },
    'isis_interface_unknown_ifname': {
        'args': ['sonic1'],
        'rc': 2,
        'rc_output': isis_interface_unknown_ifname_output
    },
    'show_run_isis_output': {
        'args': [],
        'rc': 0,
        'rc_output': show_run_isis_output
    },
    'show_run_isis_config_db_output': {
        'args': ['--config_db'],
        'rc': 0,
        'rc_output': show_run_isis_config_db_output
    },
    'show_run_isis_invalid_help_output': {
        'args': ['?'],
        'rc': 2,
        'rc_output': show_run_isis_invalid_help_output
    },
    'isis_summary_output': {
        'args': [],
        'rc': 0,
        'rc_output': isis_summary_output
    },
    'isis_summary_json_output': {
        'args': ['--json'],
        'rc': 0,  
        'rc_output': isis_summary_json_output
    },
    'isis_summary_invalid_help_output': {
        'args': ['?'],
        'rc': 2,
        'rc_output': isis_summary_invalid_help_output
    },
}
