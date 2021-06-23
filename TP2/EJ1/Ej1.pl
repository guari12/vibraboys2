/*Verificacion de la evacuacion continua de gas*/
verificar(piloto_ok) :-
    (
        (estado(piloto_ok, desconocido), estado(leakage_prevention_between_sit_and_orifice, yes), writeln('Verificar Pilot'));
        (estado(piloto_ok, yes), writeln('Set the valve acording to the instructions'));
        (estado(piloto_ok, no), writeln('Make a full service and reinstall it'));
        verificar(sit_and_orifice_ok)
    ).

verificar(sit_and_orifice_ok) :-
    (
        (estado(sit_and_orifice_ok, desconocido), estado(safety_valve_spring_ok, yes), writeln('Verificar leakage prevention between sit and orifice'));
        (estado(sit_and_orifice_ok, no), writeln('Replace sit and orifice and put the safety valve into circuit'));
        verificar(safety_valve_spring_ok)
    ).

verificar(safety_valve_spring_ok) :-
(
    (estado(safety_valve_spring_ok, desconocido), estado(control_valve_sensors_blocked, no), writeln('Verificar safety valve spring'));
    (estado(safety_valve_spring_ok, no), writeln('Put spring and safety valve in service'));
    verificar(control_valve_sensors_blocked)
).

verificar(control_valve_sensors_blocked) :-
(
    (estado(control_valve_sensors_blocked, desconocido), estado(valve_status_closed, no), writeln('Verificar control valve sensors'));
    (estado(control_valve_sensors_blocked, yes), writeln('Clean and troubleshoot the sensing pipes'));
    verificar(valve_status_closed)
).
    
verificar(valve_status_closed) :- 
(
    (estado(valve_status_closed, desconocido), estado(relief_valve_ok_with_10_percent_more_pressure, no), writeln('Verificar valve status "Close"'));
    (estado(valve_status_closed, yes), writeln('Place the safety valve in "Open"'));
    verificar(relief_valve_ok_with_10_percent_more_pressure)
).
    
verificar(relief_valve_ok_with_10_percent_more_pressure) :- 
(
    (estado(relief_valve_ok_with_10_percent_more_pressure, desconocido), estado(safety_valve_has_continuous_evacuation, no), writeln('Verificar si relief valve works correctly with +10% over regular pressure')); 
    (estado(relief_valve_ok_with_10_percent_more_pressure, yes),  writeln('Safety function appropriate'));
    verificar(safety_valve_has_continuous_evacuation)  
).

verificar(safety_valve_has_continuous_evacuation) :- 
    (
        (estado(safety_valve_has_continuous_evacuation, desconocido), writeln('Verificar the evacuation of safety valve'));
    	verificar(preventable_leakage_between_sit_and_orifice)
    ).

verificar(preventable_leakage_between_sit_and_orifice) :-
    (
        (estado(preventable_leakage_between_sit_and_orifice, desconocido), estado(safety_spring_ok, yes), writeln('Verificar if there is a preventable leakage'));  
        (estado(preventable_leakage_between_sit_and_orifice, no), writeln('Replace sit and orifice and put the safety valve into circuit'));
        (estado(preventable_leakage_between_sit_and_orifice, yes), writeln('Set the safety valve acording to the instructions'));
        verificar(safety_spring_ok)
    ).

verificar(safety_spring_ok) :-
    (
        (estado(safety_spring_ok, desconocido), estado(pressure_sensor_pipes_blocked, no), writeln('Verificar if safety spring is effective'));
        (estado(safety_spring_ok, no), writeln('Replace the safety spring'));
        verificar(pressure_sensor_pipes_blocked)
    ).

verificar(pressure_sensor_pipes_blocked) :-
    (
        (estado(pressure_sensor_pipes_blocked, desconocido), estado(line_gas_pressure_ok, yes), writeln('Verificar if pressure sensor pipes are blocked'));
        (estado(pressure_sensor_pipes_blocked, yes), writeln('Clean up and fix the faults of sensing pipes'));
        verificar(line_gas_pressure_ok)
    ).
verificar(line_gas_pressure_ok) :-
    (
        (estado(line_gas_pressure_ok, desconocido), estado(safety_valve_has_continuous_evacuation, yes), writeln('Verificar line gas pressure'));
        (estado(line_gas_pressure_ok, no), writeln('Please adjust the regulator acording to the instructions'));
    	verificar(leakage_fixed_with_wrench)
    	/*verificar(safety_valve_has_continuous_evacuation)*/
    ).
/*---------------------------------------------------------------------------------------------*/

/*Verificacion del espesor de tubrias*/
verificar(safety_system_having_dazzling_rusting_efects) :- 
                (
                    (estado(safety_system_having_dazzling_rusting_efects, desconocido), writeln('Verificar safety system dazzling and rusting efects'));
                    (estado(safety_system_having_dazzling_rusting_efects, yes), writeln('Coordination is required in order to render and color the equipment'));
                    verificar(piloto_ok)
                ). 

verificar(thickness_less_than_limit) :-
                (
                    (estado(thickness_less_than_limit, desconocido), estado(safety_system_having_dazzling_rusting_efects, no),writeln('Verificar system thickness'));
                    (estado(thickness_less_than_limit, yes), writeln('Please report to technical inspection unit'));
                    (estado(thickness_less_than_limit, no), writeln('Equipment in good conticions'));
                    verificar(safety_system_having_dazzling_rusting_efects)
                ).
/*---------------------------------------------------------------------------------------------*/


/*Verificacion de fugas de gas*/
verificar(gas_leakage_at_joint) :-
                (
                    (estado(gas_leakage_at_joint, desconocido), writeln('Verificar leakage at joint'));
                    (estado(gas_leakage_at_joint, no), writeln('The safety gas joint is free of gas'))
                ).

verificar(leakage_fixed_with_wrench) :-
                (
                    (estado(leakage_fixed_with_wrench, yes), writeln('Report to technical inspection unit'));
                    (estado(leakage_fixed_with_wrench, no), writeln('Report to the repair departament'));
                    (estado(leakage_fixed_with_wrench, desconocido), (estado(gas_leakage_at_joint, yes), writeln('Verificar si leakage was fixed with wrench')));
                    verificar(gas_leakage_at_joint)
                ).
/*---------------------------------------------------------------------------------------------*/

/*==========================================================================*/
verificar(sistema) :-
    estado(sistema, desconocido), writeln('Analizando sistema...'), writeln(''), 
	(   
    	verificar(thickness_less_than_limit)
    ).

/* Ground Facts de instancia variables (podrian resolverse mediante sensado o agregando la informacion interactivamente a la base de conocimientos) */

/*Verificacion de la evacuacion continua de gas*/
estado(piloto_ok, desconocido).
estado(sit_and_orifice_ok, desconocido).
estado(safety_valve_spring_ok, desconocido).
estado(control_valve_sensors_blocked, desconocido).
estado(valve_status_closed, desconocido).
estado(relief_valve_ok_with_10_percent_more_pressure, desconocido).
estado(safety_valve_has_continuous_evacuation, desconocido).

estado(line_gas_pressure_ok, desconocido).
estado(pressure_sensor_pipes_blocked, desconocido).
estado(safety_spring_ok, desconocido).
estado(preventable_leakage_between_sit_and_orifice, desconocido).
/*---------------------------------------------------------------------------------------------*/


/*Verificacion del espesor de tubrias*/
estado(thickness_less_than_limit, desconocido).
estado(safety_system_having_dazzling_rusting_efects, desconocido).
/*---------------------------------------------------------------------------------------------*/

/*Verificacion de fugas de gas*/
estado(gas_leakage_at_joint, desconocido).
estado(leakage_fixed_with_wrench, desconocido).
/*---------------------------------------------------------------------------------------------*/

estado(sistema, desconocido).
