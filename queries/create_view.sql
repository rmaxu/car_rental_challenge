CREATE OR REPLACE VIEW metrics_view AS
SELECT 
    car.car_id,
    COUNT(rental.rental_id) AS reservations,
    AVG(EXTRACT(EPOCH FROM rental.return_date - rental.pickup_date) / 3600) as avg_rental_time
FROM 
    rental 
LEFT JOIN 
    car
    ON rental.car_id = car.car_id
GROUP BY 
    car.car_id
ORDER BY
    reservations DESC,
    avg_rental_time DESC;