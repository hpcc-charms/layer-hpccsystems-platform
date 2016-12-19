# Overview

[HPCC Systems,](http://HPCCSystems.com) an open source High Performance Computing Cluster, is a massive parallel-processing computing platform that solves Big Data problems. HPCC Systems is an enterprise-proven platform for manipulating, transforming, querying, and data warehousing Big Data. Built by LexisNexis, the HPCC platform has helped it grow to a $1.5 billion information solutions company.

The HPCC Systems architecture incorporates a data query engine (called Thor) and a data delivery engine (called Roxie), as well as common middleware support components, an external communications layer, client interfaces which provide both end-user services and system management tools, and auxiliary components to support monitoring and to facilitate loading and storing of file system data from external sources.

An HPCC environment can include only Thor clusters, or both Thor and Roxie clusters. The HPCC Juju charm creates a cluster which contains both, but you can customize it after deployment.

See [How it Works](http://www.hpccsystems.com/Why-HPCC/How-it-works)  for more details.

See [System Requirements](http://hpccsystems.com/download/docs/system-requirements) for hardware details.
> Please note, your Juju instance must have at least 4GB of RAM. To increase the memory for a unit, run this command:
   `juju set-constraints mem=4G`

The HPCC Juju Charm encapsulates best practice configurations for the HPCC  Systems Platform.  You can use a Juju Charm to stand up an HPCC Platform on:

- Local Provider (LXC)

- Amazon Web Services Cloud


# Usage

## General Usage

1. To deploy a single HPCC node:

    `juju deploy hpcc <name>`

    **For example:**

        'juju deploy hpcc myhpcc`

1. To check the status , run
        juju status

        You also can log into the node to check if HPCC is properly installed.

        `juju ssh myhpcc/0`

1. To deploy a HPCC cluster
    `juju deploy hpcc <master name>`
    `juju deploy hpcc <cluster name>`
    `juju add-relation <master name>:support-node  <cluster name>:cluster`

ECLWatch ip is the public ip of "master name"

1.  Once HPCC is properly installed, you can add more nodes using this command:

        `juju add-unit <cluster_name> -n <#_of_nodes_to_add>`

    **For example:**

        `juju add-unit cluster -n 3`

1. You can expose the HPCC cluster by running:

       `juju expose <master_name>`

Once the service is deployed, running, and exposed, you can find the address for the ECL Watch Web interface by running juju status and looking for the public-address field. Type that address plus :8010 for the port.

For example, **nnn.nnn.nnn.nnn:8010**.




# Configuration

When you use the `juju add-unit` command to add nodes, scripts are called automatically to provide a default configuration.

### ssh-keys ###
The hpcc charm automatically generates a key pair  (*id\_rsa*  &  *id\_rsa.pub*) to configure nodes.

If you already have your own key pair and wish to use it, copy and paste their contents into the two variables (*ssh-key-public* and *ssh-key-private*) in the configuration file (config.yaml) or in the Juju canvas configuration settings.

Alternately, you can set these using this command:

    juju set <hpcc service name> ssh-key-public=<public key> ssh-key-private=<private key>

###To update from prior version

You can set the **hpcc-version** in the configuration file (config.yaml) or in the Juju canvas configuration settings.

Alternately, you can set these using this command:
    juju set <hpcc service name> hpcc-version=<new version> package-checksum=<checksum string>

### Verifying the checksum
The charm uses an md5sum to verify the checksum of the HPCC platform  package before installing.

For this version of the charm, it is set to check the md5sum for the Community Edition Version 5.4.2-1 for Ubuntu 14.04 amd64. To verify a different version, edition, or OS version, change the value of the md5sum in the package-checksum variable in config.yaml. You can get other package checksums from [http://hpccsystems.com/download](http://hpccsystems.com/download)

###To reconfigure your topology

You can reconfigure the topology of your system by setting the values for **support-nodes, slaves-per-node, roxie-ratio, thor-ratio** in the configuration file (config.yaml) or in the Juju canvas configuration settings.

Alternately, you can set these using this command:

    juju set <hpcc service name> roxie-ratio=<floating point value 0.0 – 1.0> > thor-ratio=<floating point value 0.0 – 1.0>

### Ports

The charm automatically opens for external access, the following ports:

- Port **8010** for ECLWatch access
- Port **8002** for WsECL access.
- Port **9876** for direct Roxie access
- Port **8015** for Configuration Manager access.

### Next Steps ###

After deploying and adding nodes, you can tweak various options to optimize your HPCC deployment to meet your needs.

See [HPCC Systems Web site](http://HPCCSystems.com) for more details.


# HPCC Systems Contact Information

[HPCC Systems Web site](http://HPCCSystems.com)

For support, visit the HPCC Community Forums:
[HPCC Community Forums](http://hpccsystems.com/bb/index.php?sid=0bda2dddb2ea50418357171d33b11e5f)
