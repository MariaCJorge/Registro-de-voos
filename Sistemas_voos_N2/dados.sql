SELECT * FROM vra_20257;
-- DELETE FROM vra_20257;
-- ALTER TABLE vra_20257 AUTO_INCREMENT = 1;
INSERT INTO vra_20257 (numero_voo, data_voo, origem, destino, horario_partida, horario_chegada, status_voo) VALUES
('VRA1001', '2024-01-15', 'São Paulo', 'Rio de Janeiro', '08:00:00', '09:00:00', 'On Time'),
('VRA1002', '2024-01-15', 'Rio de Janeiro', 'São Paulo', '10:00:00', '11:00:00', 'Delayed'),
('VRA1003', '2024-01-16', 'Belo Horizonte', 'Salvador', '12:00:00', '14:00:00', 'Cancelled'),
('VRA1004', '2024-01-16', 'Salvador', 'Belo Horizonte', '15:00:00', '17:00:00', 'On Time'),
('VRA1005', '2024-01-17', 'Curitiba', 'Porto Alegre', '18:00:00', '19:30:00', 'On Time');
INSERT INTO vra_20257 (numero_voo, data_voo, origem, destino, horario_partida, horario_chegada, status_voo) VALUES
('VRA1006', '2024-01-17', 'Porto Alegre', 'Curitiba', '20:00:00', '21:30:00', 'Delayed'),
('VRA1007', '2024-01-18', 'Fortaleza', 'Recife', '07:00:00', '08:30:00', 'On Time'),
('VRA1008', '2024-01-18', 'Recife', 'Fortaleza', '09:00:00', '10:30:00', 'On Time'),
('VRA1009', '2024-01-19', 'Manaus', 'Belém', '11:00:00', '12:30:00', 'Cancelled'),
('VRA1010', '2024-01-19', 'Belém', 'Manaus', '13:00:00', '14:30:00', 'On Time');      