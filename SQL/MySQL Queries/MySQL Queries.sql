SELECT customer.first_name, customer.last_name, customer.email, address
FROM customer 
JOIN address
ON customer.address_id = address.address_id
WHERE city_id = 312;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
From film
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category 
ON category.category_id = film_category.category_id
WHERE category.name = 'comedy';

SELECT actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name, film.title, film.description, film.release_year
FROM actor
JOIN film_actor
ON actor.actor_id = film_actor.actor_id
JOIN film
ON film.film_id = film_actor.film_id
WHERE actor.actor_id = 5;

SELECT CONCAT(customer.first_name,' ', customer.last_name) AS custmer_name, customer.email, address
FROM customer
JOIN address
ON customer.address_id = address.address_id
WHERE customer.store_id = 1 AND 
city_id = 1 OR 
city_id = 42 OR 
city_id = 312 OR 
city_id =459;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
JOIN film_actor
ON film.film_id = film_actor.film_id
WHERE film.rating = 'G'AND 
film.special_features LIKE '%behind the scenes%' AND
actor_id = 15;

SELECT film.film_id, film.title, film_actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name)
FROM film
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
WHERE film.rental_rate = 2.99 AND
category.name = 'drama';

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, actor.first_name, actor.last_name 
FROM film

JOIN film_category 
ON film.film_id = film_category.film_id
JOIN category
ON category.category_id = film_category.category_id
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'sandra' AND
actor.last_name = 'kilmer' AND
category.name = 'action';