-- for sqlite3

CREATE TABLE billing (
    hour INTEGER,
    multiplier REAL
);

.mode csv
.separator ","
.import billing.csv billing

CREATE TABLE access_log (
    client_ip TEXT,
    identity TEXT,
    username TEXT,
    timestamp TEXT,
    timezone TEXT,
    request TEXT,
    status TEXT,
    bytes INTEGER,
    ref TEXT,
    user_agent TEXT,
    unknown TEXT
);

.separator " "
.import uncommitted/access.log access_log




