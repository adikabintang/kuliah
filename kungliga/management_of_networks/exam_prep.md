# SNMP

## Terms

### Manager

SNMP manager is a program that runs on the central device that manages the SNMP operations, connects and queries information from the SNMP agents.

### Agent

SNMP agent is a program that runs on the managed devices in an SNMP network.

### MIB

Management Information Base (MIB) is a collection of objects (such as incoming traffic, outgoing traffic in router; cartridge status on printers; etc) that are grouped and modeled for management purpose.

### object identifier (OID)

An Object Identifier (OID) uniquely identifies the object in the MIB tree. It consists of sequence of integers as the ID. Example: `1.3.6.1.2.1.6.13`.

## Strong Points of SNMP v1

- Simple protocols and operations
- Low complexity on agent side
- Ubiquity: many devices have SNMP features
- Well-tested: it has been used for a while, so it is widely understood and tested

## Limitations of SNMP v1

- Not suitable for a large network: the load of the manager might be too high
- Vulnerable: it does not have cryptographic features
- Limited expressiveness: only read and write a single scalar objects

## Other network management protocols
- Command-Line Interface (CLI)
- Syslog
- Netflow/IPFIX
- Netconf

# Distributed Management

## Approaches

### Hierarchies of SNMP agents

...

### Scrit-enabled agents (management by delegation)

- A management program injects a script `S` to all the managed nodes.
- S runs something, the result is sent back to the manager
- Use case: statistical aggregation and notification schemes

### Mobile agents

- A management program injects a mobile agent `MA` onto one node.
- After executing in one node, `MA` will move by itself to another node, taking its execution state.
- `MA` sends back to the manager in form of a message
- Use case: diagnosing and correcting problems on nodes, updating software on the nodes
- Big drawbacks: security, safety, complexity

### Peer-to-peer management

- There is management system, management plane, and managed system. See the slide.

## Peer-to-peer: Echo protocol

Echo protocol is polling.

### Application use-cases

- Distributed polling or estimation of a global aggregators
- Network search. Example: find set of routers that run IOS version x.
- Perform operations on nodes with given properties. Example: update module z on all routers that run IOS version x.

#### Terms

- Degree of a node: number of neighbors that a node has. 
  - `deg(G)`: max degree of any node on group `G`
- Diameter of a tree (`diam(G)`): the distance from the root to the farthest leave. It is not the same as the height [[geeksforgeeks](https://www.geeksforgeeks.org/diameter-of-a-binary-tree/)].

### Performance of Echo-based operations

- Processing load L: `L = deg(G)`
- Execution time T (time complexity): `T = O(diam(G))`

## Peer-to-peer: GAP protocol

GAP protocol is a push protocol.

### Performance of the GAP protocol

- Management traffic `M`
  - For GAP with rate control, `M` is limited to `r` messages per second for each link
- Processing load `L`: `L = O(r * deg(M))`
- Time for initialization: `diam(G)`
- Time for update of aggregate and reconfiguration due to node churn or failure: adding/removing a node takes at most `2 * diam(G)` rounds
- For a network graph with `diam(G) = O(log(N))`, the initialization time, the update time, and the reconfiguration time of GAP are all `O(log(N) * deg(G))`

 