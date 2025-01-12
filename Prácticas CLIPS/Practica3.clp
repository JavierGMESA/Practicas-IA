(deftemplate aeronave ;;IMPORTANTE: PUEDES HACER UN ASSERT DE UNA PLANTILLA SIN RELLENAR SUS CAMPOS
    (slot id_ae)
    (slot id_o)
    (slot id_d)
    (slot peticion (allowed-values Ninguna Despegue Aterrizaje Emergencia Rumbo))
    (slot estado (allowed-values enTierra Ascenso Crucero Descenso) (default enTierra))
    (slot compañia)
    (slot velocidad)
)

(deftemplate aerodromo
    (slot id)
    (slot ciudad)
    (slot radar (allowed-values ON OFF))
    (slot visibilidad)
    (slot viento)
)

(deftemplate piloto
    (slot id_ae)
    (slot estado (allowed-values OK SOS Ejecutando StandBy) (default StandBy))
)

(deftemplate vuelo
    (slot id_o)
    (slot id_d)
    (slot distancia)
    (slot v_despegue (default 240))
    (slot v_crucero (default 700))
)

(deffunction tiempH (?v ?d)
    (bind ?h (div ?d ?v))
    (return ?h)
)

(deffunction tiempM (?v ?d)
    (bind ?m (mod ?d ?v))       ;IMPORTANTE: DIVISIÓN
    (bind ?v (div ?v 60))       ;IMPORTANTE: MÓDULO
    (bind ?r (div ?m ?v))
    (return ?r)
)

(defrule Despegar
    ?ae <- (aeronave (id_ae ?x) (id_o ?o) (id_d ?d) (estado enTierra) (peticion Despegue) (compañia ?c))
    ?p <- (piloto (id_ae ?x) (estado OK))
    (vuelo (id_o ?o) (id_d ?d) (v_despegue ?vel))
    (aerodromo (id ?o) (ciudad ?ci1) (radar ON) (visibilidad ?v1) (viento ?v2))
    (aerodromo (id ?d) (ciudad ?ci2))
    (test (> ?v1 5))
    (test (< ?v2 75))
    => 
    (modify ?p (estado Ejecutando))
    (modify ?ae (estado Ascenso) (velocidad ?vel) (peticion Ninguna))
    (printout t "La aeronave " ?x " de la compañía " ?c " va a realizar la acción de despegue desde el aerodromo " ?o)
    (printout t " de " ?ci1 " con destino " ?ci2 "." crlf)
)

(defrule Excepcion
    ?ae <- (aeronave (id_ae ?x) (id_o ?o) (id_d ?d) (peticion Despegue) (compañia ?c))
    (piloto (id_ae ?x) (estado ~OK))
    (aerodromo (id ?o))
    (aerodromo (id ?d))
    =>
    (modify ?ae (peticion Emergencia))
    (printout t "ATENCION El piloto de la aeronave " ?x " de la compañia " ?c " no se encuentra disponible para iniciar el despegue ")
    (printout t "desde el aerodromo " ?o " con destino " ?d "." crlf)
)

(defrule Crucero
    ?ae <- (aeronave (id_ae ?x) (velocidad ?v0) (id_o ?o) (id_d ?d) (estado Ascenso))
    ?p <- (piloto (id_ae ?x) (estado Ejecutando))
    (aerodromo (id ?o) (ciudad ?c1))
    (aerodromo (id ?d) (ciudad ?c2))
    (vuelo (id_o ?o) (id_d ?d) (v_crucero ?v1) (distancia ?dis))
    =>
    (modify ?ae (velocidad ?v1) (estado Crucero))
    (modify ?p (estado StandBy))
    (printout t "ATENCION PASAJEROS: El despegue del vuelo con origen aerodromo " ?o " de la ciudad " ?c1)
    (printout t " y destino aerodromo " ?d " de la ciudad " ?c2 " ha realizado su despegue correctamente. ")
    (printout t "El tiempo de vuelo estimado es de " (tiempH ?v1 ?dis) " horas y " (tiempM ?v1 ?dis) " minutos." crlf) ;;IMPORTANTE: USO DE FUNCIÓN EN printout
)

(deffacts iniciales
    (aeronave (id_ae 1234) (id_o F1) (id_d F2) (peticion Despegue) (estado enTierra) (compañia Boeing) (velocidad 0))
    (aerodromo (id F1) (ciudad ElPuerto) (radar ON) (visibilidad 10) (viento 50))
    (aerodromo (id F2) (ciudad Jerez) (radar ON) (visibilidad 10) (viento 50))
    (piloto (id_ae 1234) (estado OK))
    (vuelo (id_o F1) (id_d F2) (distancia 1000) (v_despegue 120) (v_crucero 230))
    (aeronave (id_ae 1235) (id_o F1) (id_d F2) (peticion Despegue) (estado enTierra) (compañia Boeing) (velocidad 0))
    (piloto (id_ae 1235) (estado SOS))
)