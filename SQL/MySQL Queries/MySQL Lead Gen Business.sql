SELECT * FROM billing;

SELECT * FROM clients;

SELECT * FROM leads;

SELECT * FROM sites;

-- get the total revenue for March of 2012?
SELECT billing.charged_datetime AS charged_date, SUM(billing.amount) AS revenue
FROM billing
WHERE billing.charged_datetime LIKE '%2012-03%';

-- get total revenue collected from the client with an id of 2?
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_2, SUM(billing.amount)as revenue
FROM clients
JOIN billing ON clients.client_id = billing.client_id
WHERE clients.client_id = 2;

-- get all the sites that client=10 owns?
SELECT clients.client_id, sites.domain_name
FROM clients
JOIN sites
ON clients.client_id = sites.client_id
WHERE clients.client_id = 10;

-- get total # of sites created per month per year for the client with an id of 1? What about for client=20?
SELECT sites.client_id, COUNT(sites.site_id) AS number_sites, DATE_FORMAT(sites.created_datetime, '%M') AS month_created, DATE_FORMAT(sites.created_datetime, '%Y') AS year_created
FROM sites
WHERE sites.client_id = 1
GROUP BY month_created, year_created
ORDER BY year_created, month_created;


SELECT sites.client_id, COUNT(sites.site_id) AS number_sites, DATE_FORMAT(sites.created_datetime, '%M') AS month_created, DATE_FORMAT(sites.created_datetime, '%Y') AS year_created
FROM sites
WHERE sites.client_id = 20
GROUP BY month_created, year_created;

-- get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011? 
SELECT sites.domain_name, COUNT(leads.site_id) AS num_leads, DATE_FORMAT(leads.registered_datetime, '%M %D %Y') AS date_generated
FROM sites
JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-02-15' 
GROUP BY sites.domain_name;
  
-- get a list of client names and the total # of leads we've generated for each of our clients 
-- between January 1, 2011 to December 31, 2011?
SELECT CONCAT(clients.first_name,' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS num_leads
FROM clients
JOIN sites
ON clients.client_id = sites.client_id
JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31' 
GROUP BY clients.client_id;

-- get a list of client names and the total # of leads we've generated for each client each month 
-- between months 1 - 6 of Year 2011?
SELECT CONCAT(clients.first_name,' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS num_leads, DATE_FORMAT
(leads.registered_datetime, '%M') AS month_generated
FROM clients
JOIN sites
ON clients.client_id = sites.client_id
JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-06-30' 
GROUP BY leads.registered_datetime;

-- get a list of client names and the total # of leads we've generated for each of our clients' sites 
-- between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second 
-- query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.
SELECT CONCAT(clients.first_name,' ', clients.last_name) AS client_name, sites.domain_name, COUNT(leads.leads_id) AS num_leads, leads.registered_datetime 
FROM clients
JOIN sites
ON clients.client_id = sites.client_id
JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY sites.domain_name
ORDER BY clients.client_id, num_leads DESC;

SELECT CONCAT(clients.first_name,' ', clients.last_name) AS client_name, sites.domain_name, COUNT(leads.leads_id) AS num_leads
FROM clients
JOIN sites
ON clients.client_id = sites.client_id
JOIN leads
ON sites.site_id = leads.site_id
GROUP BY sites.domain_name
ORDER BY clients.client_id, num_leads DESC;

-- retrieves total revenue collected from each client for each month of the year. Order it by client id
SELECT CONCAT(clients.first_name,' ', clients.last_name) AS client_name, SUM(billing.amount) AS total_revenue, DATE_FORMAT(billing.charged_datetime, '%M') AS 'month_charged', DATE_FORMAT(billing.charged_datetime, '%Y') AS 'year_charged'
FROM clients
JOIN billing
ON clients.client_id = billing.client_id
GROUP BY client_name, MONTH(billing.charged_datetime), YEAR(billing.charged_datetime)  
ORDER BY clients.client_id, YEAR(billing.charged_datetime), MONTH(billing.charged_datetime);



-- retrieves all the sites that each client owns. Group the results so that each row shows a new client. It will 
-- become clearer when you add a new field called 'sites' that has all the sites that the client owns. 
-- SELECT CONCAT(clients.first_name,' ', clients.last_name) AS client_name, GROUP_CONCAT(' ',sites.domain_name) AS sites
FROM clients
JOIN sites
ON clients.client_id = sites.client_id
GROUP BY clients.client_id

  
  