;;hechos estructuros
(deftemplate persona
    (multislot nombre) ;Permite nombre y apellidos
    (slot dni (type INTEGER)) ;definimos tipo
    (slot profession (default estudiante)) ;por defecto
    (slot nacionalidad (allowed-values Es Fr Po)) ;valores disponibles
)

(deftemplate rectangulo
    (slot altura)
    (slot base)
)

(deffacts iniciales
    (persona (nombre Mario Cantero)
    (dni 122234)
    (profession escritor)
    (nacionalidad Es)
    )
    (persona (nombre Juana Bodega Gallego))
    ;;Hechos no estructurados
    (ciudad Barbate Cadiz)
)

;;PARA AÑADIR, hacemos un (clear) LE DAMOS A Load Current File y luego en la terminal hacer (reset)

;;(facts) ;;visualizar los hechos actuales

;;(reset) ;;para que se muestren los hechos en facts

;;(assert (ciudad Juana Cadiz))
;;(assert (persona (nombre Alicia) (dni 1235)))

;;(retract 1) Para eliminar el hecho uno
;;(modify 1 (nombre Maria Juarez)) para modificar un dato ESTRUCTURADO. El numero
;;es el indice del facts

;;(duplicate 2 (nombre Maria Bodega Gallego) (dni 11)) Para duplicar modificando lo que quiero

(defrule frances
    (persona (nombre ?x) (nacionalidad Fr))
    => (assert (ciudad ?x Paris))
)
;; Si la persona es francesa, es de Paris

;;(assert (hermanos Juan Pedro Paula Patricia))
(defrule mostrarHermano
    (hermanos Juan $?resto)
    => (printout t "Los hermanos de Juan son " $?resto crlf)
)

;;$?x hace referencia a una variable multivalor (multislot)

;; ?dir <- (ciudad Barbate Cadiz) para asignar un hecho a una variable
;;EJEMPLO:
;;(defrule casamiento (comprometidos ?x ?y) ?dir <- (soltero ?x) => assert(retract ?dir))

;;(defglobal ?*numero* = 10) ;; VARIABLES GLOBALES

(defrule calcular_area
    (rectangulo (altura ?x) (base ?y))
    => (assert (area (* ?x ?y)))
)

(defrule no_esp
    (persona (nombre ?x) (nacionalidad ~Es)) ;;Negacion
    => (printout t "La persona " ?x " no es español")
)

(defrule esp_fr
    (persona (nombre ?x) (nacionalidad Es | Fr))
    => (printout t "La persona " ?x " es española o francesa")
)