import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    database='tienda',
    user='mercatododb',
    password='',
    port='3306'

)

def get_db_cursor():
    return db.cursor(dictionary=True)



# #database con unos cuantos ejemplos:

# CREATE DATABASE tienda;

# USE tienda;

# -- Tabla usuarios
# CREATE TABLE usuarios (
#   ID_usuario INT NOT NULL AUTO_INCREMENT,
#   Nombre VARCHAR(100) NOT NULL,
#   cedula VARCHAR(20) NOT NULL,
#   fecha_registro DATE DEFAULT NULL,
#   rol ENUM('empleado', 'administrador') NOT NULL,
#   PRIMARY KEY (ID_usuario)
# );

# -- Tabla categoria_producto
# CREATE TABLE categoria_producto (
#   ID_categoria_producto INT NOT NULL AUTO_INCREMENT,
#   nombre_categoria VARCHAR(100) NOT NULL,
#   PRIMARY KEY (ID_categoria_producto)
# );

# -- Tabla proveedores
# CREATE TABLE proveedores (
#   ID_proveedor INT NOT NULL AUTO_INCREMENT,
#   Nombre_empresa VARCHAR(100) NOT NULL,
#   Nombre_representante_legal VARCHAR(100) NOT NULL,
#   tipo_proveedor VARCHAR(50) NOT NULL,
#   direccion VARCHAR(200) NOT NULL,
#   telefono VARCHAR(20) NOT NULL,
#   email VARCHAR(100) NOT NULL,
#   URL VARCHAR(200) DEFAULT NULL,
#   PRIMARY KEY (ID_proveedor)
# );

# -- Tabla producto
# CREATE TABLE producto (
#   ID_producto INT NOT NULL AUTO_INCREMENT,
#   nombre_producto VARCHAR(100) NOT NULL,
#   descripcion_producto TEXT DEFAULT NULL,
#   valor_producto DECIMAL(10, 2) NOT NULL,
#   ID_categoria_producto INT NOT NULL,
#   stock INT NOT NULL,
#   ID_proveedor INT NOT NULL,
#   fecha_ingreso DATE DEFAULT NULL,
#   PRIMARY KEY (ID_producto),
#   FOREIGN KEY (ID_categoria_producto) REFERENCES categoria_producto(ID_categoria_producto),
#   FOREIGN KEY (ID_proveedor) REFERENCES proveedores(ID_proveedor)
# );

# -- Tabla ventas
# CREATE TABLE ventas (
#   ID_venta INT NOT NULL AUTO_INCREMENT,
#   fecha_venta DATE DEFAULT NULL,
#   ID_usuario INT NOT NULL,
#   total DECIMAL(10, 2) DEFAULT NULL,
#   PRIMARY KEY (ID_venta),
#   FOREIGN KEY (ID_usuario) REFERENCES usuarios(ID_usuario)
# );

# -- Tabla detalle_ventas
# CREATE TABLE detalle_ventas (
#   ID_detalle_venta INT NOT NULL AUTO_INCREMENT,
#   ID_venta INT NOT NULL,
#   ID_producto INT NOT NULL,
#   cantidad INT NOT NULL,
#   valor_venta_producto DECIMAL(10, 2) NOT NULL,
#   PRIMARY KEY (ID_detalle_venta),
#   FOREIGN KEY (ID_venta) REFERENCES ventas(ID_venta),
#   FOREIGN KEY (ID_producto) REFERENCES producto(ID_producto)
# );

# -- Tabla compras
# CREATE TABLE compras (
#   ID_compra INT NOT NULL AUTO_INCREMENT,
#   fecha_compra DATE DEFAULT NULL,
#   valor_compra DECIMAL(10, 2) DEFAULT NULL,
#   PRIMARY KEY (ID_compra)
# );

# -- Tabla detalle_compra
# CREATE TABLE detalle_compra (
#   ID_detalle_compra INT NOT NULL AUTO_INCREMENT,
#   ID_compra INT NOT NULL,
#   ID_producto INT NOT NULL,
#   cantidad INT NOT NULL,
#   ID_proveedor int not null,
#   valor_compra_producto DECIMAL(10, 2) NOT NULL,
#   PRIMARY KEY (ID_detalle_compra),
#   FOREIGN KEY (ID_compra) REFERENCES compras(ID_compra),
#   FOREIGN KEY (ID_producto) REFERENCES producto(ID_producto),
#   FOREIGN KEY (ID_proveedor) REFERENCES proveedores(ID_proveedor)
# );

# -- Tabla devoluciones
# CREATE TABLE devoluciones (
#   ID_devolucion INT NOT NULL AUTO_INCREMENT,
#   fecha_devolucion date default null,
#   PRIMARY KEY (ID_devolucion)
# );

# create table detalle_devolucion (
# ID_devolucion int not null,
# ID_detalle_devolucion int not null auto_increment,
# ID_producto int not null,
# descripcion varchar(30) not null,
# cantidad int not null,
# retorno_inventario boolean,
# primary key (ID_detalle_devolucion),
# foreign key (ID_producto) references producto (ID_producto),
# foreign key (ID_devolucion) references devoluciones (ID_devolucion)
# );


# CREATE TABLE admin (
#   ID_admin INT NOT NULL AUTO_INCREMENT,
#   nombre VARCHAR(100) NOT NULL,
#   cc VARCHAR(20) NOT NULL,
#   PRIMARY KEY (ID_admin)
# );




# insert into usuarios (nombre, cedula, fecha_registro) values
# ("Danilo Torres",1035700584, '2024-04-02');

# #new

# INSERT INTO categoria_producto (nombre_categoria) VALUES
#     ('Electrónica'),
#     ('Aseo'),
#     ('Hogar');

# INSERT INTO proveedores (Nombre_empresa, Nombre_representante_legal, tipo_proveedor, direccion, telefono, email, URL) VALUES
#     ('ElectroTech S.A.S.', 'Juan Pérez', 'Electrónica', 'Calle 123, Ciudad', '3123456789', 'info@electrotech.com', 'https://www.electrotech.com'),
#     ('AseoTotal Ltda.', 'María Gómez', 'Aseo', 'Carrera 456, Pueblo', '3209876543', 'contacto@aseototal.com', 'https://www.aseototal.com'),
#     ('HogarPerfecto E.U.', 'Pedro Rodríguez', 'Hogar', 'Avenida 789, Villa', '3101234567', 'ventas@hogarperfecto.com', 'https://www.hogarperfecto.com');

# -- Productos de Electrónica
# INSERT INTO producto (nombre_producto, descripcion_producto, valor_producto,  ID_categoria_producto, stock, ID_proveedor, fecha_ingreso) VALUES
#     ('Audífonos', 'Audífonos inalámbricos', 80000, 1, 50, 1, '2024-07-09'),
#     ('Mouse', 'Mouse inalámbrico', 25000,  1, 30, 1, '2024-07-09'),
#     ('Teclado', 'Teclado mecánico', 120000, 1, 20, 2, '2024-07-09');

# -- Productos de Hogar
# INSERT INTO producto (nombre_producto, descripcion_producto, valor_producto, ID_categoria_producto, stock, ID_proveedor, fecha_ingreso) VALUES
#     ('Sartén Antiadherente', 'Sartén de 24 cm', 30000, 3, 25, 3, '2024-07-09'),
#     ('Juego de Toallas', 'Toallas de algodón, paquete de 3 unidades', 25000, 3, 35, 3, '2024-07-09'),
#     ('Lámpara de Mesa', 'Lámpara de mesa LED', 50000, 3, 15, 1, '2024-07-09');


# insert into admin (nombre, cc) values
# ("Daniel Arredondo", 123456);



# #new data

# USE tienda;

# -- Insertar más datos de ventas y detalle ventas
# INSERT INTO ventas (ID_usuario, fecha_venta, total) VALUES
#     (1, '2024-07-10', 160000),
#     (1, '2024-07-11', 75000);

# INSERT INTO detalle_ventas (ID_venta, ID_producto, valor_venta_producto, cantidad) VALUES
#     (1, 1, 80000, 1),
#     (1, 2, 25000, 1),
#     (2, 5, 25000, 3);

# -- Insertar datos en la tabla compras (sin ID_proveedor)
# INSERT INTO compras (fecha_compra, valor_compra) VALUES
#     ('2024-07-08', 450000.00),
#     ('2024-07-07', 200000.00);

# -- Insertar datos en la tabla detalle_compra (con ID_proveedor)
# INSERT INTO detalle_compra (ID_compra, ID_producto, cantidad, ID_proveedor, valor_compra_producto) VALUES
#     (1, 1, 30, 1, 80000),
#     (1, 3, 15, 2, 120000),
#     (2, 4, 20, 3, 30000),
#     (2, 5, 10, 3, 25000);


# -- Insertar datos en usuarios (empleados)
# INSERT INTO usuarios (nombre, cedula, fecha_registro, rol) VALUES
#     ("Danilo Torres", 1035700584, '2024-04-02', 'empleado'),
#     ("Ana María", 1234567890, '2024-04-02', 'empleado'),
#     ("Carlos Rodríguez", 2345678901, '2024-05-15', 'empleado'),
#     ("Laura Gómez", 3456789012, '2024-06-20', 'empleado');

# -- Insertar datos en categoria_producto
# INSERT INTO categoria_producto (nombre_categoria) VALUES
#     ('Electrónica'),
#     ('Aseo'),
#     ('Hogar');

# -- Insertar datos en proveedores
# INSERT INTO proveedores (Nombre_empresa, Nombre_representante_legal, tipo_proveedor, direccion, telefono, email, URL) VALUES
#     ('ElectroTech S.A.S.', 'Juan Pérez', 'Electrónica', 'Calle 123, Ciudad', '3123456789', 'info@electrotech.com', 'https://www.electrotech.com'),
#     ('AseoTotal Ltda.', 'María Gómez', 'Aseo', 'Carrera 456, Pueblo', '3209876543', 'contacto@aseototal.com', 'https://www.aseototal.com'),
#     ('HogarPerfecto E.U.', 'Pedro Rodríguez', 'Hogar', 'Avenida 789, Villa', '3101234567', 'ventas@hogarperfecto.com', 'https://www.hogarperfecto.com');

# -- Insertar datos en producto
# -- Productos de Electrónica
# INSERT INTO producto (nombre_producto, descripcion_producto, valor_producto, ID_categoria_producto, stock, ID_proveedor, fecha_ingreso) VALUES
#     ('Audífonos', 'Audífonos inalámbricos', 80000, 1, 50, 1, '2024-07-09'),
#     ('Mouse', 'Mouse inalámbrico', 25000, 1, 30, 1, '2024-07-09'),
#     ('Teclado', 'Teclado mecánico', 120000, 1, 20, 2, '2024-07-09');

# -- Productos de Hogar
# INSERT INTO producto (nombre_producto, descripcion_producto, valor_producto, ID_categoria_producto, stock, ID_proveedor, fecha_ingreso) VALUES
#     ('Sartén Antiadherente', 'Sartén de 24 cm', 30000, 3, 25, 3, '2024-07-09'),
#     ('Juego de Toallas', 'Toallas de algodón, paquete de 3 unidades', 25000, 3, 35, 3, '2024-07-09'),
#     ('Lámpara de Mesa', 'Lámpara de mesa LED', 50000, 3, 15, 1, '2024-07-09');

# -- Insertar datos en ventas
# INSERT INTO ventas (ID_usuario, fecha_venta, total) VALUES
#     (1, '2024-07-10', 160000),
#     (1, '2024-07-11', 75000);

# -- Insertar datos en detalle_ventas
# INSERT INTO detalle_ventas (ID_venta, ID_producto, valor_venta_producto, cantidad) VALUES
#     (1, 1, 80000, 1),
#     (1, 2, 25000, 1),
#     (2, 5, 25000, 3);

# -- Insertar datos en compras
# INSERT INTO compras (fecha_compra, valor_compra) VALUES
#     ('2024-07-08', 450000.00),
#     ('2024-07-07', 200000.00);

# -- Insertar datos en detalle_compra
# INSERT INTO detalle_compra (ID_compra, ID_producto, cantidad, ID_proveedor, valor_compra_producto) VALUES
#     (1, 1, 30, 1, 80000),
#     (1, 3, 15, 2, 120000),
#     (2, 4, 20, 3, 30000),
#     (2, 5, 10, 3, 25000);

# -- Insertar datos en devoluciones
# INSERT INTO devoluciones (fecha_devolucion) VALUES
#     ('2024-07-12'),
#     ('2024-07-13');

# -- Insertar datos en detalle_devolucion
# INSERT INTO detalle_devolucion (ID_devolucion, ID_producto, descripcion, cantidad, retorno_inventario) VALUES
#     (1, 1, 'Producto defectuoso',1, 1),
#     (1, 2, 'No cumple con las expectativas',3, 0),
#     (2, 5, 'Tamaño incorrecto',2, 1);

# -- Insertar datos en admin
# INSERT INTO admin (nombre, cc) VALUES
#     ("Daniel Arredondo", 123456);


# #drop database tienda;




