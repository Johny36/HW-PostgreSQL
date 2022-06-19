CREATE TABLE public."Bag"
(
    id  		integer 		PRIMARY KEY,
	client_id  	integer         NOT NULL
);

ALTER TABLE public."Bag"
ADD     CONSTRAINT fk_bag FOREIGN KEY(client_id)
REFERENCES "Client"(id);