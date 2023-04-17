1.  SELECT name, language, Percentage FROM country
    JOIN countrylanguage ON countrylanguage.CountryCode = country.Code
    WHERE countrylanguage.language = "Slovene"
    ORDER BY Percentage DESC;

2. SELECT country.name, COUNT(city.CountryCode) AS city_count
FROM country
JOIN city ON country.code = country.code
GROUP BY country.name
ORDER BY city_count DESC;

3. SELECT name
FROM city
WHERE CountryCode = "MEX" AND Population > 500000
ORDER BY Population DESC;

4. SELECT Language
FROM countrylanguage
WHERE Percentage > 89
ORDER BY Percentage DESC;

5. SELECT *
FROM country
WHERE SurfaceArea < 501 AND Population > 100000;

6. SELECT *
FROM country
WHERE GovernmentForm = "Constitutional Monarchy" AND Capital > 200 AND LifeExpectancy > 75;

7. SELECT country.name AS country_name, city.name AS city_name, city.district, city.population
FROM city
JOIN country ON city.CountryCode = country.code
WHERE country.name = 'Argentina' AND city.district = 'Buenos Aires' AND city.population > 500000;

8. SELECT region, COUNT(name) AS country_count
FROM country
GROUP BY region
ORDER BY country_count DESC;