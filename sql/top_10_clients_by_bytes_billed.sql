SELECT
    client_ip,
    SUM(bytes * multiplier) total_bytes_billed
FROM
    access_log
    INNER JOIN billing
        ON billing.hour = CAST(SUBSTR(access_log.timestamp, 14, 2) AS INTEGER)
GROUP BY
    client_ip
ORDER BY
    total_bytes_billed DESC
LIMIT 10;