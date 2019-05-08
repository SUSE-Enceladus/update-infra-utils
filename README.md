update-infra-utils
==================

A collection of utilities used to help with maintenance and setup of the SUSE
operated update infrastructure in Public Cloud Frameworks.

## update-server-repo-setup

Code to configure repositories on an update server.

The `generate-repos-config` generates a json formatted configuration file
using another json formatted configuration file as directives for the
repository information to extract from SCC, SUSE Customer Center. An example
of the input configuration file is shown in `product_config.json.example`.
The generated file is used by the `enable-rmt-repos` script to enable
repositories on an RMT server. The configuration file produced by
`generate-repos-config` is also used by the `check_rmt_repos` utility
maintained in the [monitoring] (https://github.com/SUSE-Enceladus/monitoring)
project.

Example:
   generate-repos-config -i product_config.json.example -u $SCC_USERNAME -p $SCC_PASSWORD

This will generate a file named `rmt_repository_config.json` that can then
be used `enable-rmt-repos` to enable repositories for mirroring on an RMT
server. When place in `/etc/rmt-utils/rmt_repository_config.json` the file
functions as the configuration file for `check_rmt_repos`.
