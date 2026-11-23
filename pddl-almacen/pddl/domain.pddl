(define (domain almacen-automatizado)
  (:requirements :strips :typing)

  (:types
    zona robot lote tarjeta estante - object)

  (:predicates
    (conectada ?a - zona ?b - zona)
    (zona-libre ?z - zona)
    (zona-desbloqueada ?z - zona)
    (zona-inspeccion ?z - zona)
    (tarjeta-de ?t - tarjeta ?z - zona)

    (estante-en ?e - estante ?z - zona)
    (estante-vacio ?e - estante)
    (destino ?l - lote ?e - estante)

    (robot-en ?r - robot ?z - zona)
    (manos-libres ?r - robot)
    (cargando ?r - robot ?l - lote)
    (tiene-tarjeta ?r - robot ?t - tarjeta)

    (lote-en ?l - lote ?z - zona)
    (lote-inspeccionado ?l - lote)
    (lote-almacenado ?l - lote ?e - estante)
    (tarjeta-en ?t - tarjeta ?z - zona))

  (:action mover
    :parameters (?r - robot ?de - zona ?a - zona)
    :precondition (and (robot-en ?r ?de)
                       (conectada ?de ?a)
                       (zona-libre ?a))
    :effect (and (robot-en ?r ?a)
                 (not (robot-en ?r ?de))))

  (:action mover-restringida
    :parameters (?r - robot ?de - zona ?a - zona)
    :precondition (and (robot-en ?r ?de)
                       (conectada ?de ?a)
                       (zona-desbloqueada ?a))
    :effect (and (robot-en ?r ?a)
                 (not (robot-en ?r ?de))))

  (:action tomar-tarjeta
    :parameters (?r - robot ?t - tarjeta ?z - zona)
    :precondition (and (robot-en ?r ?z)
                       (tarjeta-en ?t ?z)
                       (manos-libres ?r))
    :effect (and (tiene-tarjeta ?r ?t)
                 (not (tarjeta-en ?t ?z))))

  (:action desbloquear-zona
    :parameters (?r - robot ?t - tarjeta ?de - zona ?z - zona)
    :precondition (and (robot-en ?r ?de)
                       (conectada ?de ?z)
                       (tiene-tarjeta ?r ?t)
                       (tarjeta-de ?t ?z))
    :effect (and (zona-desbloqueada ?z)
                 (not (tiene-tarjeta ?r ?t))))

  (:action recoger
    :parameters (?r - robot ?l - lote ?z - zona)
    :precondition (and (robot-en ?r ?z)
                       (lote-en ?l ?z)
                       (manos-libres ?r))
    :effect (and (cargando ?r ?l)
                 (not (lote-en ?l ?z))
                 (not (manos-libres ?r))))

  (:action soltar
    :parameters (?r - robot ?l - lote ?z - zona)
    :precondition (and (robot-en ?r ?z)
                       (cargando ?r ?l))
    :effect (and (lote-en ?l ?z)
                 (manos-libres ?r)
                 (not (cargando ?r ?l))))

  (:action inspeccionar-lote
    :parameters (?r - robot ?l - lote ?z - zona)
    :precondition (and (robot-en ?r ?z)
                       (zona-inspeccion ?z)
                       (lote-en ?l ?z)
                       (manos-libres ?r))
    :effect (lote-inspeccionado ?l))

  (:action almacenar
    :parameters (?r - robot ?l - lote ?e - estante ?z - zona)
    :precondition (and (robot-en ?r ?z)
                       (cargando ?r ?l)
                       (estante-en ?e ?z)
                       (estante-vacio ?e)
                       (destino ?l ?e)
                       (lote-inspeccionado ?l))
    :effect (and (lote-almacenado ?l ?e)
                 (manos-libres ?r)
                 (not (cargando ?r ?l))
                 (not (estante-vacio ?e))))
)
