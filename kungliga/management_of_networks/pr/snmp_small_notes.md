# Notes

good links: 
- https://www.youtube.com/watch?v=2IXP0TkwNJU
- https://www.youtube.com/watch?v=ZX-XGQoISHQ
- https://kb.paessler.com/en/topic/653-how-do-snmp-mibs-and-oids-work 
- https://docstore.mik.ua/orelly/networking_2ndEd/snmp/ch02_05.htm
- what is MIB 2 group: https://docstore.mik.ua/orelly/networking_2ndEd/snmp/ch02_05.htm
- MIB 2 goups' objects: https://www.ibm.com/support/knowledgecenter/en/SSGNTH_4.0.1/com.ibm.netcool_ssm_4.0.1.doc/rg/reference/appMIB2_overview_r.html 

Key terms:

**Object Identifier (OID)**

ID for object.
Example of objects:
- In printers, it is cartridge states
- In routers, they are incoming and outgoing traffic, packet loss, etc

Example:
- OID: 1.3.6.1.2.1.2.2.1.8
    - This ID is for temperature sensor ID of the Network Attached Storage (NAS).

More info: https://en.wikipedia.org/wiki/Object_identifier

**Management Information Base (MIB)**

Word based OID. Example: SYNOLOGY-SYSTEM-MIB::temperature.0

According to wikipedia, MIB is a database used for managing the entities in a communication network. The database is hierarchical and each entry is addressed through OID.

