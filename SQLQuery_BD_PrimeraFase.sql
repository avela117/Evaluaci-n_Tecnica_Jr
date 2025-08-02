CREATE DATABASE bd_et;

USE bd_et

CREATE TABLE Categoria (
    CodigoCategoria INT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL
);
GO

CREATE TABLE Producto (
    CodigoProducto INT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    CodigoCategoria INT,
    FOREIGN KEY (CodigoCategoria) REFERENCES Categoria(CodigoCategoria)
);
GO

CREATE TABLE Venta (
    CodigoVenta INT PRIMARY KEY,
    Fecha DATE NOT NULL,
    CodigoProducto INT,
    CodigoVentaRelacionado INT, -- Clave foránea autorreferencial
    FOREIGN KEY (CodigoProducto) REFERENCES Producto(CodigoProducto),
    FOREIGN KEY (CodigoVentaRelacionado) REFERENCES Venta(CodigoVenta)
);
GO

INSERT INTO Categoria (CodigoCategoria, Nombre) VALUES
(1, 'Smartphones'),
(2, 'Laptops'),
(3, 'Tablets'),
(4, 'Auriculares'),
(5, 'Cámaras'),
(6, 'Televisores'),
(7, 'Smartwatches'),
(8, 'Consolas de videojuegos'),
(9, 'Drones'),
(10, 'Monitores'),
(11, 'Teclados'),
(12, 'Mouses'),
(13, 'Routers'),
(14, 'Impresoras'),
(15, 'Proyectores'),
(16, 'Almacenamiento externo'),
(17, 'Cables y adaptadores'),
(18, 'Baterías portátiles'),
(19, 'Altavoces Bluetooth'),
(20, 'Accesorios para automóviles');

INSERT INTO Producto (CodigoProducto, Nombre, CodigoCategoria) VALUES



-- Smartphones
(1, 'iPhone 14 Pro', 1),
(2, 'Samsung Galaxy S23', 1),
(3, 'Google Pixel 7', 1),
(4, 'Xiaomi Mi 13', 1),
(5, 'OnePlus 11', 1),

-- Laptops
(6, 'MacBook Air M2', 2),
(7, 'Dell XPS 13', 2),
(8, 'HP Spectre x360', 2),
(9, 'Lenovo ThinkPad X1', 2),
(10, 'Asus ZenBook 14', 2),

-- Tablets
(11, 'iPad Pro 12.9"', 3),
(12, 'Samsung Galaxy Tab S8', 3),
(13, 'Microsoft Surface Go 3', 3),
(14, 'Lenovo Tab P11 Pro', 3),
(15, 'Amazon Fire HD 10', 3),

-- Auriculares
(16, 'AirPods Pro', 4),
(17, 'Sony WH-1000XM5', 4),
(18, 'Bose QuietComfort 45', 4),
(19, 'JBL Tune 760NC', 4),
(20, 'Beats Studio3', 4),

-- Cámaras
(21, 'Canon EOS R10', 5),
(22, 'Sony Alpha a6400', 5),
(23, 'Nikon Z50', 5),
(24, 'Fujifilm X-T30 II', 5),
(25, 'Panasonic Lumix G100', 5),

-- Televisores
(26, 'Samsung QLED 55"', 6),
(27, 'LG OLED CX 65"', 6),
(28, 'Sony Bravia XR 75"', 6),
(29, 'TCL Roku TV 50"', 6),
(30, 'Hisense ULED 65"', 6),

-- Smartwatches
(31, 'Apple Watch Series 8', 7),
(32, 'Samsung Galaxy Watch 6', 7),
(33, 'Garmin Fenix 7', 7),
(34, 'Fitbit Versa 4', 7),
(35, 'Amazfit GTR 4', 7),

-- Consolas de videojuegos
(36, 'PlayStation 5', 8),
(37, 'Xbox Series X', 8),
(38, 'Nintendo Switch OLED', 8),
(39, 'Steam Deck 512GB', 8),
(40, 'PlayStation 5 Digital', 8),

-- Drones
(41, 'DJI Mini 3 Pro', 9),
(42, 'DJI Air 2S', 9),
(43, 'Autel EVO Nano+', 9),
(44, 'Ryze Tello', 9),
(45, 'Parrot Anafi', 9),

-- Monitores
(46, 'LG UltraGear 27"', 10),
(47, 'Dell UltraSharp 32"', 10),
(48, 'Samsung Odyssey G7', 10),
(49, 'ASUS ROG Swift 27"', 10),
(50, 'BenQ EX3501R', 10),

-- Teclados
(51, 'Logitech MX Keys', 11),
(52, 'Razer Huntsman Elite', 11),
(53, 'Corsair K95 RGB', 11),
(54, 'Keychron K6', 11),
(55, 'SteelSeries Apex Pro', 11),

-- Mouses
(56, 'Logitech MX Master 3S', 12),
(57, 'Razer DeathAdder V2', 12),
(58, 'Corsair Dark Core RGB', 12),
(59, 'Glorious Model O', 12),
(60, 'SteelSeries Rival 600', 12),

-- Routers
(61, 'TP-Link Archer AX6000', 13),
(62, 'Netgear Nighthawk AX12', 13),
(63, 'ASUS RT-AX88U', 13),
(64, 'Google Nest WiFi', 13),
(65, 'Linksys Velop MX5300', 13),

-- Impresoras
(66, 'HP LaserJet Pro M404', 14),
(67, 'Canon PIXMA G6020', 14),
(68, 'Brother HL-L2350DW', 14),
(69, 'Epson EcoTank ET-4760', 14),
(70, 'Samsung Xpress M2020W', 14),

-- Proyectores
(71, 'BenQ HT2050A', 15),
(72, 'Epson Home Cinema 2250', 15),
(73, 'LG CineBeam PF50KA', 15),
(74, 'ViewSonic PX701HD', 15),
(75, 'Anker Nebula Capsule II', 15),

-- Almacenamiento externo
(76, 'Samsung T7 1TB SSD', 16),
(77, 'WD My Passport 2TB', 16),
(78, 'Seagate Expansion 4TB', 16),
(79, 'SanDisk Extreme 1TB', 16),
(80, 'Crucial X8 2TB', 16),

-- Cables y adaptadores
(81, 'Cable USB-C a Lightning', 17),
(82, 'Adaptador HDMI a VGA', 17),
(83, 'Cable DisplayPort 1.4', 17),
(84, 'Hub USB-C 7 en 1', 17),
(85, 'Extensor Ethernet Cat6', 17),

-- Baterías portátiles
(86, 'Anker PowerCore 10000', 18),
(87, 'Xiaomi Mi Power Bank 3', 18),
(88, 'RAVPower 20000mAh', 18),
(89, 'Mophie Powerstation XL', 18),
(90, 'Zendure SuperTank Pro', 18),

-- Altavoces Bluetooth
(91, 'JBL Flip 6', 19),
(92, 'Bose SoundLink Flex', 19),
(93, 'Sony SRS-XB43', 19),
(94, 'Ultimate Ears BOOM 3', 19),
(95, 'Marshall Emberton', 19),

-- Accesorios para automóviles
(96, 'Soporte magnético para celular', 20),
(97, 'Cargador USB para auto', 20),
(98, 'Transmisor FM Bluetooth', 20),
(99, 'Cámara de reversa', 20),
(100, 'Organizador de asiento', 20),
(101,  'Aromatizador', 20);

DECLARE @i INT = 1;

WHILE @i <= 500
BEGIN
    INSERT INTO Venta (CodigoVenta, Fecha, CodigoProducto)
    VALUES (
        @i,
        -- Fecha aleatoria entre 2015-01-01 y 2020-12-31
        DATEADD(DAY, ABS(CHECKSUM(NEWID())) % DATEDIFF(DAY, '2015-01-01', '2020-12-31'), '2015-01-01'),
        -- CodigoProducto aleatorio entre 1 y 100
        (ABS(CHECKSUM(NEWID())) % 100) + 1
    );

    SET @i = @i + 1;
END;