SELECT * FROM red_social.pets;

SELECT
pets.id,pets.name,pets.birthdate,
breeds.name as breed,
species.name as specie
FROM pets
JOIN breeds ON pets.breed_id = breeds.id
JOIN species ON breeds.specie_id=species.id
;

SELECT users.id as user_id,CONCAT_WS(" ",users.firstname,users.lastname) as fullname ,users.username,
pets.id as pet_id,pets.name,pets.birthdate,
breeds.name as breed,
species.name as specie
FROM users
LEFT JOIN pets ON users.id = pets.owner_id
LEFT JOIN breeds ON pets.breed_id = breeds.id
LEFT JOIN species ON breeds.specie_id=species.id
;



SELECT users.id as user_id,CONCAT_WS(" ",users.firstname,users.lastname) as fullname ,users.username,
GROUP_CONCAT(pets.name),
JSON_ARRAYAGG(breeds.name),
JSON_ARRAYAGG(species.name),
COUNT(pets.id)
FROM users
LEFT JOIN pets ON users.id = pets.owner_id
LEFT JOIN breeds ON pets.breed_id = breeds.id
LEFT JOIN species ON breeds.specie_id=species.id
GROUP BY user_id
;


SELECT 
    users.id AS user_id,
    CONCAT_WS(" ", users.firstname, users.lastname) AS fullname,
    users.username,
    GROUP_CONCAT(pets.name) AS pets,
    JSON_ARRAYAGG(breeds.name) AS breeds,
    JSON_ARRAYAGG(species.name) AS species,
    COUNT(pets.id) AS pet_count
FROM 
    users
LEFT JOIN 
    pets ON users.id = pets.owner_id
LEFT JOIN 
    breeds ON pets.breed_id = breeds.id
LEFT JOIN 
    species ON breeds.specie_id = species.id
GROUP BY 
    users.id
HAVING 
    JSON_CONTAINS(species, JSON_QUOTE("Canino"));

