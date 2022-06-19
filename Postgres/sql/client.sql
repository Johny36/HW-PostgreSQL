CREATE TABLE public."Client"
(
    id   		integer 		        PRIMARY KEY,
    name 		character varying(61),
    email    	character varying(121)  UNIQUE,
	phone   	character varying(21)   UNIQUE,
	is_vip  	boolean                 DEFAULT false
);