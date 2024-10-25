;;JAVIER GARCÍA MESA u32896608 PRACTICA 1 IA
;;EJERCICIO 1
(deffacts ciudades_iniciales
    (ubicacion Sevilla Norte Cadiz)
    (ubicacion Sevilla Oeste Cordoba)
)

(defrule inversa1
    (ubicacion ?x Sur ?y)
    => (assert (ubicacion ?y Norte ?x))
)

(defrule inversa2
    (ubicacion ?x Norte ?y)
    => (assert (ubicacion ?y Sur ?x))
)

(defrule inversa3
    (ubicacion ?x Este ?y)
    => (assert (ubicacion ?y Oeste ?x))
)

(defrule inversa4
    (ubicacion ?x Oeste ?y)
    => (assert (ubicacion ?y Este ?x))
)

(defrule transi1
    (ubicacion ?x Norte ?y) (ubicacion ?y Norte ?z)
    => (assert (ubicacion ?x Norte ?z))
)

(defrule transi2
    (ubicacion ?x Sur ?y) (ubicacion ?y Sur ?z)
    => (assert (ubicacion ?x Sur ?z))
)

(defrule transi3
    (ubicacion ?x Oeste ?y) (ubicacion ?y Oeste ?z)
    => (assert (ubicacion ?x Oeste ?z))
)

(defrule transi4
    (ubicacion ?x Este ?y) (ubicacion ?y Este ?z)
    => (assert (ubicacion ?x Este ?z))
)

(defrule transi5
    (ubicacion ?x Norte ?y) (ubicacion ?y Este ?z)
    => (assert (ubicacion ?x Noreste ?z))
)

(defrule transi6
    (ubicacion ?x Norte ?y) (ubicacion ?y Oeste ?z)
    => (assert (ubicacion ?x Noroeste ?z))
)

(defrule transi7
    (ubicacion ?x Sur ?y) (ubicacion ?y Este ?z)
    => (assert (ubicacion ?x Sureste ?z))
)

(defrule transi8
    (ubicacion ?x Sur ?y) (ubicacion ?y Oeste ?z)
    => (assert (ubicacion ?x Suroeste ?z))
)

(defrule inicio
?f1 <-(situacion ?x ?y)
(ubicacion ?x ?u ?y)
=>
(printout t ?x " esta al " ?u " de " ?y crlf)
(retract ?f1)
)

;;EJERCICIO 2
(deftemplate Coche
    (slot Modelo)
    (slot Precio (type INTEGER))
    (slot Maletero (allowed-values Pequeño Mediano Grande))
    (slot Caballos (type INTEGER))
    (slot ABS (allowed-values Sí No))
    (slot Consumo (type FLOAT))
)

(deftemplate Preferencia
    (multislot Cliente)
    (slot Precio (type INTEGER) (default 13000))
    (slot Maletero (allowed-values Pequeño Mediano Grande) (default Grande))
    (slot Caballos (type INTEGER) (default 80))
    (slot ABS (allowed-values Sí No) (default Sí))
    (slot Consumo (type FLOAT) (default 8.0)) ;;TIPO FLOAT
)

(deffacts modelos_iniciales
    (Coche (Modelo Modelo1) (Precio 12000) (Maletero Pequeño) (Caballos 65) (ABS No) (Consumo 4.7))
    (Coche (Modelo Modelo2) (Precio 12500) (Maletero Pequeño) (Caballos 80) (ABS Sí) (Consumo 4.9))
    (Coche (Modelo Modelo3) (Precio 13000) (Maletero Mediano) (Caballos 100) (ABS Sí) (Consumo 7.8))
    (Coche (Modelo Modelo4) (Precio 14000) (Maletero Grande) (Caballos 125) (ABS Sí) (Consumo 6.0))
    (Coche (Modelo Modelo5) (Precio 15000) (Maletero Pequeño) (Caballos 147) (ABS Sí) (Consumo 8.5))
)

(defrule Modelo_Elegido
    (Coche (Modelo ?x1) (Precio ?x2) (Maletero ?x3) (Caballos ?x4) (ABS ?x5) (Consumo ?x6))
    (Preferencia (Cliente ?y1) (Precio ?y2) (Maletero ?y3) (Caballos ?y4) (ABS ?y5) (Consumo ?y6))
    (test (<= ?x2 ?y2))
    (test (eq ?x3 ?y3)) ;;PARA COMPARAR VALORES ENUMERADOS (EL INVERSO ES neq)
    (test (>= ?x4 ?y4))
    (test (eq ?x5 ?y5))
    (test (<= ?x6 ?y6))
    => (printout t "Al cliente " ?y1 " le conviene el " ?x1 crlf) ;;crlf ES SALTO DE LÍNEA
)


