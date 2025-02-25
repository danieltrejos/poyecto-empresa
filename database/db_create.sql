-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS lender_mvp;
USE lender_mvp;

-- Crear la tabla Usuarios
CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    es_cliente BOOLEAN DEFAULT TRUE,
    estado BOOLEAN DEFAULT TRUE
);

-- Crear la tabla Prestamos
CREATE TABLE Prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prestamo_codigo VARCHAR(20) UNIQUE NOT NULL,
    tasa_interes FLOAT NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_final DATE NOT NULL,
    plazo_meses INT NOT NULL,
    monto FLOAT NOT NULL,
    saldo_pendiente FLOAT NOT NULL,
    estado VARCHAR(20) NOT NULL,
    cliente_id INT NOT NULL,
    usuario_id INT NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id) ON DELETE CASCADE
);

-- Crear la tabla Transacciones
CREATE TABLE Transacciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    monto FLOAT NOT NULL,
    fecha_transaccion DATETIME DEFAULT CURRENT_TIMESTAMP,
    tipo_transaccion VARCHAR(20) NOT NULL,
    prestamo_id INT NOT NULL,
    usuario_id INT NOT NULL,
    FOREIGN KEY (prestamo_id) REFERENCES Prestamos(id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id) ON DELETE CASCADE
);

-- Crear la tabla Roles
CREATE TABLE Roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE NOT NULL
);

-- Crear la tabla Permisos
CREATE TABLE Permisos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL
);

-- Crear tabla intermedia Usuarios_Roles (Muchos a Muchos)
CREATE TABLE Usuarios_Roles (
    usuario_id INT NOT NULL,
    rol_id INT NOT NULL,
    PRIMARY KEY (usuario_id, rol_id),
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (rol_id) REFERENCES Roles(id) ON DELETE CASCADE
);

-- Crear tabla intermedia Roles_Permisos (Muchos a Muchos)
CREATE TABLE Roles_Permisos (
    rol_id INT NOT NULL,
    permiso_id INT NOT NULL,
    PRIMARY KEY (rol_id, permiso_id),
    FOREIGN KEY (rol_id) REFERENCES Roles(id) ON DELETE CASCADE,
    FOREIGN KEY (permiso_id) REFERENCES Permisos(id) ON DELETE CASCADE
);