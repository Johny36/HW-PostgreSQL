CREATE TABLE public."Product"
(
    id  		integer 		        PRIMARY KEY,
    name 		character varying(121),
    price_value numeric,
	price_unit 	character varying(5),
	bar_code	character varying(15)   UNIQUE,
	quantity	integer
);

--ALTER TABLE "Product"
  --  ADD COLUMN bar_code character varying;

 ---  HW1 
ALTER TABLE "Product"
    DROP COLUMN bar_code ;

--- HW2
INSERT INTO "Product"("ID", name, price_value, price_unit, bar_code, quantity)
	VALUES (1, 'First Product', 100, '1234567890123');

INSERT INTO "Product"("ID", name, price, bar_code)
	VALUES (2, 'Second Product', 200, '2234567890123');
INSERT INTO "Product"("ID", name, price, bar_code)
	VALUES (3, 'Third Product', 300, '3234567890123');
INSERT INTO "Product"("ID", name, price, bar_code)
	VALUES (4, 'Fourth Product', 450, '4234567890123');
SELECT * FROM "Product";

--UPDATE "Producte"     
-- SET price = 0;

----------Set price for 
--UPDATE "Producte"
-- SET price = 100;
-- WHERE id = 1;



SELECT * FROM "Product" where price < 250;

CREATE TABLE if not exists public."ClientsDB"
(   
	id integer, 
	name character varying ,
	is_vip boolean
)

INSERT INTO public."ClientsDB"("id", name, is_vip)
	VALUES (1, 'Ferrari', 1);

INSERT INTO public."ClientsDB"(id, name, is_vip)
	VALUES (2, 'Lamburghini', 1);

INSERT INTO public."ClientsDB"(id, name, is_vip)
	VALUES (3, 'VW', 0);

INSERT INTO public."ClientsDB"(id, name, is_vip)
	VALUES (4, 'Bugatti', 1);

INSERT INTO public."ClientsDB"(id, name, is_vip)
	VALUES (5, 'AUDI', 0);

INSERT INTO public."ClientsDB"(id, name, is_vip)
	VALUES (6, 'BMW', 0);

SELECT * FROM "ClientsDB";

---HW5---
SELECT * from "ClientsDB" where length(name)>5;

--HW6---
DELETE FROM public."ClientsDB" WHERE id = 5;
--HW7---
SELECT * from "ClientsDB" WHERE is_vip = 0;

---HW8---
ALTER TABLE public."ClientsDB"
ADD COLUMN EMail character varying;
---HW9---
UPDATE public."ClientsDB"
	SET email = 'ferrari@protonmail.com'
	WHERE id = 1;

UPDATE public."ClientsDB"
	SET email = 'lamburghini@gmail.com'
	WHERE id = 2;

UPDATE public."ClientsDB"
	SET email = 'VW@Volkswagen.com'
	WHERE id = 3;

UPDATE public."ClientsDB"
	SET email = 'bugatti@bugatti.com'
	WHERE id = 4;

UPDATE public."ClientsDB"
	SET email = 'bmwgroup@bmwgroupe.com'
	WHERE id = 6;