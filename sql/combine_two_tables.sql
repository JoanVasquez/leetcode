-- Select firstName and lastName from the Person table.
-- Use LEFT JOIN to bring in city and state from Address.
-- Match rows on the shared key: Person.personId = Address.personId.
--
-- This guarantees:
--  All people are returned.
--  If a person has no address, the city and state will be NULL.
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | personId    | int     |
-- | lastName    | varchar |
-- | firstName   | varchar |
-- +-------------+---------+
-- personId is the primary key (column with unique values) for this table.
-- This table contains information about the ID of some persons and their first and last names.
--
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | addressId   | int     |
-- | personId    | int     |
-- | city        | varchar |
-- | state       | varchar |
-- +-------------+---------+
-- addressId is the primary key (column with unique values) for this table.
-- Each row of this table contains information about the city and state of one 

SELECT firstName, lastName, Address.city, Address.state FROM Person LEFT JOIN Address ON Person.personId = Address.personId;

