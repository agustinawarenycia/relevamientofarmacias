select @@VERSION;

--Creamos la base de datos
create database Relevamiento;
--Seleccionamos la base de datos a usar	
use Relevamiento;

-- CREAR un esquema dentro de la base de datos
create schema computadoras;


--create table Terminal.Omnibus.controll(
--nroControl int primary key identity (1,1) not null,
--codES int NOT NULL,
--patente varchar  NOT NULL,
--fecha date NOT NULL, --date	YYYY-MM-DD
--hora varchar(4) NOT NULL,
--dniChofer int	NOT NULL,
--codLoc int NOT NULL,
--cantPasajeros int NOT NULL,
--);

create table Relevamiento.computadoras.pc_Farmacias(
	nombre varchar(255) NOT NULL,
	ip varchar(255) not null,
	arquitectura_so varchar(255) not null,
	tipo_maquina varchar(255) not null,
	procesador varchar(255) not null,
	cores_fisicos int,
	cores_totales int,
	ram_tot varchar(255) not null,
	ram_usada varchar(255) not null,
	ram_disponible varchar(255) not null,
	espacio_tot_C varchar(255) not null,
	espacio_usado_C varchar(255) not null,
	espacio_disponible_C varchar(255) not null,
	espacio_tot_D varchar(255) not null,
	espacio_usado_D varchar(255) not null,
	espacio_disponible_D varchar(255) not null,
	anydesk varchar(255) not null,
	id_anydesk varchar(255) not null,
	CONSTRAINT PK_nombre_ip primary key (nombre, ip)
	)
	go


create table Relevamiento.computadoras.farmacia(
	idFarmacia varchar(255) primary key not null,
	nombreFcia varchar(255) not null,
	direccion varchar(255) not null

	)
	go

create table Relevamiento.computadoras.pc_almacenamiento(
	nombre varchar(255) primary key not null,
	info_txt varchar(255) not null,
)
go

--agregar pk

  ALTER TABLE farmacia
  ADD PRIMARY KEY (idFarmacia);



-- ALTER TABLE dbo.gasto 
--ADD CONSTRAINT  FK_gasto_consorcio FOREIGN KEY (idprovincia,idlocalidad,idconsorcio)  REFERENCES consorcio(idprovincia,idlocalidad,idconsorcio);

alter table Relevamiento.computadoras.farmacia
	ADD CONSTRAINT fk_nombre_ip FOREGEIN KEY(


	Create table consorcio	(idprovincia int,
                         idlocalidad int,
                         idconsorcio int, 
					     nombre varchar(50),
					     direccion varchar(250),					     
					     idzona int,	
						 idconserje int,	
						 idadmin int,	
					     Constraint PK_consorcio PRIMARY KEY (idprovincia, idlocalidad,idconsorcio),

						 Constraint FK_consorcio_pcia FOREIGN KEY (idprovincia,idlocalidad)  REFERENCES localidad(idprovincia,idlocalidad),
	)
go
-------------------

Create table gasto	(
						idgasto int identity,
						idprovincia int,
                         idlocalidad int,
                         idconsorcio int, 
					     periodo int,
					     fechapago datetime,					     
						 idtipogasto int,
						 importe decimal (8,2),	
					     Constraint PK_gasto PRIMARY KEY (idgasto),
						
						Constraint FK_gasto_consorcio FOREIGN KEY (idprovincia,idlocalidad,idconsorcio)  REFERENCES consorcio(idprovincia,idlocalidad,idconsorcio),
						Constraint FK_gasto_tipo FOREIGN KEY (idtipogasto)  REFERENCES tipogasto(idtipogasto)					     					     						 					     					     
							)
go