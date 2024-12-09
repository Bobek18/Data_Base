-- Вставка даних для таблиці `AlertContact`
INSERT INTO alertcontacts (contact_name, contact_phone)
VALUES ('John Doe', '+380501234567'),
       ('Jane Smith', '+380501234568'),
       ('Alice Brown', '+380501234569'),
       ('Bob White', '+380501234570'),
       ('Charlie Black', '+380501234571');

-- Вставка даних для таблиці `BatteryAlert`
INSERT INTO batteryalerts (alert_time, alert_type)
VALUES ('2024-12-10 14:00:00', 'Low Battery'),
       ('2024-12-10 15:00:00', 'Critical Battery'),
       ('2024-12-10 16:00:00', 'Battery Normal'),
       ('2024-12-10 17:00:00', 'Battery Charging'),
       ('2024-12-10 18:00:00', 'Battery Low');

-- Вставка даних для таблиці `BatteryStatus`
INSERT INTO batterystatus (battery_level, measurement_time, batteryalerts_alert_id)
VALUES (80, '2024-12-10 14:00:00', 1),
       (30, '2024-12-10 15:00:00', 2),
       (90, '2024-12-10 16:00:00', 3),
       (50, '2024-12-10 17:00:00', 4),
       (20, '2024-12-10 18:00:00', 5);

-- Вставка даних для таблиці `HeartRateAlert`
INSERT INTO heartratealerts (alert_time, alert_type)
VALUES ('2024-12-10 14:00:00', 'Heart Rate High'),
       ('2024-12-10 15:00:00', 'Heart Rate Normal'),
       ('2024-12-10 16:00:00', 'Heart Rate Low'),
       ('2024-12-10 17:00:00', 'Heart Rate Critical'),
       ('2024-12-10 18:00:00', 'Heart Rate Elevated');

-- Вставка даних для таблиці `HeartRate`
INSERT INTO heartrates (heart_rate, measurement_time, user_name, heartratealerts_alert_id)
VALUES (120, '2024-12-10 14:00:00', 'John Doe', 1),
       (75, '2024-12-10 15:00:00', 'Jane Smith', 2),
       (60, '2024-12-10 16:00:00', 'Alice Brown', 3),
       (150, '2024-12-10 17:00:00', 'Bob White', 4),
       (100, '2024-12-10 18:00:00', 'Charlie Black', 5);

-- Вставка даних для таблиці `LocationAlert`
INSERT INTO locationalerts (alert_time, alert_type)
VALUES ('2024-12-10 14:00:00', 'Out of Zone'),
       ('2024-12-10 15:00:00', 'In Zone'),
       ('2024-12-10 16:00:00', 'Location Safe'),
       ('2024-12-10 17:00:00', 'Location Critical'),
       ('2024-12-10 18:00:00', 'Location Normal');

-- Вставка даних для таблиці `Location`
INSERT INTO locations (latitude, longitude, measurement_time, locationalerts_alert_id)
VALUES (50.4501, 30.5002, '2024-12-10 14:00:00', 1),
       (50.4601, 30.5102, '2024-12-10 15:00:00', 2),
       (50.4701, 30.5202, '2024-12-10 16:00:00', 3),
       (50.4801, 30.5302, '2024-12-10 17:00:00', 4),
       (50.4901, 30.5402, '2024-12-10 18:00:00', 5);

-- Вставка даних для таблиці `Smartwatch`
INSERT INTO smartwatches (serial_number, user_name, locations_location_id, alertcontacts_contact_id, heartrates_rate_id, batterystatus_battery_id)
VALUES ('SN1234567890', 'John Doe', 1, 1, 1, 1),
       ('SN1234567891', 'Jane Smith', 2, 2, 2, 2),
       ('SN1234567892', 'Alice Brown', 3, 3, 3, 3),
       ('SN1234567893', 'Bob White', 4, 4, 4, 4),
       ('SN1234567894', 'Charlie Black', 5, 5, 5, 5);

-- Вставка даних для таблиці `NotificationSetting`
INSERT INTO NotificationSettings (is_heart_rate_alert_enabled, is_battery_alert_enabled, is_location_alert_enabled, smartwatch_watch_id)
VALUES (TRUE, TRUE, TRUE, 1),
       (FALSE, TRUE, FALSE, 2),
       (TRUE, FALSE, TRUE, 3),
       (TRUE, TRUE, FALSE, 4),
       (FALSE, FALSE, TRUE, 5);
