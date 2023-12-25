# 0x14-mysql
These MySQL-related tasks involve setting up MySQL on servers, creating users, configuring databases, and establishing a primary-replica infrastructure with data backup procedures. Each task contributes to the robustness, security, and reliability of the MySQL setup.

Here's an overview of the tasks:

### Task 0: Install MySQL
- **Objective**: Install MySQL 5.7.x on both `web-01` and `web-02`.
- **Instructions**: Ensure MySQL is installed on both servers with the specified version.

### Task 1: Let us in!
- **Objective**: Create a MySQL user named `holberton_user` on both servers with specific permissions.
- **Instructions**: Grant `holberton_user` access to check the primary/replica status of databases on `web-01` and `web-02`.

### Task 2: If only you could see what I've seen with your eyes
- **Objective**: Create a database named `tyrell_corp` on `web-01` and add a table named `nexus6` with at least one entry.
- **Instructions**: Ensure the `holberton_user` has `SELECT` permissions on the `nexus6` table.

### Task 3: Quite an experience to live in fear, isn't it?
- **Objective**: Create a new user named `replica_user` on the primary MySQL server (`web-01`) with appropriate permissions for replication.
- **Instructions**: Grant `replica_user` the necessary replication permissions on `web-01`.

### Task 4: Setup a Primary-Replica infrastructure using MySQL
- **Objective**: Establish a primary-replica infrastructure with MySQL.
- **Instructions**: Configure `web-01` as the primary and `web-02` as the replica, setting up MySQL replication for the database named `tyrell_corp`. Provide configuration files for both servers (`my.cnf` or `mysqld.cnf`).

### Task 5: MySQL backup
- **Objective**: Create a Bash script that generates a MySQL dump, compresses it into a tar.gz archive, and names it according to the date.
- **Instructions**: The script should dump all MySQL databases, compress the dump into a tar.gz file with the date as the filename, and use the `root` user for database access.
