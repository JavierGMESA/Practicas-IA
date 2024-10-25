;;Ejercicio de las valvulas

(deftemplate valvula
    (slot nombre)
    (slot estado (allowed-values abierta cerrada) (default cerrada))
    (slot presion (default 0))
    (slot T1 (default 0))
    (slot T2 (default 0))
)

(deffunction aumpres (?p ?t1) ;;IMPORTANTE: TODO LO QUE VAYA DESPUÉS DEL PRIMER PARÉNTESIS EN UNA FUNCIÓN
    (bind ?res ?p)            ;;IMPORTANTE: SE CONSIDERA EL CUERPO DE LA FUNCIÓN (Y LO ANTERIOR LO ARGUMENTOS)
    (while (> ?t1 35)         ;;IMPORTANTE: BUCLE while
        (bind ?res (+ ?res 1))
        (bind ?t1 (- ?t1 5))
    )
    (return ?res)             ;;IMPORTANTE: USO DEL RETURN
    
)

(deffunction decrement (?t1 ?t2)
    (if (> ?t2 ?t1) then            ;;IMPORTANTE: IF-THEN
        (bind ?t2 (- ?t2 ?t1))
    )
    (return ?t2)
)

(deffacts Iniciales
    (valvula (nombre Entrada) (T1 101) (T2 35) (presion 1))
    (valvula (nombre Salida) (T1 101) (T2 155) (presion 5))
    (valvula (nombre Pasillo1) (T1 99) (T2 37) (estado cerrada))
)

(defrule R1
    ?v <- (valvula (presion 5) (estado abierta))
    => (modify ?v (presion 0) (estado cerrada))
)

(defrule R2
    ?v <- (valvula (estado cerrada) (presion ?p) (T1 ?t1))
    (test (> ?t1 35))
    (test (< ?p 10))
    => (modify ?v (estado abierta) (presion (aumpres ?p ?t1))) 
)

(defrule R3
    ?v1 <- (valvula (nombre ?n1) (T2 ?t))
    ?v2 <- (valvula (nombre ?n2) (T1 ?t12) (T2 ?t))
    (test (neq ?n1 ?n2))
    (test (< ?t12 ?t))
    => (modify ?v1 (estado cerrada))
    (modify ?v2 (estado cerrada) (T2 (decrement ?t12 ?t)))
)

