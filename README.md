# miv_top
## Install
1. Create a new virtual environment (optional)
1. `python setup.py install,`Or you can also use package management tool to install according to requirement.txt, but we recommend the first one.  
## Usage
### View current usage
only type in mivtop  
**（base）#root: ****mivtop****
### Monitor
`config.yaml` it consists four parts: 

- **database**：Target database ip, port, table, user, passwd...
- **server**： Target server ip，users which is configured for database server.
- **email**：It is configured for eamil server(email sender), email content style, receivers.
- **log**：It is configured for log information. 
## Test
The test.py is used to test the modules in the project.
## Dir & files

- database: database operations
- mail: email operations
- top: resource acquisition
- ui: ui design
- utils: utils for coding (logging)
- config.yaml: project configure
- monitor.py: monitor process entrance
- setup.py: pack the project
- test.py: test
