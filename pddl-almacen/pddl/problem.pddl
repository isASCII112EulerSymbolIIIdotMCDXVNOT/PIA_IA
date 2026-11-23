(define (problem turno-manana)
  (:domain almacen-automatizado)

  (:objects
    recepcion inspeccion centro seguridad pasillo-a pasillo-b - zona
    robot-1 - robot
    lote-herramientas lote-quimicos - lote
    tarjeta-a tarjeta-b - tarjeta
    estante-a1 estante-b1 - estante)

  (:init
    (conectada recepcion inspeccion)   (conectada inspeccion recepcion)
    (conectada inspeccion centro)      (conectada centro inspeccion)
    (conectada centro seguridad)       (conectada seguridad centro)
    (conectada centro pasillo-a)       (conectada pasillo-a centro)
    (conectada pasillo-a pasillo-b)    (conectada pasillo-b pasillo-a)

    (zona-libre recepcion)
    (zona-libre inspeccion)
    (zona-libre centro)
    (zona-libre seguridad)
    (zona-inspeccion inspeccion)

    (tarjeta-en tarjeta-a seguridad)
    (tarjeta-de tarjeta-a pasillo-a)
    (tarjeta-en tarjeta-b seguridad)
    (tarjeta-de tarjeta-b pasillo-b)

    (estante-en estante-a1 pasillo-a)
    (estante-vacio estante-a1)
    (estante-en estante-b1 pasillo-b)
    (estante-vacio estante-b1)
    (destino lote-herramientas estante-a1)
    (destino lote-quimicos estante-b1)

    (robot-en robot-1 centro)
    (manos-libres robot-1)

    (lote-en lote-herramientas recepcion)
    (lote-en lote-quimicos recepcion))

  (:goal (and (lote-almacenado lote-herramientas estante-a1)
              (lote-almacenado lote-quimicos estante-b1)))
)
