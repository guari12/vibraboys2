(define (problem capp-pieza)
    (:domain capp)
    (:objects 
        orientacionX
        orientacionY
        orientacionZ
        orientacion-X
        orientacion-Y
        orientacion-Z
        s2
        s4
        s6
        s9
        s10
        slot
        through-hole
        blind-hole
        fresado
        taladrado
        torneado
    )
    (:init 
        (orientacion orientacionX)
        (orientacion orientacionY)
        (orientacion orientacionZ)
        (orientacion orientacion-X)
        (orientacion orientacion-Y)
        (orientacion orientacion-Z)
        (feature s2)
        (feature s4)
        (feature s6)
        (feature s9)
        (feature s10)
        (tipo slot)
        (tipo through-hole)
        (tipo blind-hole)
        (operacion fresado)
        (operacion taladrado)
        (operacion torneado)
        (feature-tipo s2 slot)
        (feature-tipo s4 slot)
        (feature-tipo s6 slot)
        (feature-tipo s9 slot)
        (feature-tipo s10 slot)
        (orientacion-pieza orientacion-X)
        (orientacion-feature s2 orientacionX)
        (orientacion-feature s4 orientacion-X)
        (orientacion-feature s6 orientacionX)
        (orientacion-feature s9 orientacionZ)
        (orientacion-feature s10 orientacionZ)
        (fabricable slot fresado)
    )
    (:goal 
        (and
            (fabricada s2)
            (fabricada s4)
            (fabricada s6)
            (fabricada s9)
            (fabricada s10)
        )
    )
)