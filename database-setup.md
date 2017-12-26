## To setup database follow the steps below
* The database that the app is developed with is postgresql 10.1
* **Windows**
    * Start psql 
    * Login as postgres user
    * To create database issue this command: `create database findtutor;`
    * To create user issue following command: `create user findtutor;`
    * Assign password to user: `alter user findtutor with encrypted password 'F1ndtut0r';`
    * Grant permissions on DB to user: `grant all privileges on database findtutor to findtutor;`