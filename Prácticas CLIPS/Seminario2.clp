(defglobal ?*LIMIT1* = 900
            ?*ANNO* = 2023) ;;HAY QUE DEJAR ESPACIOS ENTRE EL =

;;EJERCICIO 2: PAC-MAN
(deftemplate comecocos 
    (slot posX (default 0)) ;;Mejor no definir el tipo
    (slot posY (default 0)) 
    (slot contador ) 
    (slot Vida (default 3)) 
)

(deftemplate fantasma
    (slot posX ) 
    (slot posY ) 
)

(deftemplate fruta
    (slot posX ) 
    (slot posY ) 
)

(defrule COMER
?come <- (comecocos (posX ?x) (posY ?y) (contador ?c)) ;;IMPORTANTE: NO HACE FALTA GUARDAR LA Vida 
?frut <- (fruta (posX ?x) (posY ?y)) ;;IMPORTANTE: PONEMOS x E y ARRIBA Y ABAJO -> NOS EVITAMOS LOS test
=> (retract ?frut) ;;borramos la fruta
(modify ?come (contador (+ ?c 1))) ;;IMPORTANTE: MODIFICACIÓN DEL comecocos
)

(defrule MORIR
?come <- (comecocos (posX ?x) (posY ?y) (Vida ?v))
    (fantasma (posX ?x) (posY ?y))
=> (modify ?come (posX 1) (posY 1) (Vida (- ?v 1)))
)

(defrule GANAR
    (comecocos (posX ?x) (posY ?y) (contador ?c))
    (test (> ?c 9))
    => (printout t "Ha ganado la partida" crlf)
)

(defrule GAMEOVER
    (comecocos (posX ?x) (posY ?y) (contador 0))
    => (printout t "Ha perdido la partida" crlf)
)

;;EJERCICIO CAJERO AUTOMÁTICO
(deftemplate Usuario
    (slot DNI)
    (slot Pin)
    (slot Dinero (default 0))
)

(deftemplate Tarjeta
    (slot Pin)
    (slot DNI)
    (slot Intentos (default 3))
    (slot Limite (default 100.00))
    (slot Anno)
    (slot Validacion (allowed-values Si No) (default No))
)

(deftemplate Cuenta
    (slot DNI)
    (slot Saldo)
    (slot Estado (allowed-values enPantalla dineroEntregado Inicial SuperaLimite SinSaldo) (default Inicial))
)



(deffunction decrementar (?num)
    (- ?num 1)
)

(deffunction diferencia (?num1 ?num2)
    (- ?num1 ?num2)
)

(deffacts Inciales
    (Tarjeta (DNI 123456) (Pin 1212) (Intentos 3) (Limite 500) (Anno 2026))
    (Tarjeta (DNI 456456) (Pin 4545) (Intentos 3) (Limite 500) (Anno 2026))
    (Tarjeta (DNI 000111) (Pin 0011) (Intentos 0) (Limite 500) (Anno 2026))
    (Cuenta (DNI 123456) (Saldo 5000))
    (Cuenta (DNI 456456) (Saldo 33))
    (Cuenta (DNI 000111) (Saldo 30000))
)

(defrule Supera_Intentos
    (declare (salience 50)) ;;IMPORTANTE: PRIORIDADES
    ?tar <- (Tarjeta (Intentos 0) (DNI ?dni))
    ?us <- (Usuario (DNI ?dni))
    => (printout t "La tarjeta se ha quedado sin intentos" crlf)
    (modify ?tar (Validacion No)) ;;NO HACE FALTA
    (retract ?us) ;;HECHO AL USUARIO
)

(defrule Pin_Invalido
    (Usuario (Pin ?p1) (DNI ?dni))
    ?tar <- (Tarjeta (Pin ?p2) (Intentos ?i) (DNI ?dni))
    (test (!= ?p1 ?p2))
    => (printout t "El pin es incorrecto" crlf)
    (modify ?tar (Intentos (decrementar ?i)))
)

(defrule Valida_Tarjeta
    (Usuario (DNI ?dni) (Pin ?p))
    ?tar <- (Tarjeta (DNI ?dni) (Intentos ?i) (Anno ?an) (Pin ?p) (Validacion No))
    (test (> ?i 0))
    (test (> ?an ?*ANNO*))
    => (modify ?tar (Validacion Si))
)

(defrule Muestra_Saldo
    (Usuario (DNI ?dni) (Pin ?pin))
    (Tarjeta (DNI ?dni) (Pin ?pin) (Validacion Si))
    ?c <- (Cuenta (DNI ?dni) (Saldo ?s) (Estado ~enPantalla&~dineroEntregado))
    => (printout t "El saldo es " ?s crlf)
    (modify ?c (Estado enPantalla))
)

(defrule Saldo_NoSuficiente
    (Usuario (DNI ?dni) (Pin ?pin))
    (Tarjeta (DNI ?dni) (Pin ?pin) (Validacion Si))
    (Cuenta (DNI ?dni) (Saldo 0.00))
    => (printout t "Su cuenta no tiene saldo" crlf)
)

(defrule CompruebaLimite2
    (Usuario (DNI ?dni) (Pin ?pin) (Dinero ?din))
    (Tarjeta (DNI ?dni) (Pin ?pin) (Limite ?lim) (Validacion Si))
    (Cuenta (DNI ?dni))
    (test (> ?din ?lim))
    => (printout t "El dinero a sacar es mayor que el limite de la tarjeta" crlf)
)

(defrule CompruebaLimite1
    (Usuario (DNI ?dni) (Dinero ?din))
    (Tarjeta (DNI ?dni) (Validacion Si))
    (Cuenta (DNI ?dni))
    (test (> ?din ?*LIMIT1*))
    => (printout t "El dinero a sacar es mayor que el limite del banco" crlf)
)

(defrule Entrega_Dinero
    (Usuario (DNI ?dni) (Dinero ?din))
    (Tarjeta (DNI ?dni) (Limite ?lim) (Validacion Si))
    ?c <- (Cuenta (DNI ?dni) (Saldo ?s) (Estado ~dineroEntregado))
    (test (<= ?din ?lim))
    (test (<= ?din ?*LIMIT1*))
    => (printout t "El saldo actual de su cuenta es " (diferencia ?s ?din) crlf)
    (modify ?c (Saldo (diferencia ?s ?din)) (Estado dineroEntregado))
)

(defrule Inicial
    (declare (salience 100))
    => (printout t "Introduzca su DNI" crlf)
    (bind ?dni (read))
    (printout t "Introduzca su Pin" crlf)
    (bind ?pin (read))
    (printout t "Introduzca el dinero a sacar" crlf)
    (bind ?din (read))
    (assert (Usuario (DNI ?dni) (Pin ?pin) (Dinero ?din)))
)



